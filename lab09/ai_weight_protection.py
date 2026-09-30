# ai_weight_protection.py
import os

def simulate_hpc_cluster():
    weight_file = "production_resnet50.pth"
    
    # Clean up any read-only file from previous runs
    if os.path.exists(weight_file):
        os.chmod(weight_file, 0o666)
        os.remove(weight_file)
        
    # Simulate downloading the trained model
    print("Downloading 250MB Production Model Weights...")
    with open(weight_file, "w") as f:
        f.write("0101010101010101010") # Fake binary weight data
    
    # AI Ops: Securing the asset
    print("AI Ops: Securing model weights at the OS level (Read-Only)...")
    os.chmod(weight_file, 0o444) # Everyone can read, NO ONE can write
    
    # Simulate a Junior Developer running a buggy training script
    print("\n[Junior Dev] Running script: training_job.py")
    print("[Junior Dev] 'Oops, I opened the production model in Write mode!'")
    
    try:
        # The buggy code
        model = open(weight_file, "w") 
        model.write("Initializing random weights... Overwriting!")
        model.close()
    except PermissionError:
        print(">>> [DISASTER AVERTED] OS Kernel denied write access.")
        print(">>> The multi-million dollar model is safe.")

if __name__ == "__main__":
    simulate_hpc_cluster()