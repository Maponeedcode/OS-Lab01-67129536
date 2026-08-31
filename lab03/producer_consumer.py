# producer_consumer.py
import threading
import time
import random

# Shared Memory: Bounded Buffer
BUFFER_SIZE = 5
buffer = [None] * BUFFER_SIZE
in_index = 0
out_index = 0

# OS Synchronization Tools
mutex = threading.Lock()               # Protects critical sections (in_index, out_index)
empty = threading.Semaphore(BUFFER_SIZE) # Counts empty slots
full = threading.Semaphore(0)            # Counts filled slots

def data_loader_producer():
    """Simulates loading images from Disk to RAM (Buffer)"""
    global in_index
    for i in range(10):
        item = f"Image_Batch_{i}"
        time.sleep(random.uniform(0.1, 0.3)) # Simulating Disk I/O delay
        
        empty.acquire() # WAIT if buffer is full (slots == 0)
        mutex.acquire() # LOCK the buffer for writing
        
        # --- CRITICAL SECTION ---
        buffer[in_index] = item
        print(f"[Producer] Loaded: {item} into slot {in_index}")
        in_index = (in_index + 1) % BUFFER_SIZE
        # ------------------------
        
        mutex.release() # UNLOCK the buffer
        full.release()  # SIGNAL that a new item is available

def gpu_trainer_consumer():
    """Simulates taking images from RAM (Buffer) to Train Model"""
    global out_index
    for i in range(10):
        full.acquire()  # WAIT if buffer is empty (items == 0)
        mutex.acquire() # LOCK the buffer for reading
        
        # --- CRITICAL SECTION ---
        item = buffer[out_index]
        print(f"    -> [Consumer] Training on: {item} from slot {out_index}")
        out_index = (out_index + 1) % BUFFER_SIZE
        # ------------------------
        
        mutex.release() # UNLOCK the buffer
        empty.release() # SIGNAL that a slot is now empty
        
        time.sleep(random.uniform(0.2, 0.5)) # Simulating GPU training delay

def main():
    print("--- Starting ML Data Pipeline (Bounded Buffer) ---")
    producer_thread = threading.Thread(target=data_loader_producer)
    consumer_thread = threading.Thread(target=gpu_trainer_consumer)
    
    producer_thread.start()
    consumer_thread.start()
    
    producer_thread.join()
    consumer_thread.join()
    print("--- Pipeline Execution Completed Successfully ---")

if __name__ == "__main__":
    main()