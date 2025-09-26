from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout

from kivy_garden.webview import WebView

URL = "https://script.google.com/a/~/macros/s/AKfycbwGAABrxYCNDb5P_LOxVLAmXBJg6Zq573eqCtABPAP6u6IF1e_PJ4atHFaE12VCFEv6Og/exec"  # 🔹 Replace with your website


class SplashScreen(Screen):
    def on_enter(self):
        Clock.schedule_once(self.switch_to_webview, 3)

    def switch_to_webview(self, *args):
        self.manager.current = "webview"


class WebViewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout()
        layout.add_widget(WebView(url=URL))
        self.add_widget(layout)


class MNWebApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(WebViewScreen(name="webview"))

        splash_img = Image(source="icon.png")
        sm.get_screen("splash").add_widget(splash_img)

        return sm


if __name__ == "__main__":
    MNWebApp().run()
