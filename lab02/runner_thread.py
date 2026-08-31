# runner_thread.py
import time
import threading
from task import process_image

def thread_worker(image_id):
    process_image(image_id)

def main():
    num_images = 16
    threads = []
    
    print(f"--- Starting Multithreading for {num_images} images ---")
    start_time = time.time()
    
    # Create 16 threads
    for i in range(num_images):
        t = threading.Thread(target=thread_worker, args=(i,))
        threads.append(t)
        t.start()
        
    # Wait for all threads to finish
    for t in threads:
        t.join()
        
    end_time = time.time()
    print(f"Total Time (Threads): {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()