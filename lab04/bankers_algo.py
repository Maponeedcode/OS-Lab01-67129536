# bankers_algo.py
import numpy as np

# System Resources: [GPU_Type_A, GPU_Type_B, High_Speed_RAM(TB)]
total_resources = np.array([10, 5, 7])

# Max requirement for each ML Job (Job 0, Job 1, Job 2)
max_need = np.array([
    [7, 5, 3], 
    [3, 2, 2], 
    [9, 0, 2]
])

# Currently allocated resources
allocated = np.array([
    [0, 1, 0], 
    [2, 0, 0], 
    [3, 0, 2]
])

def is_safe_state(available, max_need, allocated):
    num_jobs = len(allocated)
    work = available.copy()
    finish = [False] * num_jobs
    safe_sequence = []
    
    # Calculate remaining needs: Need = Max - Allocated
    need = max_need - allocated
    
    while len(safe_sequence) < num_jobs:
        allocated_in_this_round = False
        
        for i in range(num_jobs):
            if not finish[i] and all(need[i] <= work):
                # Job i can finish its execution
                work += allocated[i] # OS reclaims the resources
                finish[i] = True
                safe_sequence.append(f"Job_{i}")
                allocated_in_this_round = True
                
        if not allocated_in_this_round:
            return False, [] # System is in an UNSAFE state (Deadlock imminent)
            
    return True, safe_sequence

def main():
    print("--- OS Scheduler: Banker's Algorithm Check ---")
    
    # Calculate initially available resources
    available = total_resources - np.sum(allocated, axis=0)
    print(f"Currently Available Resources: {available}")
    
    safe, sequence = is_safe_state(available, max_need, allocated)
    
    if safe:
        print(f">> SYSTEM IS SAFE. Execution Sequence: {' -> '.join(sequence)}")
        print(">> OS will grant the lock requests.")
    else:
        print(">> WARNING: SYSTEM IS UNSAFE! Granting locks will cause a Deadlock.")
        print(">> OS Scheduler denies the request and forces the process to wait.")

if __name__ == "__main__":
    main()