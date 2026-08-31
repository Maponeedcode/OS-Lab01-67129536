# runner_process.py
import time
import multiprocessing
from task import process_image

def process_worker(image_id):
    process_image(image_id)

def main():
    num_images = 16
    processes = []
    
    print(f"--- Starting Multiprocessing for {num_images} images ---")
    start_time = time.time()
    
    # Create 16 separate OS processes
    for i in range(num_images):
        p = multiprocessing.Process(target=process_worker, args=(i,))
        processes.append(p)
        p.start()
        
    # Wait for all processes to finish
    for p in processes:
        p.join()
        
    end_time = time.time()
    print(f"Total Time (Processes): {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()