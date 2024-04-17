import cv2
import numpy as np
import pyautogui 

# Set the screen resolution to record 
screen_width,screen_height=pyautogui.size()
resolution=(screen_width,screen_height)

# Set the output video filename
output_filename="screen_recording.mp4"

# Set the frames per second (fps) for the recording 
fps=30.0

fourcc=cv2.VideoWriter_fourcc(*"mp4v")
out=cv2.VideoWriter(output_filename,fourcc,fps,resolution)

# Set the recording durations in sec.
recording_duration=5

# Start the screen recording 
for i in range(int(fps * recording_duration)):

    # Capture the screen
    screen=pyautogui.screenshot()
    
    # Convert the screenshot to a numpy array and BGR format for OpenCV
    frame=np.array(screen)
    frame=cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    
    # Write the frame to the o/p.
    out.write(frame)

# Release the VideoWriter
out.release()