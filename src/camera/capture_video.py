from picamzero import Camera

cam = Camera()
cam.start_preview()
cam.record_video("~/embedded/ml/rpc_project/camera_output/video.mp4", duration=5)
cam.stop_preview()