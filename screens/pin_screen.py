from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from ui.custom_button import CustomButton
import services.lock_control

class PinScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.pin = ""
        self.correct_pin = "1234"
        self.spacing = 20
        self.padding = 20
        self.background_color = (0, 0, 0, 1)

        self.label = Label(text="PIN GİRİN", font_size=28, size_hint=(1, 0.2), color=(1, 1, 1, 1))
        self.add_widget(self.label)

        self.pin_display = Label(text="", font_size=36, size_hint=(1, 0.2), color=(1, 1, 1, 1))
        self.add_widget(self.pin_display)

        self.grid = GridLayout(cols=3, spacing=10, size_hint=(1, 0.6))
        self.add_widget(self.grid)

        buttons = [
            "1", "2", "3",
            "4", "5", "6",
            "7", "8", "9",
            "Sil", "0", "Tamam"
        ]

        for label in buttons:
            btn = CustomButton(text=label)
            btn.bind(on_release=self.on_button_press)
            self.grid.add_widget(btn)

    def on_button_press(self, instance):
        text = instance.text
        if text == "Sil":
            self.pin = ""
        elif text == "Tamam":
            if self.pin == self.correct_pin:
                self.label.text = "KAPI AÇILDI"
                services.lock_control.lockOpen_threaded()
                Clock.schedule_once(lambda dt: self.reset_label(), 2)
                
            else:
                self.label.text = "❌ Yanlış PIN!"
            self.pin = ""
        else:
            if len(self.pin) < 6:
                self.pin += text
        self.pin_display.text = "*" * len(self.pin)
    def reset_label(self):
        self.label.text = "PİN GİRİN"
