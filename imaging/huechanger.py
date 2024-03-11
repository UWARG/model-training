import cv2
import numpy as np
import tkinter as tk
from tkinter import Scale, Button, HORIZONTAL, filedialog
import pickle

# Initialize global variables for channel dominance
red_dominance = 1.0
green_dominance = 1.0
blue_dominance = 1.0

def adjust_color_dominance(frame):
    # Adjust the color dominance of each channel
    frame[:, :, 2] = np.clip(frame[:, :, 2] * red_dominance, 0, 255)  # Red channel
    frame[:, :, 1] = np.clip(frame[:, :, 1] * green_dominance, 0, 255)  # Green channel
    frame[:, :, 0] = np.clip(frame[:, :, 0] * blue_dominance, 0, 255)  # Blue channel
    return frame

def update():
    ret, frame = cap.read()
    if ret:
        adjusted_frame = adjust_color_dominance(frame)
        cv2.imshow("Video Feed", adjusted_frame)
    
    # Call the update function every 20 milliseconds
    root.after(20, update)

def set_dominance(channel, value):
    global red_dominance, green_dominance, blue_dominance
    if channel == "red":
        red_dominance = float(value)
    elif channel == "green":
        green_dominance = float(value)
    elif channel == "blue":
        blue_dominance = float(value)

def save_settings():
    settings = {
        "red_dominance": red_dominance,
        "green_dominance": green_dominance,
        "blue_dominance": blue_dominance
    }
    with open("settings.pkl", "wb") as file:
        pickle.dump(settings, file)

def load_settings():
    try:
        with open("settings.pkl", "rb") as file:
            settings = pickle.load(file)
            set_dominance("red", settings["red_dominance"])
            set_dominance("green", settings["green_dominance"])
            set_dominance("blue", settings["blue_dominance"])
            red_slider.set(settings["red_dominance"])
            green_slider.set(settings["green_dominance"])
            blue_slider.set(settings["blue_dominance"])
    except FileNotFoundError:
        pass

def close_app():
    save_settings()
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Color Dominance Adjustment")

# Create sliders to adjust color dominance for each channel
red_label = tk.Label(root, text="Red Dominance:")
red_label.pack()
red_slider = Scale(root, from_=0, to=2, resolution=0.1, orient=HORIZONTAL, command=lambda value: set_dominance("red", value))
red_slider.pack()

green_label = tk.Label(root, text="Green Dominance:")
green_label.pack()
green_slider = Scale(root, from_=0, to=2, resolution=0.1, orient=HORIZONTAL, command=lambda value: set_dominance("green", value))
green_slider.pack()

blue_label = tk.Label(root, text="Blue Dominance:")
blue_label.pack()
blue_slider = Scale(root, from_=0, to=2, resolution=0.1, orient=HORIZONTAL, command=lambda value: set_dominance("blue", value))
blue_slider.pack()

# Create a button to save settings
save_button = Button(root, text="Save Settings", command=save_settings)
save_button.pack()

# Create a button to load settings
load_button = Button(root, text="Load Settings", command=load_settings)
load_button.pack()

# Open the webcam using OpenCV
cap = cv2.VideoCapture(0)

# Load settings when the application starts
load_settings()

# Start the video adjustment and processing loop
update()

# Create a button to exit the application
exit_button = Button(root, text="Exit", command=close_app)
exit_button.pack()

# Start the Tkinter main loop
root.mainloop()
