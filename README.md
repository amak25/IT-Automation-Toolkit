# IT Automation Toolkit

A collection of Python and Shell scripts designed to automate repetitive system administration tasks, streamline user management, and improve operational efficiency.

## Project Overview
This repository serves as a centralized toolkit for IT operations. The goal is to reduce manual error and save time on daily help desk and admin workflows.

**Current Modules:**
* User Onboarding: Automates the generation of user credentials and system logging from raw HR data.
* Log Analysis: Parsers for server logs to identify critical errors.
* Backup Utilities: Automated file compression and archival scripts.

---

## Module 1: New Hire Onboarding
Located in: `/onboarding`

This script simulates the account creation process for new employees. It processes a CSV file of new hires, generates standardized usernames and secure temporary passwords, and produces an audit log of the actions taken.

### Key Features
* Standardization: Enforces specific username conventions (First Initial + Last Name).
* Security: Generates random, high-entropy temporary passwords.
* Auditing: Writes all actions to `onboarding_log.txt` for accountability.
* Error Handling: Accounts for errors and handles missing input files or bad data formats.

### How to Run
1.  Clone the repository:**
    ```bash
    git clone [https://github.com/amak25/IT-Automation-Toolkit.git](https://github.com/amak25/IT-Automation-Toolkit.git)
    cd IT-Automation-Toolkit/onboarding
    ```

2.  Prepare the Input:
    Ensure a file named `new_hires.csv` exists in the folder with the following headers:
    `FirstName,LastName,Department`

3.  Execute the Script:
    ```bash
    python create_users.py
    ```

4.  View Results:
    Check the console for immediate feedback.
    Open `onboarding_log.txt` to see the permanent record of created users.

---

## Module 2: System Maintenance
Located in: `/maintenance`

This module manages data integrity and storage optimization through an automated rotational backup system.

### Key Features
* Automated Compression: Uses `shutil` to archive target directories into portable ZIP formats.
* Retention Policy Enforcement: Automatically scans and deletes backups older than X days to prevent storage overflow.
* Zero-Config Setup: Automatically generates target directories if they do not exist.

### How to Run
1.  Navigate to the maintenance directory:
    ```bash
    cd maintenance
    ```
2.  Run the manager:
    ```bash
    python backup_manager.py
    ```
3.  Configuration: Edit the `SOURCE_FOLDER` and `RETENTION_DAYS` variables at the top of the script to customize behavior.

---

## Module 3: Server Health Monitoring
Located in: `/monitoring`

This tool parses raw server logs to extract critical incidents, filtering out noise (standard INFO logs) to highlight actionable issues.

### Key Features
* Pattern Matching: Scans specifically for "ERROR", "CRITICAL", and "WARNING" keywords.
* Automated Reporting: Compiles a summary of all critical failures into a clean text file for review.
* Non-Destructive: Reads the logs without modifying the source data.

### How to Run
1.  Navigate to the monitoring directory:
    ```bash
    cd monitoring
    ```
2.  Run the monitor:
    ```bash
    python log_monitor.py
    ```
3.  **Review:** Check `error_report.txt` for the summary of critical events.

## Technologies Used
* Python 3.14.0
* Libraries: `csv`, `random`, `string`, `datetime`

--
Created by [amak25] - 1/2026
