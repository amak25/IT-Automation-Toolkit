import shutil
import os
import datetime

# --- CONFIGURATION ---
SOURCE_FOLDER = './work_documents'  # The folder we want to save
BACKUP_FOLDER = './backups'         # Where the zips go
RETENTION_DAYS = 5                  

def create_backup():
    """Compresses the source folder into a timestamped zip file."""
    # Ensure backup folder exists
    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)

    # Generate a timestamped filename (e.g., backup_2025-10-24)
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    backup_filename = f"backup_{timestamp}"
    
    # Create the zip file
    # shutil.make_archive(base_name, format, root_dir)
    shutil.make_archive(os.path.join(BACKUP_FOLDER, backup_filename), 'zip', SOURCE_FOLDER)
    print(f"Backup created: {backup_filename}.zip")

def prune_old_backups():
    """Deletes backups older than RETENTION_DAYS."""
    print(f"Checking for backups older than {RETENTION_DAYS} days...")
    
    current_time = datetime.datetime.now().timestamp()
    
    for filename in os.listdir(BACKUP_FOLDER):
        file_path = os.path.join(BACKUP_FOLDER, filename)
        
        if filename.endswith('.zip'):
            file_creation_time = os.path.getctime(file_path)
            
            age_in_days = (current_time - file_creation_time) / (24 * 3600)
            
            if age_in_days > RETENTION_DAYS:
                os.remove(file_path)
                print(f"DELETED (Expired): {filename}")
            else:
                print(f"KEPT (Recent): {filename}")

if __name__ == "__main__":
    # Create a dummy folder to backup if it doesn't exist (just for testing)
    if not os.path.exists(SOURCE_FOLDER):
        os.makedirs(SOURCE_FOLDER)
        with open(os.path.join(SOURCE_FOLDER, 'dummy_file.txt'), 'w') as f:
            f.write("This is a test document.")
            
    create_backup()
    prune_old_backups()