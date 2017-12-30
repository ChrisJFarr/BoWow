import picamera
from time import sleep

camera = picamera.PiCamera()

# All camera settings with their default values
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 50
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.rotation = 0
camera.hflip = False
camera.vflip = False
camera.crop = (0.0, 0.0, 1.0, 1.0)

# Flip picture
camera.hflip = True
camera.vflip = True

# Record video
camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()

# Take picture
## camera.capture('image.jpg')

