import os

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivy.utils import platform, get_color_from_hex
from kivymd.toast import toast

from back_end.base import create_db, get_all_data, get_by_name, delete_by_name
from front_end.component.card_item_home import CardItemMyCart
from front_end.screens.adhesion_screen import AdhesionScreen
from front_end.screens.historic_screen import HistoricScreen
from front_end.screens.main_screen import MainScreen
from front_end.screens.marketing_screen import MarketingScreen
from front_end.screens.product_detail_screen import ProductDetailScreen
from front_end.screens.renumeration_screen import RenumerationScreen
from front_end.screens.validation_screen import ValidationScreen


class MyScrollView(ScrollView):
    def on_touch_down(self, touch):
        x, y = self.root.get_screen('Main').ids.list_product.to_widget(*self.to_window(*touch.pos))

        if self.root.get_screen('Main').ids.list_image.collide_point(x, y):
            touch.pos = (x, y)
            return self.root.get_screen('Main').ids.list_image.on_touch_down(touch)
        else:
            return super(MyScrollView, self).on_touch_down(touch)


class HistoricScreen(HistoricScreen):
    pass


class MainScreen(MainScreen):
    pass


class MarketingScreen(MarketingScreen):
    pass


class RenumerationScreen(RenumerationScreen):
    pass


class AdhesionScreen(AdhesionScreen):
    pass


class ProductDetailScreen(ProductDetailScreen):
    pass


class ValidationScreen(ValidationScreen):
    pass


class App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.carousel = None
        Window.bind(on_keyboard=self.Android_back_click)
        self.sm = ScreenManager(transition=FadeTransition())
        self.data_folder = None
        self.stockist = []

    def Android_back_click(self, window, key, *largs):
        if key == 27:
            if self.sm.current == "Main":
                if self.root.get_screen('Main').ids.carousel.index == 0:
                    self.close_app()
                else:
                    self.select_screen(0)
            else:
                self.sm.current = "Main"
            return True

    def select_screen(self, index):
        """
            to select one screen
        :param index:
        :return: None
        """
        self.carousel = self.root.get_screen('Main').ids.carousel
        self.carousel.index = index
        self.root.get_screen('Main').ids[f"button{index}"].text_color = get_color_from_hex('#10B34E')
        self.root.get_screen('Main').ids[f"label{index}"].text_color = get_color_from_hex('#10B34E')
        for i in range(4):
            if i != index:
                self.root.get_screen('Main').ids[f"button{i}"].text_color = get_color_from_hex('#000000')
                self.root.get_screen('Main').ids[f"label{i}"].text_color = get_color_from_hex('#000000')

    def build(self):
        self.load_all_kv_files()
        self.sm.add_widget(MainScreen())
        self.sm.add_widget(HistoricScreen())
        self.sm.add_widget(MarketingScreen())
        self.sm.add_widget(RenumerationScreen())
        self.sm.add_widget(AdhesionScreen())
        self.sm.add_widget(ProductDetailScreen())
        self.sm.add_widget(ValidationScreen())
        create_db()
        return self.sm

    def close_app(self, *larg):
        super(App, self).stop(*larg)

    def load_all_kv_files(self):
        Builder.load_file('front_end/kv_file/main_screen.kv')
        Builder.load_file('front_end/kv_file/historic_screen.kv')
        Builder.load_file('front_end/kv_file/adhesion_screen.kv')
        Builder.load_file('front_end/kv_file/renumeration.kv')
        Builder.load_file('front_end/kv_file/marketing_screen.kv')
        Builder.load_file('front_end/kv_file/card_item_home.kv')
        Builder.load_file('front_end/kv_file/product_detail_screen.kv')
        Builder.load_file('front_end/kv_file/validation_screen.kv')

    def create_folder(self):
        if platform == "android":
            self.data_folder = os.getenv("EXTERNAL_STORAGE") or os.path.expanduser("~")
            path = os.path.join(self.data_folder, "longrich")

    def remove_product(self, name: str):
        data = delete_by_name(name)
        self.root.get_screen('Main').ids.list_my_cart.clear_widgets()
        for obj in data:
            self.root.get_screen('Main').ids.list_my_cart.add_widget(CardItemMyCart(
                name=obj[0],
                image=obj[1],
                price="",
                category=obj[2],
            ))


if __name__ == "__main__":
    App().run()
