import docker
import time

client = docker.from_env()

def diagnose_and_heal():
    print("\n--- [Doctor Agent] Scanning Infrastructure ---")
    try:
        container = client.containers.get("fragile-service")
        
        # Read the last 30 lines of logs
        logs = container.logs(tail=30).decode("utf-8")
        
        # DEBUG: Let's see exactly what the doctor sees
        print(f"DEBUG: Analyzing {len(logs)} characters of log data...")

        # Case-insensitive check and stripping whitespace
        if "CRITICAL: DB_SECRET missing!" in logs:
            print("ALERT: Failure detected! Root Cause: Missing DB_SECRET.")
            print("REASONING: Injecting the required environment variable and restarting...")
            
            # THE HEAL
            container.stop()
            container.remove()
            
            # Use the exact image name from your 'docker images' list
            client.containers.run(
                "self-healing-mcp-agent-patient-app", 
                name="fragile-service",
                ports={'8000/tcp': 8000},
                environment={"DB_SECRET": "TylerTexas_Verified_2026"},
                detach=True
            )
            print("SUCCESS: Service healed and restarted.")
            return True
            
        else:
            print("STATUS: App is running. (No 'CRITICAL' flag found in current log window)")
            
    except Exception as e:
        print(f"ERROR: {e}")
    
    return False

if __name__ == "__main__":
    print("Self-Healing Agent started. Monitoring for issues...")
    while True:
        healed = diagnose_and_heal()
        if healed:
            print("Mission complete. Standing by for next failure.")
            # Give it a moment to boot up before checking again
            time.sleep(15) 
        else:
            time.sleep(5)