# starvation_sim.py
import threading
import time

shared_resource_lock = threading.Lock()
job_counts = {"Greedy_Model_A": 0, "Greedy_Model_B": 0, "Polite_Model": 0}
is_running = True

def greedy_task(name):
    """A greedy thread that constantly attacks the lock."""
    while is_running:
        shared_resource_lock.acquire()
        
        # Critical Section
        job_counts[name] += 1
        
        shared_resource_lock.release()
        # Micro-sleep to force OS context switch, but immediately competes again
        time.sleep(0.00001) 

def polite_task(name):
    """A polite thread that waits nicely before requesting the lock."""
    while is_running:
        # Polite worker waits slightly longer before requesting
        time.sleep(0.01) 
        
        shared_resource_lock.acquire()
        
        # Critical Section
        job_counts[name] += 1
        
        shared_resource_lock.release()

def main():
    print("--- Starting Cluster Starvation Simulation (Running for 3 seconds) ---")
    
    t1 = threading.Thread(target=greedy_task, args=("Greedy_Model_A",))
    t2 = threading.Thread(target=greedy_task, args=("Greedy_Model_B",))
    t3 = threading.Thread(target=polite_task, args=("Polite_Model",))

    t1.start()
    t2.start()
    t3.start()

    # Let the simulation run for exactly 3 seconds
    time.sleep(3.0)
    
    global is_running
    is_running = False # Signal all threads to stop

    t1.join()
    t2.join()
    t3.join()

    print("\n--- Final Resource Acquisition Counts ---")
    for worker_name, count in job_counts.items():
        print(f"{worker_name}: {count} times")

if __name__ == "__main__":
    main()