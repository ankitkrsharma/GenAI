# 🤖 AI-Powered Project Risk Management System

## 🧠 Overview
This system helps IT organizations identify, assess, and mitigate project risks in real-time using AI agents powered by Gemini and CrewAI.

It continuously monitors:
- 📈 **External factors**: market trends, transaction histories, economic indicators
- 🏗️ **Internal metrics**: project status, schedule delays, payment issues, team availability

It then generates:
- 🧾 Risk reports
- 🛡️ Mitigation strategies
- 📢 Alerts for decision-makers

A conversational chatbot interface allows project managers and leadership to query real-time risk status for one or more projects.

---

## 🎯 Key Features

- ✅ Multi-agent architecture using **CrewAI**
- 🧠 Integration with **Google Gemini** via Langchain
- 🧾 Auto-generated reports and mitigation plans
- 💬 Conversational chatbot to interact with the system
- 📊 Real-time internal & external data analysis
- 🗃️ MySQL-backed project tracking
- 🌐 UI via **Streamlit** or optional React frontend

---

## 🧩 Agents & Roles

| Agent                      | Responsibility                                              |
|---------------------------|--------------------------------------------------------------|
| Project Risk Manager       | Orchestrates all other agents and owns final analysis       |
| Market Analysis Agent      | Analyzes external financial trends and economic data        |
| Risk Scoring Agent         | Scores financial/project risks based on defined criteria    |
| Project Status Tracking Agent | Tracks internal delays, resource issues, and project health |
| Reporting Agent            | Compiles results into human-readable reports and alerts     |

---

## 🧰 Technologies Used

- **Python**, **Streamlit** / **React**
- **CrewAI** for agent workflow
- **Google Gemini** via Langchain
- **MySQL** for project tracking
- **Pinecone/ChromaDB** (optional vector DB)
- **dotenv**, **SQLAlchemy**, **Loguru**, **Pydantic**

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/ai-risk-management-system.git
cd ai-risk-management-system
