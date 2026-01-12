def rollback():
    with open("state/current_version.txt", "w") as f:
        f.write("v1")
    print("🚨 Rollback executed to v1")