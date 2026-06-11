# Duong Phuc Khanh 👋

### Senior Full-Stack Engineer | High-Throughput Systems & Database Optimization
Thanh Khe, Da Nang, Vietnam | phuckhanh22@gmail.com | [LinkedIn](https://www.linkedin.com/in/khanhduong22)

---

## 🚀 Professional Overview

Results-driven **Senior Software Engineer** with **7+ years of professional experience** building high-throughput web applications, robust database architectures, and scalable cloud solutions. Proven expertise in optimizing database performance, designing real-time analytics engines, and leading cross-functional engineering teams.

---

## 🛠️ Core Competencies & Tech Stack

| **Backend & Databases** | **Frontend & Mobile** | **DevOps & Infrastructure** |
| :--- | :--- | :--- |
| • **Languages**: Node.js (NestJS), Python (FastAPI), Java, PHP<br>• **Databases**: TimescaleDB, PostgreSQL, MySQL, OracleDB<br>• **Performance**: Query Tuning, B-Tree/GIN Indexing, Stored Procedures<br>• **Queues/Caching**: Redis (Mutex/L2 Cache), RabbitMQ<br>• **Security**: RBAC, DDL/DML Governance, Data Masking | • **Mobile**: React Native, iOS (Swift), Android<br>• **Frameworks**: Next.js, Vue 3, Nuxt.js<br>• **Architecture**: Feature-Sliced Design (FSD)<br>• **Type Safety**: TypeScript, Codegen APIs<br>• **QA/Testing**: Jest, Vitest, Playwright (UT/IT/E2E)<br>• **Performance**: Core Web Vitals, ISR/PPR, Code-Splitting | • **Cloud**: AWS (Certified Solutions Architect - SAA)<br>• **AI**: Claude Certified Architect – Foundations<br>• **DevOps/IaC**: Docker, Terraform, Ansible<br>• **CI/CD**: GitHub Actions, SonarQube<br>• **Observability**: Prometheus, Grafana, SigNoz APM<br>• **Search**: Meilisearch, Qdrant |

---

## ⚡ Flagship Projects

### 🚀 [Linkpul](https://linkpul.com) — High-Throughput Short-Link Platform
* **Overview**: A high-concurrency URL redirection and real-time analytics platform.
* **Architecture**: Engineered a FastAPI gateway with distributed Redis Mutex Locks to prevent race conditions and rate-limit clients. Optimized PostgreSQL to store 100M+ analytics records via async Celery write-batching.
* **Observability & QA**: Set up SigNoz (OpenTelemetry) APM, Prometheus/Grafana, and K6 stress-tested endpoints to handle 50k+ req/sec.

### 📈 [Index](https://index.vn) — Real-Time News & Fintech Platform
* **Overview**: A real-time fintech analytics platform with low-latency data rendering.
* **ETL Pipeline**: Designed a 4-step ETL pipe (Scraper -> Staging Buffer -> TimescaleDB Hypertables with Continuous Aggregates -> Read-Only API Replica via postgres_fdw).
* **Performance**: Implemented a 3-layer caching strategy (React Query -> Next.js ISR -> Redis L2) reducing db load and cutting latency to <5ms. Refactored frontend to Feature-Sliced Design (FSD), reducing bundle size by 8%.

### 🎯 [Danang Chill Finder](https://github.com/khanhduong22/danang-chill-finder) — AI Spatial Cafe Recommender
* **Overview**: AI-powered recommendation system for cafes in Da Nang.
* **Tech**: Built with Next.js 16, Supabase, pgvector, and TailwindCSS. Employs vector similarity search for natural language cafe recommendations.

### 🧠 [RecSys Demo](https://github.com/khanhduong22/rec-sys-demo) — Real-Time Collaborative Filtering Engine
* **Overview**: Client-side collaborative filtering and browser fingerprinting demo.
* **Tech**: Next.js, TypeScript, browser fingerprinting, and interactive similarity matrix rendering.

### 📝 [MD Preview](https://github.com/khanhduong22/md-preview) — Markdown Assistant & PDF Exporter
* **Overview**: Clean, GitHub-style Markdown live editor with custom PDF export and guided tours. Live at [md.khanhdp.com](https://md.khanhdp.com).

---

## 📊 GitHub Metrics

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=khanhduong22&show_icons=true&theme=tokyonight&count_private=true" alt="GitHub Stats" height="180"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=khanhduong22&layout=compact&theme=tokyonight" alt="Top Languages" height="180"/>
</div>

<div align="center" style="margin-top: 10px;">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=khanhduong22&theme=tokyonight" alt="GitHub Streak" height="80"/>
</div>

---

## 🏆 Awards & Certifications

* **First Prize** — Startup Runway 2018 (Founder of JustOrder mobile application)
* **First Prize** — Regional Computer Science & Mathematics Competitions
* **AWS Certified** Solutions Architect – Associate (SAA)
* **Claude Certified** Architect – Foundations
* **PMP** — Project Management Professional (FPT PM track)
