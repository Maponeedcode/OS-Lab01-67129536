# ai_thrashing.py
import time
import os

def fast_ram_access(iterations):
    """Simulates AI training when everything fits in Physical RAM"""
    simulated_ram = [0.0] * 1000
    start_time = time.time()
    
    for _ in range(iterations):
        for i in range(len(simulated_ram)):
            simulated_ram[i] += 1.5 # Fast Memory CPU operation
            
    return time.time() - start_time

def slow_swap_thrashing_access(iterations, filename="swap_file.bin"):
    """Simulates Thrashing: OS is constantly reading/writing to the Disk Swap file"""
    # Create a dummy swap file
    with open(filename, "wb") as f:
        f.write(b'\x00' * 1000)
        
    start_time = time.time()
    
    for _ in range(iterations):
        # Thrashing: Constant Disk I/O because RAM is full
        with open(filename, "r+b") as f:
            data = bytearray(f.read())
            for i in range(len(data)):
                data[i] = (data[i] + 1) % 255
            f.seek(0)
            f.write(data)
            
    os.remove(filename) # Cleanup
    return time.time() - start_time

def main():
    print("--- Simulating AI Training Batch (10,000 Iterations) ---")
    iterations = 10000
    
    print("\n1. Scenario: Batch fits in RAM (No Page Faults)")
    ram_time = fast_ram_access(iterations)
    print(f"   -> Processing Time: {ram_time:.4f} seconds")
    
    print("\n2. Scenario: Out of Memory - OS is Thrashing (Swapping to Disk)")
    swap_time = slow_swap_thrashing_access(iterations)
    print(f"   -> Processing Time: {swap_time:.4f} seconds")
    
    performance_drop = swap_time / ram_time
    print(f"\n>>> SYSTEM IMPACT: Thrashing made the system {performance_drop:.0f} TIMES slower!")

if __name__ == "__main__":
    main()