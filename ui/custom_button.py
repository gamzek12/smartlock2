from kivy.uix.button import Button
from kivy.animation import Animation

class CustomButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''  # arka plan resmi yok
        self.background_color = (0, 0, 0, 1)  # siyah
        self.color = (1, 1, 1, 1)  # beyaz yazı
        self.font_size = 32

    def on_press(self):
        anim = Animation(background_color=(1, 1, 1, 1), color=(0, 0, 0, 1), duration=0.1)
        anim.start(self)

    def on_release(self):
        anim = Animation(background_color=(0, 0, 0, 1), color=(1, 1, 1, 1), duration=0.1)
        anim.start(self)
