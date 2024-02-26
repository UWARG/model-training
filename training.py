"""
For model training
"""

import ultralytics


# n for nano, s for small, m for medium, l for large
# Use nano or small for now
MODEL_START = "yolov8n.yaml"

# Change path to last.pt in runs/ to resume
MODEL_RESUME_PATH = "path/to/last.pt"

# Path to configuration that describes the dataset directory structure
DATASET_PATH = "2023_pad.yaml"


if __name__ == "__main__":

    # Load model
    # Start or resume
    model = ultralytics.YOLO(MODEL_START)

    # Train
    # Configurations: https://docs.ultralytics.com/usage/cfg/
    model.train(
        data=DATASET_PATH,
        imgsz=720,
        save=True,
        save_period=10,
        device=0,
        workers=4,
        verbose=True,
        resume=True,  # Ignored if model is not initialized with an existing .pt model
    )

    print("Done!")
