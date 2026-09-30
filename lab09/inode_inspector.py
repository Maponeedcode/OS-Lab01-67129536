# inode_inspector.py
import os
import stat
import time

def inspect_file(filename):
    print(f"--- OS Inode Inspection for: {filename} ---")
    
    # OS System Call: stat() gets the file's metadata from the filesystem
    file_stats = os.stat(filename)
    
    # Extracting Metadata
    inode_number = file_stats.st_ino
    file_size_bytes = file_stats.st_size
    
    # Formatting timestamps
    created_time = time.ctime(file_stats.st_ctime)
    modified_time = time.ctime(file_stats.st_mtime)
    
    # Decoding POSIX Permissions
    # stat.filemode converts raw bits into human-readable format (e.g., -rw-r--r--)
    permissions = stat.filemode(file_stats.st_mode)
    
    print(f"Inode Number:     {inode_number}")
    print(f"File Size:        {file_size_bytes} bytes")
    print(f"Created On:       {created_time}")
    print(f"Last Modified:    {modified_time}")
    print(f"OS Permissions:   {permissions}")

def main():
    test_file = "dataset_sample.csv"
    
    # Create a dummy file
    with open(test_file, "w") as f:
        f.write("id,feature_1,feature_2,label\n")
        f.write("1,0.5,0.8,cat\n")
        
    inspect_file(test_file)

if __name__ == "__main__":
    main()