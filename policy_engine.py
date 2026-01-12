import yaml

def load_policy():
    with open("policies/rollout_policy.yml") as f:
        return yaml.safe_load(f)