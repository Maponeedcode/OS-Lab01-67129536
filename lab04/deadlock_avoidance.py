# deadlock_avoidance.py
import threading
import time

gpu_0_lock = threading.Lock()
gpu_1_lock = threading.Lock()

def train_model_a():
    """Model A needs GPU 0 first, then GPU 1"""
    print("[Model A] Waiting for GPU 0...")
    gpu_0_lock.acquire()
    print("[Model A] Got GPU 0. Processing...")
    time.sleep(0.1) 
    
    print("[Model A] Waiting for GPU 1...")
    gpu_1_lock.acquire()
    print("[Model A] Got GPU 1! Training complete.")
    
    gpu_1_lock.release()
    gpu_0_lock.release()

def train_model_b():
    """
    Model B originally wanted GPU 1 first. 
    But to prevent Circular Wait, we FORCE it to request GPU 0 first.
    """
    print("[Model B] Waiting for GPU 0 (Strict Ordering Rule)...")
    gpu_0_lock.acquire()
    print("[Model B] Got GPU 0. Processing...")
    time.sleep(0.1) 
    
    print("[Model B] Waiting for GPU 1...")
    gpu_1_lock.acquire()
    print("[Model B] Got GPU 1! Training complete.")
    
    gpu_1_lock.release()
    gpu_0_lock.release()

def main():
    print("--- Starting ML Training Cluster (Safe Mode) ---")
    t1 = threading.Thread(target=train_model_a)
    t2 = threading.Thread(target=train_model_b)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    print("--- Cluster Execution Completed Successfully ---")

if __name__ == "__main__":
    main()