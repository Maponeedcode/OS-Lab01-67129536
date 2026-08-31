# race_condition.py
import threading
import time

# Shared Memory (Simulating ML Model Weights)
shared_weight = 0

def update_weights(iterations):
    global shared_weight
    for _ in range(iterations):
        # --- CRITICAL SECTION ---
        # Simulating a non-atomic operation (Read -> Modify -> Write)
        temp = shared_weight
        # A tiny sleep forces the OS scheduler to switch threads right here
        time.sleep(0.0000001) 
        shared_weight = temp + 1
        # ------------------------

def main():
    target_iterations = 100
    
    # Create 2 threads trying to update the exact same weight
    t1 = threading.Thread(target=update_weights, args=(target_iterations,))
    t2 = threading.Thread(target=update_weights, args=(target_iterations,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    expected_value = target_iterations * 2
    print(f"Expected Weight Value: {expected_value}")
    print(f"Actual Weight Value:   {shared_weight}")
    
    if expected_value != shared_weight:
        print(">> ERROR: Race Condition Detected! Data is corrupted.")

if __name__ == "__main__":
    main()