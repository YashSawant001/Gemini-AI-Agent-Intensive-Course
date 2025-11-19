# Gemini AI Agents Portfolio: Capstone Project

This repository serves as a portfolio of projects completed during the 5-Day AI Agents Intensive Course. The primary focus is the **Concierge Capstone Project**, demonstrating core ADK skills.

### 🔧 Project Setup and Prerequisites

To run these projects locally, ensure you have Python 3.9+ installed and configure your environment:

1.  **Clone the Repository:** `git clone YOUR_REPOSITORY_URL`
2.  **Install Dependencies:**
    `pip install google-adk`
3.  **Set API Key:** Configure your Gemini API Key as a secure environment variable (`GEMINI_API_KEY`).

---

## Capstone Project: Concierge Itinerary Agent 🏆

**Track:** Concierge Agents (Automating personalized planning).

**Goal:** Built, deployed, and submitted a multi-agent system that demonstrates the three core course concepts, serving as the final project submission.

### Key Concepts Demonstrated:
1.  **Multi-Agent Orchestration (Sequential Flow):** Uses a `SequentialAgent` to manage a structured workflow (Context Injection → Planning → Validation).
2.  **Tool Use (Time and Feasibility Checks):** Agents use custom tools (`current_time_checker`, `location_feasibility_check`) to access real-time data and verify schedule feasibility.
3.  **Context Engineering (Profile Injection):** A dedicated agent injects explicit `User Constraints` as the initial context, simulating the RAG pattern to ensure personalized outputs.

**Code:** [capstone_project/capstone_concierge_agent.py](capstone_project/capstone_concierge_agent.py)

---
