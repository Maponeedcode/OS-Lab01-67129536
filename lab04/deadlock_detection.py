# deadlock_detection.py
import threading
import time

gpu_0_lock = threading.Lock()
gpu_1_lock = threading.Lock()

# Detection Threshold (Timeout in seconds)
TIMEOUT = 2.0 

def train_model_a():
    print("[Model A] Waiting for GPU 0...")
    gpu_0_lock.acquire()
    print("[Model A] Acquired GPU 0. Simulating work...")
    time.sleep(0.5)
    
    print("[Model A] Trying to acquire GPU 1 (Detection Mode)...")
    # DEADLOCK DETECTION: Wait only up to TIMEOUT seconds
    acquired = gpu_1_lock.acquire(timeout=TIMEOUT)
    
    if not acquired:
        # --- DEADLOCK DETECTED & RECOVERY ---
        print("\n>> [OS WATCHDOG] Deadlock Detected on Model A!")
        print(">> [RECOVERY] Model A is releasing GPU 0 to prevent total system freeze...\n")
        gpu_0_lock.release() # Rollback / Preempt resource
        return
    
    print("[Model A] Successfully acquired GPU 1! Training...")
    gpu_1_lock.release()
    gpu_0_lock.release()

def train_model_b():
    print("[Model B] Waiting for GPU 1...")
    gpu_1_lock.acquire()
    print("[Model B] Acquired GPU 1. Simulating work...")
    time.sleep(0.5)
    
    print("[Model B] Waiting for GPU 0...")
    # Model B gets blocked here, but will be saved when Model A yields
    gpu_0_lock.acquire()
    print("[Model B] Successfully acquired GPU 0! Training completed.")
    
    gpu_0_lock.release()
    gpu_1_lock.release()

def main():
    print("--- Starting Cluster with Deadlock Detection ---")
    t1 = threading.Thread(target=train_model_a)
    t2 = threading.Thread(target=train_model_b)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    print("--- System Finished (Recovered Successfully) ---")

if __name__ == "__main__":
    main()