# ChangeShield – Production Change Safety Controller

ChangeShield is an SRE-focused change management system that enforces safe production changes using automated validation and rollback, reducing outages caused by human error.

This project demonstrates how SREs prevent incidents at the moment of change, rather than detecting them after users are impacted.

@ Why Change Safety Matters
Industry data and real-world experience show that:
Most production outages are caused by unsafe deployments or configuration changes
Manual rollbacks increase Mean Time To Recovery (MTTR)
Human judgment under pressure is unreliable
ChangeShield automates reliability guardrails so that unsafe changes never fully reach production.

Engineer / CI Pipeline
        |
        |  (proposes a change)
        v
+------------------------+
|   ChangeShield Core    |
|------------------------|
| - Policy Engine        |
| - Health Validator     |
| - Rollback Controller  |
+------------------------+
        |
        |  SAFE → Promote
        |  FAIL → Rollback
        v
Target Service (App v1 / v2)

Key Architectural Principles
Automation over human judgment
Rollback-first design
Deterministic decision-making
Fail fast, recover faster

@ Failure Flow (Critical SRE Section)

Normal Flow (Successful Change)
New version is deployed
Health checks are executed periodically
All checks pass within policy limits
Change is promoted
Failure Flow (Rollback Scenario)
New version is deployed
Health checks fail repeatedly
Failure threshold is exceeded
Automatic rollback is triggered
System returns to last known stable version

Deploy v2
   ↓
Health Check X X X X X
   ↓
Failure Threshold Reached
   ↓
Rollback to v1
   ↓
System Stability Restored


@ Tech Stack
| Layer          | Technology     | Purpose                      |
| -------------- | -------------- | ---------------------------- |
| Controller     | Python         | Change orchestration logic   |
| Target Service | Flask          | Simulated production service |
| Policies       | YAML           | Reliability guardrails       |
| Automation     | Docker, Bash   | Reproducible execution       |
| CI/CD          | GitHub Actions | Automated change execution   |


@ How to Run Locally
docker-compose up --build

Expected behavior:
App v2 will intermittently fail health checks
ChangeShield will detect failures
Rollback to v1 happens automatically


@ What This Project Demonstrates
SRE change management principles
Automated rollback systems
Failure-first design
Production safety engineering
Reducing MTTR through automation
