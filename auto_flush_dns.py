import os
import subprocess
import time

def flush_dns():
    try:
        print("Flushing DNS cache...")
        # Running the ipconfig /flushdns command
        result = subprocess.run(['ipconfig', '/flushdns'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("DNS cache flushed successfully!")
        else:
            print(f"Error flushing DNS cache: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

def run_periodically(interval_minutes=5):
    while True:
        flush_dns()
        print(f"Waiting for {interval_minutes} minutes before flushing again...")
        # Sleep for the specified interval in seconds (5 minutes = 300 seconds)
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    run_periodically(interval_minutes=5)