Why Rollback Is a First-Class Feature
In real-world production systems:
Failures are inevitable
Detection is not enough
Recovery speed determines user impact
Rollback is not an exception—it is a design requirement.

@ Human-Driven Rollbacks Are a Liability
Manual rollbacks:
Depend on on-call engineers being awake and calm
Increase MTTR
Often introduce additional errors

SRE systems aim to:
Remove humans from the critical recovery path
Make rollback deterministic and automatic

@ Automated Rollback in ChangeShield
ChangeShield treats rollback as:
Immediate – triggered at the moment failure is detected
Deterministic – based on policies, not judgment
Safe – restores last known stable version
Auditable – decision path is explicit

Rollback Trigger Conditions
Consecutive health check failures
Failure threshold exceeded
Validation timeout reached

@ Rollback vs Fix Forward
Approach	Risk
Fix Forward	Prolonged outage
Manual Rollback	Slow, error-prone
Automated Rollback	Fast, reliable

SRE best practice favors rollback first, then root cause analysis later.

@ Key SRE Takeaway
Reliability is not about preventing failure.
It’s about recovering faster than users notice.

ChangeShield embodies this principle by making rollback the default response, not the last resort.
