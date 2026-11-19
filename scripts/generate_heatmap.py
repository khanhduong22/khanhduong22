#!/usr/bin/env python3
"""Generate dark and light numbered GitHub contribution heatmap SVGs."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
import re
import urllib.request
from xml.sax.saxutils import escape

MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
FONT_SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif"
FONT_MONO = "ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,monospace"


@dataclass(frozen=True)
class Theme:
    name: str
    bg: str
    border: str | None
    accent: str
    title: str
    divider: str
    muted: str
    badge_bg: str
    badge_text: str
    cell_fills: tuple[str, str, str, str, str]
    text_fills: tuple[str, str, str, str, str]
    zero_opacity: str


THEMES = (
    Theme(
        name="dark",
        bg="#0d1117",
        border=None,
        accent="#39d353",
        title="#58a6ff",
        divider="#30363d",
        muted="#8b949e",
        badge_bg="#39d353",
        badge_text="#39d353",
        cell_fills=("#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"),
        text_fills=("#6e7681", "#e6edf3", "#e6edf3", "#e6edf3", "#0d1117"),
        zero_opacity="0.55",
    ),
    Theme(
        name="light",
        bg="#ffffff",
        border="#d0d7de",
        accent="#2da44e",
        title="#0969da",
        divider="#d8dee4",
        muted="#57606a",
        badge_bg="#2da44e",
        badge_text="#1a7f37",
        cell_fills=("#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"),
        text_fills=("#8c959f", "#0a3622", "#0a3622", "#ffffff", "#ffffff"),
        zero_opacity="0.6",
    ),
)


@dataclass(frozen=True)
class DayCell:
    day: date
    level: int
    count: int


def fetch_contributions(username: str) -> list[DayCell]:
    """Fetch and parse GitHub's public contributions calendar HTML."""
    url = f"https://github.com/users/{username}/contributions"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "khanhduong22-heatmap-generator/1.0"},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        html = resp.read().decode("utf-8")

    by_id: dict[str, dict[str, object]] = {}
    for td_match in re.finditer(r"<td\b[^>]*>", html):
        tag = td_match.group(0)
        if "ContributionCalendar-day" not in tag:
            continue
        date_m = re.search(r'\bdata-date="(\d{4}-\d{2}-\d{2})"', tag)
        id_m = re.search(r'\bid="([^"]+)"', tag)
        level_m = re.search(r'\bdata-level="(\d)"', tag)
        if not (date_m and id_m and level_m):
            continue
        by_id[id_m.group(1)] = {
            "day": date.fromisoformat(date_m.group(1)),
            "level": min(max(int(level_m.group(1)), 0), 4),
            "count": 0,
        }

    for tip_match in re.finditer(r"<tool-tip\b([^>]*)>([^<]*)</tool-tip>", html):
        attrs, text = tip_match.group(1), tip_match.group(2).strip()
        for_m = re.search(r'\bfor="([^"]+)"', attrs)
        if not for_m:
            continue
        cid = for_m.group(1)
        if cid not in by_id:
            continue
        count_m = re.match(r"^(\d[\d,]*)\s+contribution", text)
        by_id[cid]["count"] = int(count_m.group(1).replace(",", "")) if count_m else 0

    if len(by_id) < 300:
        raise RuntimeError(
            f"Expected >= 300 contribution days for {username}, got {len(by_id)}"
        )

    days = [
        DayCell(day=item["day"], level=item["level"], count=item["count"])  # type: ignore[arg-type]
        for item in by_id.values()
    ]
    days.sort(key=lambda d: d.day)
    return days


def _font_size_for_count(count: int) -> int:
    digits = len(str(count))
    if digits <= 2:
        return 14
    if digits == 3:
        return 11
    return 9


