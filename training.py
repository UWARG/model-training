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

# Model hyperparameters
# Configurations: https://docs.ultralytics.com/usage/cfg/
IMAGE_DIMENSION = 720
SAVE_EVERY_NTH_EPOCH = 10
DEVICE = 0  # CPU or CUDA device
WORKER_COUNT = 4  # Worker threads


def main() -> int:
    """
    Main function
    """
    # Load model
    # Start with MODEL_START or resume with MODEL_RESUME_PATH
    model = ultralytics.YOLO(MODEL_START)

    # Train
    model.train(
        data=DATASET_PATH,
        imgsz=IMAGE_DIMENSION,
        save=True,
        save_period=SAVE_EVERY_NTH_EPOCH,
        device=DEVICE,
        workers=WORKER_COUNT,
        verbose=True,
        resume=True,  # Ignored if model is not initialized with an existing .pt model
    )

    return 0


if __name__ == "__main__":
    result_main = main()
    if result_main < 0:
        print(f"ERROR: Status code: {result_main}")

    print("Done!")
