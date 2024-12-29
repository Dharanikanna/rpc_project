from picamera2 import Picamera2
import time

# Initialize the camera
picam2 = Picamera2()

# Configure the camera for video recording (you can customize resolution)
video_config = picam2.create_video_configuration(main={"size": (1920, 1080)})
picam2.configure(video_config)

# Create a video output file
output_path = "src/camera/camera_output/video.mp4"

# Start recording video
picam2.start_recording(output_path)

# Record for 5 seconds
time.sleep(5)

# Stop recording
picam2.stop_recording()
