from controller.change_manager import apply_change

SERVICE_URL = "http://localhost:8080"

if __name__ == "__main__":
    print("Starting ChangeShield rollout...")
    result = apply_change(SERVICE_URL)

    if result:
        print("✅ Change promoted successfully")
    else:
        print("❌ Change failed and was rolled back")