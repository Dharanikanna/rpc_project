from picamera2 import Picamera2

picam2 = Picamera2()
picam2.start_and_capture_file("src/camera/camera_output/image.jpg")
