# runner_seq.py
import time
from task import process_image

def main():
    num_images = 16  # We want to process 16 images
    
    print(f"--- Starting Sequential Processing for {num_images} images ---")
    start_time = time.time()
    
    for i in range(num_images):
        process_image(i)
        
    end_time = time.time()
    print(f"Total Time (Sequential): {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()