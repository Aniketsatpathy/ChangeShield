import time
from controller.validator import check_health
from controller.policy_engine import load_policy
from controller.rollback import rollback

def apply_change(service_url):
    policy = load_policy()
    failures = 0

    for _ in range(policy["canary"]["max_checks"]):
        healthy = check_health(service_url)
        if not healthy:
            failures += 1
        if failures >= policy["canary"]["failure_threshold"]:
            rollback()
            return False
        time.sleep(policy["canary"]["check_interval_seconds"])

    return True