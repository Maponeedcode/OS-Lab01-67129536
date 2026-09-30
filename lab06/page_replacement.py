# page_replacement.py

def simulate_fifo(reference_string, num_frames):
    frames = []
    page_faults = 0
    
    print(f"\n--- Running FIFO Algorithm (Frames: {num_frames}) ---")
    for page in reference_string:
        if page not in frames:
            page_faults += 1
            if len(frames) >= num_frames:
                # FIFO: Remove the first element (oldest)
                victim = frames.pop(0) 
                print(f"Page Fault! Evicted Page {victim}. Loaded Page {page}")
            else:
                print(f"Page Fault! Loaded Page {page} (Empty Frame)")
            frames.append(page)
        else:
            print(f"Page Hit! Page {page} is already in RAM.")
            
    print(f">> Total FIFO Page Faults: {page_faults}")
    return page_faults

def simulate_lru(reference_string, num_frames):
    frames = []
    page_faults = 0
    
    print(f"\n--- Running LRU Algorithm (Frames: {num_frames}) ---")
    for page in reference_string:
        if page not in frames:
            page_faults += 1
            if len(frames) >= num_frames:
                # LRU: Remove the first element (least recently used)
                victim = frames.pop(0)
                print(f"Page Fault! Evicted Page {victim}. Loaded Page {page}")
            else:
                print(f"Page Fault! Loaded Page {page} (Empty Frame)")
            frames.append(page)
        else:
            print(f"Page Hit! Page {page} is already in RAM.")
            # LRU Update: Move the accessed page to the end of the list (most recently used)
            frames.remove(page)
            frames.append(page)
            
    print(f">> Total LRU Page Faults: {page_faults}")
    return page_faults

def main():
    # Reference string exhibiting temporal locality (William Stallings, Fig 8.14)
    # Expected page faults with 3 frames: FIFO = 9 faults, LRU = 7 faults
    ai_memory_requests = [2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2]
    total_physical_frames = 3
    
    simulate_fifo(ai_memory_requests, total_physical_frames)
    simulate_lru(ai_memory_requests, total_physical_frames)

if __name__ == "__main__":
    main()