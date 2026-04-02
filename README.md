# OmniAgent (MAA) | The Swarm Intelligence Factory 🚀

[![Powered by Ollama](https://img.shields.io/badge/Inference-Ollama-blue)](https://ollama.com/)
[![Graph Database](https://img.shields.io/badge/Memory-Neo4j-green)](https://neo4j.com/)
[![Framework](https://img.shields.io/badge/Backend-FastAPI-009688)](https://fastapi.tiangolo.com/)
[![Model](https://img.shields.io/badge/Brain-Qwen%202.5-purple)](https://github.com/QwenLM/Qwen2.5)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**OmniAgent (MAA)** is a high-performance, open-source multi-agent orchestration platform. By utilizing the **MiroFish-Offline** framework and **GraphRAG** (via Neo4j), OmniAgent spawns specialized swarms that interact autonomously to solve high-stakes problems in a 100% local, private environment.

---

## 🧠 The Core Philosophy: "Plan, Simulate, Observe"

OmniAgent introduces a **Circular Intelligence Loop** designed to move beyond simple chat responses:

1.  **Plan (The Seed):** Users input a high-level goal. The system identifies 10-100 specialized personas required to map the scenario.
2.  **Simulate (The Swarm):** Agents are spawned as nodes in a **Neo4j Knowledge Graph**. They argue, collaborate, and compete based on domain-specific blueprints.
3.  **Observe (The Answer):** A dedicated **ReportAgent** monitors emergent patterns in the graph and provides a data-backed simulation report.

---

## 🏗️ Architectural Overview

Built for **Local Sovereignty**. No data leaves your machine; no API costs are incurred. Designed to run smoothly on 16GB RAM hardware.

```mermaid
graph TD
    User((User)) -->|Input Goal| UI[Next.js War Room]
    UI -->|WebSocket| API[FastAPI Gateway]
    
    subgraph Local_Mainframe [ThinkPad / HP Edge]
        API -->|Orchestration| MF[MiroFish-Offline Engine]
        MF -->|Memory| Graph[(Neo4j Knowledge Graph)]
        MF -->|Inference| Ollama[Ollama Server]
        Ollama -->|Brain| Qwen[Qwen 2.5 / Llama 3]
    end
    
    subgraph Context_Vault [The Brain]
        BP[.md Blueprints] --> MF
    end
    
    MF -->|Pattern Extraction| Observer[ReportAgent]
    Observer -->|Simulation Report| UI

## 👥 The Founding Team

| Name | Role | Focus |
| :--- | :--- | :--- |
| **Mayank** (@Mayank908) | **Lead Architect** | System Orchestration, Engine Performance, & Backend Ops. |
| **Reda Ansari** | **Context Engineer** | Swarm Personas, Knowledge Graph Logic, & Blueprint Design. |
| **Jahanvi Malela** | **UX Visionary** | Real-time Visualization, Interaction Design, & War Room UI. |

---

## 📂 Repository Structure

```text
omniagent-maa/
├── backend/                # FastAPI Gateway & Swarm Logic
│   ├── app/core            # MiroFish Integration & Graph Handlers
│   └── app/api             # WebSocket & REST Endpoints
├── context_vault/          # Markdown Domain Blueprints (The "Brain")
├── frontend/               # Next.js 14 War Room Dashboard
└── docker-compose.yml      # Local Mainframe Environment


---

## 🤝 For Contributors

We are building a **Universal Simulation Engine**. Whether you are an AI Researcher, a Backend Dev, or a Domain Expert, we want your help!

### How to Contribute:
1.  **Star the Repo:** Help us reach more builders! ⭐
2.  **Submit a Blueprint:** Add a new `.md` file to `context_vault/blueprints/` to teach the swarm a new industry (e.g., Real Estate, Space Ops).
3.  **Optimize:** Help us refine the MiroFish-Offline logic for low-resource environments.

---

## 🚀 Quick Start (Day 1)

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Mayank908/omniagent-maa.git
    ```
2.  **Initialize the Mainframe:**
    ```bash
    docker-compose up -d
    ```
3.  **Pull the Brain:**
    ```bash
    ollama pull qwen2.5:14b
    ```
4.  **Launch:**
    ```bash
    cd backend && uvicorn main:app --reload
    ```

---

*Built with zero budget and infinite grit. Project MAA is an open-source initiative under the MIT License.*
