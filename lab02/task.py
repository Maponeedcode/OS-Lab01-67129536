# task.py
import time

def process_image(image_id):
    """
    Simulates a heavy mathematical operation on an image.
    (e.g., matrix transformation for ML data augmentation)
    """
    result = 0
    # A heavy loop to stress the CPU
    for i in range(5_000_000):
        result += (i ** 2) / 3.14159
    return result