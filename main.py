from kivy.config import Config
Config.set('graphics', 'fullscreen', '1')     # Tam ekran
Config.set('graphics', 'show_cursor', '0')    # İmleç kapalı

from kivy.app import App
from screens.pin_screen import PinScreen
from kivy.core.window import Window

Window.clearcolor = (0, 0, 0, 1)      
Window.size = (320, 480)

class SmartLockApp(App):
    def build(self):
        return PinScreen()

if __name__ == '__main__':
    SmartLockApp().run()
