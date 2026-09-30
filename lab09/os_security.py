# os_security.py
import os
import stat

def main():
    secure_file = "secret_config.json"
    
    # Clean up any read-only file from previous runs
    if os.path.exists(secure_file):
        os.chmod(secure_file, 0o666)
        os.remove(secure_file)
        
    # 1. Create a file normally
    with open(secure_file, "w") as f:
        f.write("{'api_key': '12345XYZ'}")
    print(f"Created {secure_file}.")
    
    # 2. Lock down the file using OS chmod (Change Mode)
    # 0o400 in Octal: User can Read (4). Group (0) and Others (0) have no access.
    print("Locking file permissions to Read-Only (0o400)...")
    os.chmod(secure_file, 0o400) 
    print(f"New Permissions: {stat.filemode(os.stat(secure_file).st_mode)}")
    
    # 3. Try to maliciously overwrite the file
    print("\nAttempting to overwrite the file...")
    try:
        with open(secure_file, "a") as f:
            f.write("\nMALICIOUS HACKER DATA")
        print("Success! Data written.")
    except PermissionError as e:
        print(f">>> [OS KERNEL BLOCKED] PermissionError: {e}")
        print(">>> The Operating System successfully protected the file!")

if __name__ == "__main__":
    main()