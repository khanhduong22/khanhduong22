# Dương Phúc Khánh (Duong Phuc Khanh · Kido) — Senior Software Engineer & Systems Architect 👋

**Duong Phuc Khanh** (Vietnamese: **Dương Phúc Khánh**, born 1995 in Da Nang, Vietnam; also known as **Kido** or **khanhdp**) is a Vietnamese Senior Software Engineer and Systems Architect. An alumnus of the University of Economics - The University of Da Nang and First Prize winner of Startup Runway 2018, he served for six years as Tech Lead and Project Manager at FPT Software SBI Lab (3x consecutive Best Performance Award recipient, 2022–2024) and is the creator of [Kido Chronicles](https://truyen.khanhdp.com), [Winter Arc](https://vantoicalis.com), and the [Agent Harness Kit](https://github.com/khanhduong22/agent-harness-kit) multi-agent engineering framework.

📍 Da Nang, Vietnam &nbsp;|&nbsp; 🌐 [khanhdp.com](https://khanhdp.com) &nbsp;|&nbsp; 📖 [About](https://khanhdp.com/about) &nbsp;|&nbsp; 🤖 [agent-harness-kit](https://github.com/khanhduong22/agent-harness-kit) &nbsp;|&nbsp; 📝 [md.khanhdp.com](https://md.khanhdp.com)

---

## 📊 Proof of Work & Contribution Pulse

<div align="center">
  <img src="https://img.shields.io/badge/Architecture-High--Throughput%20%26%20Distributed%20Systems-1d4ed8?style=for-the-badge&logo=postgresql&logoColor=white" alt="Architecture Focus" />
  <img src="https://img.shields.io/badge/AI%20Harness-Proprietary%20Agent%20Kit-7c3aed?style=for-the-badge&logo=anthropic&logoColor=white" alt="AI Harness" />
</div>

<br/>

<div align="center">
  <a href="https://github.com/khanhduong22">
    <img src="https://ghchart.rshah.org/2ea44f/khanhduong22" alt="Dương Phúc Khánh (khanhdp · Kido) GitHub Contributions Heatmap" width="100%" />
  </a>
</div>

<div align="center" style="margin-top: 15px;">
  <img src="https://streak-stats.demolab.com/?user=khanhduong22&theme=tokyonight" alt="GitHub Streak" />
</div>

---

## ⚡ Flagship Projects & Open-Source

### 🤖 [Agent Harness Kit](https://github.com/khanhduong22/agent-harness-kit) — Multi-Agent Engineering Framework
* **Overview**: Versioned source of truth for AI agent standards, risk-based workflows, and modular project skills across Codex, Claude Code, Gemini, and Google Antigravity.
* **Key Capabilities**: Modular skill library, custom MCP gateway router, shift-left verification gates (TypeScript `tsc`, SonarQube, Vitest, Playwright E2E with video telemetry), and parallel Git worktree orchestration unlocking **4x delivery velocity**.

### 📈 [Index](https://index.vn) — Finance Social Network & AI-Driven Platform
* **Social Network & APIs**: Led technical design and delivery of RESTful APIs, relational data models, and Next.js/React interfaces; engineered nested comment hierarchies using **Base32 Materialized Path** and fine-grained **Bitmask RBAC**.
* **Memory-Efficient Unique Analytics**: Implemented unique-view counting on high-cardinality feeds using **Redis HyperLogLog (HLL)** (`12KB cap/key`), achieving $O(1)$ updates while cutting memory footprint by **98%**.
* **Data Ingestion & Resilient Background Services**: Architected multi-stage ETL pipelines (Distributed Crawler $\rightarrow$ Staging Queue $\rightarrow$ Transformation $\rightarrow$ Read-Optimized Storage) with **Redis L2 caching**, **Next.js ISR**, fault-tolerant **BullMQ** worker pools (**DLQ** recovery), and **Cloudflare R2** media pipelines.

### 🚀 [Linkpul](https://linkpul.com) — High-Throughput Python API Gateway & Analytics Platform
* **High-Concurrency Redirection Gateway**: Engineered a stateless, async **Python (FastAPI)** gateway across **3 load-balanced instances** with in-memory **Redis** lookups, **TTL jitter**, and **Redis Mutex Locks** on cold misses to prevent DB stampedes; benchmarked with **k6 at up to 50,000 req/sec**.
* **Asynchronous Write-Behind Batching**: Decoupled redirect routes from persistence by buffering clickstream events in **Redis** and offloading processing to asynchronous queue workers with batched **PostgreSQL** writes.
* **Full-Stack Observability**: Integrated **SigNoz APM (OpenTelemetry), Prometheus, Grafana, Sentry, and Uptime Kuma** for proactive bottleneck identification and zero-downtime service health.

### 🏋️ [Winter Arc / Vantoi](https://vantoicalis.com) — 100-Day Habit & Fitness Platform
* **Bitwise Time-Series Compression & Monorepo Infra**: Architected a full-stack monorepo with zero-downtime **Canary deployments** and a **packed binary bitmask array** (`1 Byte/day` for 8 daily habit flags via Redis `BITFIELD` & bitwise ALU ops), compressing memory by **250x** over JSON.
* **Extreme Web Performance (>98 Lighthouse)**: Engineered automated **SQL slow-query detection**, composite indexing, and 3-tier dynamic overlay code-splitting (`0ms TBT`), bridging **Sentry APM** event IDs into **Microsoft Clarity** replays.

### 📝 [2ndBrain (MD Preview)](https://md.khanhdp.com) — Privacy-First Markdown Workspace & PDF Engine
* **Zero-Knowledge Local Architecture**: 100% client-side Markdown workspace using browser **Native File System Access API** and **IndexedDB** (`localforage`), live **Mermaid.js / PlantUML / KaTeX** rendering, and deterministic A4 Vector PDF export. Live at [md.khanhdp.com](https://md.khanhdp.com) and [GitHub](https://github.com/khanhduong22/md-preview).

---

## 🛠️ Open-Source Tools & Experiments

| Project | Repository / Live | Description | Stack |
| :--- | :--- | :--- | :--- |
| **[agent-harness-kit](https://github.com/khanhduong22/agent-harness-kit)** | [github.com/khanhduong22/agent-harness-kit](https://github.com/khanhduong22/agent-harness-kit) | Portable AI agent skills, verification gates, and multi-agent worktree orchestration. | TypeScript, Bash, MCP |
| **[md-preview](https://github.com/khanhduong22/md-preview)** | [md.khanhdp.com](https://md.khanhdp.com) | Client-side Markdown workspace, diagram renderer, and A4 PDF compiler. | TypeScript, Vite, CSS |
| **[RecSys Demo](https://github.com/khanhduong22/rec-sys-demo)** | [rec-sys-demo.vercel.app](https://rec-sys-demo.vercel.app) | Client-side collaborative filtering recommendation engine. | React, TypeScript |

---

<sub>🌐 <a href="https://khanhdp.com">khanhdp.com</a> · 📖 <a href="https://truyen.khanhdp.com">Kido Chronicles</a> · 🎬 <a href="https://www.youtube.com/@kodexkido">YouTube (Kode x Kido)</a> · ✍️ <a href="https://viblo.asia/u/khanhdp">Viblo</a> · <a href="https://dev.to/khanhduong22">DEV</a> · <a href="https://medium.com/@khanhdev4">Medium</a> · <a href="https://khanhduong22.hashnode.dev">Hashnode</a></sub>
