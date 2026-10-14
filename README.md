# Duong Phuc Khanh (Kido) 👋

> **Architecting High-Throughput Distributed Systems & AI-Augmented Engineering Platforms.**
📍 Da Nang, Vietnam &nbsp;|&nbsp; 🌐 [khanhdp.com](https://khanhdp.com) &nbsp;|&nbsp; 🏛️ [Biography / Wiki](https://khanhdp.com/about) &nbsp;|&nbsp; 📖 [truyen.khanhdp.com](https://truyen.khanhdp.com) &nbsp;|&nbsp; 🆔 [Wikidata Q141718572](https://www.wikidata.org/wiki/Q141718572)

---

## 📊 Proof of Work & Contribution Pulse

<div align="center">
  <img src="https://img.shields.io/badge/Architecture-High--Throughput%20%26%20Distributed%20Systems-1d4ed8?style=for-the-badge&logo=postgresql&logoColor=white" alt="Architecture Focus" />
  <img src="https://img.shields.io/badge/AI%20Harness-Proprietary%20Agent%20Kit-7c3aed?style=for-the-badge&logo=anthropic&logoColor=white" alt="AI Harness" />
</div>

<br/>

<div align="center">
  <a href="https://github.com/khanhduong22">
    <img src="https://ghchart.rshah.org/2ea44f/khanhduong22" alt="Khanh Duong's GitHub Contributions Heatmap" width="100%" />
  </a>
</div>

<div align="center" style="margin-top: 15px;">
  <img src="https://streak-stats.demolab.com/?user=khanhduong22&theme=tokyonight" alt="GitHub Streak" />
</div>

---

## 🚀 Professional Overview

Results-driven **Software Architect & Systems Engineer** with **7+ years of professional experience** architecting high-throughput distributed systems and leading engineering teams. Creator of **`agent-harness-kit`** and custom **Model Context Protocol (MCP)** servers, pioneering agentic engineering workflows that unlock **4x full-stack delivery velocity** while maintaining strict architectural consistency through 7 automated verification gates. Proven track record in financial social networks, high-concurrency gateways (50k+ req/s), complex database optimization, and cross-functional leadership. Specialized in domain-driven microservices, resilient distributed architectures, and mentoring high-velocity engineering teams for business impact.

---

## 🛠️ Core Competencies & Tech Stack

| **AI & AGENTIC** | **BACKEND & DB** | **FRONTEND & MOBILE** | **DEVOPS, CLOUD & APM** |
| :--- | :--- | :--- | :--- |
| • **Daily Tooling**: Claude Code, Cursor, Antigravity, OpenAI Codex<br>• **Custom MCP**: Built custom DB & Memory MCP servers & gateway router<br>• **Context Architecture**: Hierarchical memory, token budgeting, project rules<br>• **Multi-Agent Harness**: Proprietary `agent-harness-kit` (70+ skills, worktrees, TDD) | • **Languages**: Node.js (NestJS, Hono), Python (FastAPI), Bun, TypeScript, Java<br>• **Databases & Cache**: PostgreSQL (pgBackRest), Redis, Valkey, TimescaleDB, ClickHouse<br>• **Queues & Realtime**: BullMQ, RabbitMQ, WebSockets, SSE<br>• **Architecture & Scale**: DDD, Event-Driven, Distributed Locks, Bitmask RBAC, SHA-256 Audit | • **Web & Mobile**: Next.js, React (Vite), Mobile PWA (Service Workers), Vue, React Native<br>• **Architecture**: Monorepos (Turborepo, pnpm), Micro-Frontends, FSD<br>• **Performance**: Core Web Vitals, Zero-Scroll Mobile Viewports (390/430px)<br>• **State & Types**: React Query, Redux Toolkit, Pinia, TypeScript | • **Cloud & Infrastructure**: AWS (Certified SAA), Cloudflare, Linux/Bash<br>• **Containers & CI/CD**: Docker, Docker Compose, GitHub Actions, Zero-Downtime Deploy<br>• **APM & Monitoring**: SigNoz (OpenTelemetry), Prometheus, Grafana, Sentry, Uptime Kuma<br>• **7 Quality Gates**: Knip, SonarQube, Biome/ESLint, Vitest, Playwright E2E Video Telemetry |

---

## ⚡ Flagship Projects

### 📈 [Index](https://index.vn) — Finance Social Network Platform
* **Social Network Core Architecture**: Built the Community & Social Network engine from scratch in NestJS; designed modular architectures for high-velocity feeds, dynamic groups, nested comment trees using **Base32 Materialized Path**, and high-performance **Bitmask RBAC** for fine-grained permissions.
* **High-Performance Analytics**: Implemented real-time post view counting and user engagement metrics using **Redis HyperLogLog (HLL)**, achieving $O(1)$ sub-millisecond updates while cutting memory footprint by **98%**.
* **Data Pipeline & Media Engine**: Engineered multi-stage data ingestion (Distributed Crawler $\rightarrow$ Staging Queue $\rightarrow$ Transformation ETL $\rightarrow$ Read-Optimized Storage) with 3-layer caching (<5ms latency), alongside an asynchronous video transcoding service using Cloudflare R2 and background workers.
* **Agentic Delivery (4x Multiplier)**: Orchestrated parallel autonomous sub-agents across split Git worktrees via `agent-harness-kit`, boosting delivery speed by 400% with zero architectural regression.

### 🚀 [Linkpul](https://linkpul.com) — High-Throughput Short-Link & Analytics Platform
* **High-Concurrency Redirection Gateway**: Engineered high-throughput FastAPI gateway using Redis Mutex Locks to eliminate race conditions, sustaining sub-millisecond redirection p99 under stress tests up to **50,000 req/sec**.
* **Asynchronous Counter Batching & Analytics**: Decoupled the sub-millisecond redirect path from persistence by buffering clickstream events in **Redis** and offloading ingestion to asynchronous queue workers; batched statistical aggregations into PostgreSQL with zero write contention on hot redirect routes.
* **Full-Stack Observability**: Deployed multi-layered monitoring integrating **SigNoz APM, Sentry, Prometheus, Grafana, Uptime Kuma, and Dozzle**, establishing instant anomaly detection and zero-downtime health alerts.

### 🏋️ [Winter Arc Platform](https://vantoicalis.com) — Gamified Athlete Habit Tracking & Mobile PWA
* **Mobile-First PWA & Micro-UX**: Engineered a high-performance Next.js 14 PWA tailored for calisthenics athletes; enforced strict zero-scroll viewport constraints (`390x844` standard & `430x932` mobile baselines) with dual-theme Cyber Dark/Light transitions and offline service worker synchronization. Live at [vantoicalis.com](https://vantoicalis.com) and [vantoi.khanhdp.com](https://vantoi.khanhdp.com).
* **Backend Architecture & High-Speed Cache**: Architected NestJS core using modular repository patterns, dedicated DTO mappers, and **Valkey 8 / Redis** in-memory caching for sub-millisecond streak computations and real-time leaderboards.
* **9:16 Social Story Engine**: Built dynamic Instagram/Facebook story card generation with real-time streak telemetry, activity heatmaps, and badge achievements.
* **Autonomous Quality Gate**: Pioneered automated Playwright mobile E2E pipeline with in-video banner telemetry, automated Google Drive archiving, and Slack incident webhooks.

### ⏱️ [LimArt](https://limart.khanhdp.com) — Monorepo Enterprise Attendance & Retail ERP
* **3-Tier Monorepo Architecture**: Designed a decoupled architecture featuring **Hono API** (Bun/Node runtime for ultra-low latency), Vite Admin SPA, and Vite Staff PWA sharing core schema packages via pnpm workspace. Live at [limart.khanhdp.com](https://limart.khanhdp.com).
* **Cryptographic Audit Trail**: Implemented `@checkin/audit-trail` with SHA-256 tamper-evident hash chaining, ensuring immutable logs for employee attendance, shift changes, and payroll integrity.
* **Enterprise Disaster Recovery & Search**: Configured PostgreSQL 17 with continuous WAL streaming and Point-in-Time Recovery (PITR) via **pgBackRest**, paired with **Meilisearch** for sub-50ms Vietnamese fuzzy text search.

### 🎨 [Tikat Studio](https://story.tikat.vn) — AI Creative Suite & FB Story Automation
* **Automated ImageFX Integration**: Reverse-engineered Google Gemini ImageFX session persistence (`__Secure-1PSID` auto-refresh sidecar), bypassing headless browser overhead to deliver automated, high-fidelity Facebook Story generation via FastAPI. Live at [story.tikat.vn](https://story.tikat.vn).
* **End-to-End Content Pipeline**: Integrated prompt engineering templates, localized category taxonomies, and cloud image delivery for high-velocity social media publishing.

### 📝 [2ndBrain (MD Preview)](https://md.khanhdp.com) — Privacy-First Markdown Workspace & Knowledge Engine
* **Zero-Knowledge Local Architecture**: Engineered a 100% client-side Markdown workspace using browser **Native File System Access API** and **IndexedDB** (`localforage`), enabling offline directory vault sync with zero cloud tracking. Live at [md.khanhdp.com](https://md.khanhdp.com) and [GitHub](https://github.com/khanhduong22/md-preview).
* **Advanced Diagramming & Math**: Integrated live parsers for **Mermaid.js**, **PlantUML**, **Draw.io**, and **LaTeX (MathJax)** alongside instant client-side full-text search (`minisearch`), Chrome-style color-coded tab grouping, and visual diff version history.
* **Multi-Format Distribution**: Distributed as a responsive Web PWA, an installable **Chrome Extension (Manifest V3 Side Panel)**, and a self-contained single-file HTML exporter with paginated PDF rendering.

### 🤖 [Agent Harness Kit](https://github.com/khanhduong22/agent-harness-kit) — Multi-Agent Engineering Framework
* **Overview**: One versioned source of truth for company-wide AI agent standards, risk-based workflows, and modular project packs across Codex, Claude Code, Gemini, and Google Antigravity.
* **Key Capabilities**: 70+ modular skills, custom MCP gateway router, 7 mandatory verification gates (AST linter, typecheck, SonarQube, Vitest, Playwright E2E with video recording), and parallel worktree orchestrator.

---

## 🛠️ Open-Source Tools & Experiments

| Project | Live / Demo | Description | Stack |
| :--- | :--- | :--- | :--- |
| **[RecSys Demo](https://github.com/khanhduong22/rec-sys-demo)** | [rec-sys-demo.vercel.app](https://rec-sys-demo.vercel.app) | Client-side collaborative filtering recommendation engine with browser fingerprinting. | React, TypeScript, Vector Math |

---

## 🏆 Certifications & Awards

* **Claude Certified Architect – Foundations** (Anthropic Academy)
* **AWS Certified Solutions Architect – Associate (SAA)**
* **Project Management Professional (PMP)** — FPT PM Track
* **First Prize** — [Startup Runway 2018](https://baodanang.vn/chuyen-trang-kyniem/201806/ung-dung-dat-mon-va-thanh-toan-nhanh-2905529/) at [Da Nang University of Economics (DUE)](https://vi.wikipedia.org/wiki/Tr%C6%B0%E1%BB%9Dng_%C4%90%E1%BA%A1i_h%E1%BB%8Dc_Kinh_t%E1%BA%BF,_%C4%90%E1%BA%A1i_h%E1%BB%8Dc_%C4%90%C3%A0_N%E1%BA%B5ng) (Founder of JustOrder mobile application, featured on [Báo Đà Nẵng](https://baodanang.vn/goi-mon-an-bang-dien-thoai-thong-minh-3174905.html))
* **First Prize** — City Computer Science Award (Regional competitions in Mathematics, Computer Science)
