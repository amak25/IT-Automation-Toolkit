import re
import datetime

# --- CONFIGURATION ---
INPUT_LOG = 'server.log'
OUTPUT_REPORT = 'error_report.txt'

def parse_logs():
    print(f"Scanning {INPUT_LOG} for errors...")
    
    error_count = 0
    warning_count = 0
    critical_events = []

    try:
        with open(INPUT_LOG, 'r') as file:
            for line in file:
                # 1. Use Regex or string matching to find issues
                # We are looking for lines containing "ERROR" or "CRITICAL"
                if "ERROR" in line or "CRITICAL" in line:
                    error_count += 1
                    critical_events.append(line.strip())
                elif "WARNING" in line:
                    warning_count += 1
        
        # 2. Generate a summary report
        generate_report(error_count, warning_count, critical_events)
        
    except FileNotFoundError:
        print(f"Error: Could not find {INPUT_LOG}. Please create it first.")

def generate_report(errors, warnings, events):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    print(f"\n--- SCAN COMPLETE ---")
    print(f"Errors Found: {errors}")
    print(f"Warnings Found: {warnings}")
    
    if errors > 0:
        with open(OUTPUT_REPORT, 'w') as report:
            report.write(f"SERVER HEALTH REPORT - {timestamp}\n")
            report.write("=======================================\n")
            report.write(f"Total Errors: {errors}\n")
            report.write(f"Total Warnings: {warnings}\n\n")
            report.write("CRITICAL EVENTS LOG:\n")
            report.write("--------------------\n")
            for event in events:
                report.write(f"{event}\n")
        print(f"Report generated: {OUTPUT_REPORT}")
    else:
        print("System Healthy. No critical events found.")

if __name__ == "__main__":
    parse_logs()
    