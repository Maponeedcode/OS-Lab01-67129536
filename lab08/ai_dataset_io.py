# ai_dataset_io.py
import os
import time

def setup_test_files(num_files, file_size_bytes):
    print("Setting up test environments... (This might take a few seconds)")
    
    # 1. Create directory with many small files
    os.makedirs("raw_images_folder", exist_ok=True)
    for i in range(num_files):
        with open(f"raw_images_folder/img_{i}.bin", "wb") as f:
            f.write(b'\x00' * file_size_bytes)
            
    # 2. Create one large continuous dataset file (TFRecord style)
    with open("packed_dataset.tfrecord", "wb") as f:
        f.write(b'\x00' * (num_files * file_size_bytes))
        
    print("Setup complete.\n")

def test_random_small_files(num_files):

    print(f"Test 1: Reading {num_files} separate small files (Raw Images)")
    start_time = time.time()
    
    for i in range(num_files):
        # High OS Overhead: Open -> Read -> Close (Repeated 5000 times)
        with open(f"raw_images_folder/img_{i}.bin", "rb") as f:
            data = f.read()
            
    elapsed = time.time() - start_time
    print(f"-> Time Taken: {elapsed:.4f} seconds")

def test_sequential_large_file(num_files, file_size_bytes):
    print("\nTest 2: Reading 1 large packed file (TFRecord format)")
    start_time = time.time()
    
    # Low OS Overhead: Open once -> Read sequentially in chunks -> Close once
    with open("packed_dataset.tfrecord", "rb") as f:
        for i in range(num_files):
            data = f.read(file_size_bytes)
            
    elapsed = time.time() - start_time
    print(f"-> Time Taken: {elapsed:.4f} seconds")

def cleanup(num_files):
    for i in range(num_files):
        os.remove(f"raw_images_folder/img_{i}.bin")
    os.rmdir("raw_images_folder")
    os.remove("packed_dataset.tfrecord")

def main():

    NUM_FILES = 1000
    FILE_SIZE = 4096 # 4KB per file
    
    setup_test_files(NUM_FILES, FILE_SIZE)
    
    test_random_small_files(NUM_FILES)
    test_sequential_large_file(NUM_FILES, FILE_SIZE)
    
    cleanup(NUM_FILES)

if __name__ == "__main__":
    main()