def render_svg(days: list[DayCell], theme: Theme) -> str:
    """Render a self-contained SVG contribution calendar with daily counts."""
    cell = 30
    gap = 4
    pitch = cell + gap
    left_pad = 54
    top_pad = 88
    right_pad = 24
    bottom_pad = 44

    first_day = days[0].day
    last_day = days[-1].day
    start_sunday = first_day - timedelta(days=(first_day.weekday() + 1) % 7)
    num_weeks = ((last_day - start_sunday).days // 7) + 1

    width = left_pad + num_weeks * pitch - gap + right_pad
    height = top_pad + 7 * pitch - gap + bottom_pad

    total = sum(d.count for d in days)
    max_count = max(d.count for d in days)
    active_days = sum(1 for d in days if d.count > 0)

    badge_label = f"{total:,} contributions"
    badge_w = max(144, len(badge_label) * 7 + 28)
    badge_x = width - right_pad - badge_w
    badge_cx = badge_x + badge_w / 2

    parts: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(badge_label)}">',
        "<defs>",
        f'<clipPath id="card-clip-{theme.name}"><rect width="{width}" height="{height}" rx="8"/></clipPath>',
        "</defs>",
        "<style>",
        f".t{{font:600 14px {FONT_SANS}}}",
        f".b{{font:600 11px {FONT_SANS}}}",
        f".ax{{font:500 10px {FONT_SANS}}}",
        f".num{{font:700 14px {FONT_MONO}}}",
        "</style>",
        f'<g clip-path="url(#card-clip-{theme.name})">',
        f'<rect width="{width}" height="{height}" fill="{theme.bg}" rx="8"/>',
        f'<rect width="{width}" height="3" fill="{theme.accent}"/>',
        "</g>",
    ]

    if theme.border:
        parts.append(
            f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" fill="none" stroke="{theme.border}" rx="8"/>'
        )

    parts.extend(
        [
            f'<circle cx="32" cy="30" r="5" fill="{theme.accent}" opacity="0.2"/>',
            f'<circle cx="32" cy="30" r="2.5" fill="{theme.accent}"/>',
            f'<text x="44" y="34" class="t" fill="{theme.title}">Contributions</text>',
            f'<rect x="{badge_x}" y="19" width="{badge_w}" height="22" rx="11" fill="{theme.badge_bg}" opacity="0.14"/>',
            f'<text x="{badge_cx:.1f}" y="33.5" text-anchor="middle" class="b" fill="{theme.badge_text}">{escape(badge_label)}</text>',
            f'<line x1="24" y1="58" x2="{width - right_pad}" y2="58" stroke="{theme.divider}" stroke-width="1"/>',
        ]
    )

    last_month: tuple[int, int] | None = None
    last_label_col = -10
    for item in days:
        col = (item.day - start_sunday).days // 7
        ym = (item.day.year, item.day.month)
        if ym != last_month:
            last_month = ym
            if col - last_label_col >= 2 and col <= num_weeks - 2:
                lx = left_pad + col * pitch
                parts.append(
                    f'<text x="{lx}" y="76" class="ax" fill="{theme.muted}">{MONTHS[item.day.month - 1]}</text>'
                )
                last_label_col = col

    for row, day_label in ((1, "Mon"), (3, "Wed"), (5, "Fri")):
        ly = top_pad + row * pitch + cell / 2 + 3.5
        parts.append(
            f'<text x="{left_pad - 10}" y="{ly:.1f}" text-anchor="end" class="ax" fill="{theme.muted}">{day_label}</text>'
        )

    for item in days:
        col = (item.day - start_sunday).days // 7
        row = (item.day.weekday() + 1) % 7
        x = left_pad + col * pitch
        y = top_pad + row * pitch
        fill = theme.cell_fills[item.level]
        txt_fill = theme.text_fills[item.level]
        opacity_attr = f' opacity="{theme.zero_opacity}"' if item.count == 0 else ""
        font_size = _font_size_for_count(item.count)
        font_attr = f' style="font-size:{font_size}px"' if font_size != 14 else ""
        parts.append(
            f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="5" fill="{fill}"/>'
        )
        parts.append(
            f'<text x="{x + cell / 2:.1f}" y="{y + cell / 2 + font_size * 0.35:.1f}" text-anchor="middle" class="num"{font_attr} fill="{txt_fill}"{opacity_attr}>{item.count}</text>'
        )

    footer_y = height - 16
    parts.append(
        f'<text x="24" y="{footer_y}" class="ax" fill="{theme.muted}">Peak: {max_count}/day · Active: {active_days}d</text>'
    )

    legend_swatch = 14
    legend_gap = 4
    more_w = 34
    less_w = 32
    legend_start_x = width - right_pad - more_w - 5 * (legend_swatch + legend_gap) - less_w
    legend_y = height - 26
    parts.append(
        f'<text x="{legend_start_x}" y="{footer_y}" class="ax" fill="{theme.muted}">Less</text>'
    )
    sw_x = legend_start_x + less_w
    for idx, sw_fill in enumerate(theme.cell_fills):
        sx = sw_x + idx * (legend_swatch + legend_gap)
        parts.append(
            f'<rect x="{sx}" y="{legend_y}" width="{legend_swatch}" height="{legend_swatch}" rx="3" fill="{sw_fill}"/>'
        )
    parts.append(
        f'<text x="{sw_x + 5 * (legend_swatch + legend_gap) + 2}" y="{footer_y}" class="ax" fill="{theme.muted}">More</text>'
    )

    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--username", default="khanhduong22")
    parser.add_argument("--out-dir", default="assets")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    days = fetch_contributions(args.username)
    total = sum(d.count for d in days)
    peak = max(days, key=lambda d: d.count)

    for theme in THEMES:
        svg = render_svg(days, theme)
        target = out_dir / f"contributions-{theme.name}.svg"
        target.write_text(svg, encoding="utf-8")

    print(
        f"Generated dark & light SVGs for {args.username}: "
        f"days={len(days)} total={total} peak={peak.count} ({peak.day})"
    )


if __name__ == "__main__":
    main()
