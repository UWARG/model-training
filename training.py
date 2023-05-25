"""
For model training
"""

import ultralytics


# n for nano, s for small, m for medium, l for large
# Use nano or small for now
MODEL_START = "yolov8n.yaml"

# Change path to last.pt in runs/ to resume
MODEL_RESUME_PATH = "path/to/last.pt"

# Path to file that describes the test, train, val structure
#
# Ultralytics has a settings.yaml file with key-value pair: `datasets_dir: path/to/datasets/`
# settings.yaml can be found in:
# * Windows: C:/Users/[Username]/AppData/Roaming/Ultralytics/
# * MacOS: ~/Library/Application Support/Ultralytics/
# * Linux: ~/.config/Ultralytics/
# It concatenates datasets_dir and DATASET_PATH for the expected directory
# Place test, train, val directories there (HAVE ONLY 1 SET OF TRAINING DATA THERE AT A TIME,
# rename the others (e.g. test_old0, train_old0, val_old0)), otherwise Ultralytics can grab the
# wrong dataset which is bad
#
# Example:
# datasets_dir: C:/Users/WARG/Ultralytics/datasets
# DATASET_PATH: landing_pad/2023_pad.yaml
# Expected directories: C:/Users/WARG/datasets/landing_pad/[test, train, val]
DATASET_PATH = "landing_pad/2023_pad.yaml"


if __name__ == "__main__":

    # Load model
    # Start or resume
    model = ultralytics.YOLO(MODEL_START)

    # Train
    # Configurations: https://docs.ultralytics.com/usage/cfg/
    model.train(
        data="2023_pad.yaml",
        imgsz=720,
        save=True,
        save_period=10,
        device=0,
        workers=4,
        verbose=True,
        resume=True  # Ignored if model is not initialized with an existing .pt model
    )

    print("Done!")
