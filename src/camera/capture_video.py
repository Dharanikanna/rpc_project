from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start_and_record_video("src/camera/camera_output/video.mp4", duration=5)
