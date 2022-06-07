from kivy.utils import rgba
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class MyCartScreen(MDScreen):
    def on_enter(self, *args):
        pass

    def go_next(self, screen: str) -> None:
        print("text")
        self.manager.current = screen
