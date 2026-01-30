# 🤖 Agentic MLOps: Self-Healing Infrastructure Agent

An autonomous DevOps agent built to monitor, diagnose, and repair containerized applications. This project demonstrates **Agentic Operations**—using code to perform "Reason + Act" (ReAct) loops to maintain system uptime without human intervention.


## 🌟 The Problem & Solution
* **Problem:** Manual debugging of container configuration errors (like missing secrets) increases **MTTR** (Mean Time To Recovery) and requires 24/7 human monitoring.
* **Solution:** A "Doctor Agent" that utilizes the Docker SDK to perform real-time log analysis and autonomous remediation.

## 🛠️ Tech Stack
* **Backend:** FastAPI, Uvicorn (The "Patient" App)
* **Containerization:** Docker & Docker Compose
* **Automation:** Python Docker SDK (The "Doctor" Agent)
* **Environment:** Windows PowerShell / CMD

## 🏗️ Project Structure
```text
self-healing-mcp-agent/
├── patient-app/           # The FastAPI application (The Patient)
│   ├── app.py             # Logic with intentional failure points
│   └── Dockerfile         # Container definition
├── doctor-agent/          # The Autonomous Agent (The Doctor)
│   └── agent.py           # The "Reason + Act" healing logic
└── docker-compose.yml     # Infrastructure orchestration
```

🚀 Step-by-Step Execution Guide
1. Build and Deploy the "Patient"
From the root directory, build and launch the application. We intentionally "forget" the DB_SECRET to trigger a failure.
PowerShell
docker compose up --build -d

2. Trigger the Failure (The "Try" Phase)
Access the health endpoint to generate a 500 error in the logs.
PowerShell
Invoke-RestMethod -Uri "http://localhost:8000/health"

3. Run the Autonomous "Doctor" (The "Heal" Phase)
In a new terminal window, start the agent. It will detect the error and fix the container.
PowerShell
python doctor-agent/agent.py

4. Verify the Recovery
Once the agent reports SUCCESS, verify the app is healthy.
PowerShell
Invoke-RestMethod -Uri "http://localhost:8000/health"
Expected Output: {"status":"running","message":"Connected with TylerTexas_Verified_2026"}

## 🎓 Skills Acquired & Demonstrated
* **Agentic Operations:** Implementation of "Reason + Act" (ReAct) patterns for autonomous system management.
* **Observability & Logging:** Configuring Python applications to emit actionable telemetry for automated monitors.
* **Infrastructure as Code (IaC):** Managing container lifecycles and environment configurations via Docker Compose.
* **Automated Remediation:** Reducing MTTR (Mean Time To Recovery) through programmatic infrastructure state changes.
* **Troubleshooting:** Identifying and resolving logging bottlenecks (buffering) in containerized Windows environments.
