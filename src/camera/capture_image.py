from picamzero import Camera

cam = Camera()
cam.start_preview()
cam.take_photo("~/embedded/ml/rpc_project/camera_output/image.jpg")
cam.stop_preview()