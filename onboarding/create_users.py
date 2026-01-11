import csv
import random
import string
import datetime

# 1. Setup: Define where your input data comes from
INPUT_FILE = 'new_hires.csv'
LOG_FILE = 'onboarding_log.txt'

def generate_password(length=12):
    """Generates a random secure password."""
    chars = string.ascii_letters + string.digits + "!@#$%"
    return ''.join(random.choice(chars) for _ in range(length))

def create_username(first_name, last_name):
    """Formats username as first initial + last name (lowercase)."""
    return f"{first_name[0].lower()}{last_name.lower()}"

def process_new_hires():
    print(f"--- Starting Onboarding Process: {datetime.datetime.now()} ---")
    
    # 2. Input: Read the CSV file
    try:
        with open(INPUT_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            
            # 3. Process: Loop through each employee
            for row in reader:
                f_name = row['FirstName'].strip()
                l_name = row['LastName'].strip()
                dept = row['Department'].strip()
                
                # Generate details
                username = create_username(f_name, l_name)
                temp_password = generate_password()
                
                log_entry = f"CREATED: User {username} for {f_name} {l_name} in {dept}. Password: {temp_password}"
                print(log_entry)
                
                with open(LOG_FILE, "a") as log:
                    log.write(log_entry + "\n")
                    
    except FileNotFoundError:
        print("Error: 'new_hires.csv' not found. Please create the file first.")

if __name__ == "__main__":
    process_new_hires()