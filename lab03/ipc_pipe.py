# ipc_pipe.py
import os
import time

def main():
    # Ask the OS to create a unidirectional communication channel (Pipe)
    # r = File descriptor for reading
    # w = File descriptor for writing
    r, w = os.pipe() 
    
    pid = os.fork()
    
    if pid > 0:
        # --- PARENT PROCESS (Simulating ML Trainer) ---
        os.close(w) # Parent only reads, so close the write end
        r_file = os.fdopen(r)
        
        print(f"[Trainer PID:{os.getpid()}] Waiting for data from DataLoader...")
        data = r_file.read() # Blocks until data is available
        print(f"[Trainer PID:{os.getpid()}] Received Data: '{data}'")
        print(f"[Trainer PID:{os.getpid()}] Training complete.")
        
        os.wait() # Reap the child process
        
    elif pid == 0:
        # --- CHILD PROCESS (Simulating DataLoader) ---
        os.close(r) # Child only writes, so close the read end
        w_file = os.fdopen(w, 'w')
        
        print(f"  -> [DataLoader PID:{os.getpid()}] Loading image from disk...")
        time.sleep(2) # Simulate I/O delay
        
        image_data = "Image_Tensor_Batch_01"
        print(f"  -> [DataLoader PID:{os.getpid()}] Sending data through OS Pipe...")
        w_file.write(image_data)
        w_file.close() # Closing signals EOF to the reader

if __name__ == "__main__":
    main()