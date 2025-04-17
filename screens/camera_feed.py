# screens/camera_feed.py

from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
from picamera2 import Picamera2

class CameraFeed(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
        self.picam2.start()

        Clock.schedule_interval(self.update, 1.0 / 30)

    def update(self, dt):
        frame = self.picam2.capture_array()
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        buf = frame_rgb.tobytes()
        texture = Texture.create(size=(frame_rgb.shape[1], frame_rgb.shape[0]), colorfmt='rgb')
        texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

        self.texture = texture
        self.current_frame = frame  # capture_screen'de erişeceğiz
