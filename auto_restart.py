import time
import os

# Define the name of the main script
MAIN_SCRIPT = 'main.py'

def run_script():
    while True:
        print("Starting main.py...")
        os.system(f'python {MAIN_SCRIPT}')  # Use os.system to run the script
        print("main.py has finished. Restarting in 2 minutes...")
        time.sleep(120)  # Sleep for 2 minutes (120 seconds)

if name == "main":  # Use the correct condition
    run_script()
