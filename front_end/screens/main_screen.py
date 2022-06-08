import random
import threading

from kivy.clock import mainthread
from kivy.properties import StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.screen import MDScreen

from back_end.base import get_all_data
from back_end.get_data import get_product, get_menu, get_stockist

from front_end.component.card_item_home import CardItemProduct, CardItemMyCart


def find_key(lettre: str, key: str):
    value = lettre.lower()
    key_value = key.lower()
    return value.find(key_value)


class Content_(MDBoxLayout):
    address = StringProperty()
    phone = StringProperty()


# class MyScrollView(ScrollView):
#     def on_touch_down(self, touch):
#         x, y = self.ids.list_product.to_widget(*self.to_window(*touch.pos))
#
#         if self.ids.list_image.collide_point(x, y):
#             touch.pos = (x, y)
#             return self.ids.list_image.on_touch_down(touch)
#         else:
#             return super(MyScrollView, self).on_touch_down(touch)
#

class MainScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_initialise_stockist = True
        self.product = None
        self.carousel = None
        self.is_initialise_product = True

    def process_spinner_toogle(self):
        threading.Thread(target=(
            self.get_my_cart)).start()

    def process_spinner_stockist(self):
        threading.Thread(target=(
            self.get_stockist)).start()

    def on_enter(self, *args):
        pass

    @mainthread
    def get_stockist(self):
        if self.is_initialise_stockist:
            if not MDApp.get_running_app().stockist:
                data = get_stockist()
                MDApp.get_running_app().stockist = data["stockist"]
            data = MDApp.get_running_app().stockist
            for obj in data:
                self.ids.list_stockist.add_widget(MDExpansionPanel(
                    icon="account-circle-outline",
                    content=Content_(address="".join(obj["address"]), phone=obj["phone"]),
                    panel_cls=MDExpansionPanelOneLine(
                        text=obj['name']
                    )
                ))
            self.is_initialise_stockist = False

    def select_screen(self, index):
        """
            to select one screen
        :param index:
        :return: None
        """

        self.carousel = self.ids.carousel
        self.carousel.index = index
        self.ids[f"button{index}"].text_color = get_color_from_hex('#10B34E')
        self.ids[f"label{index}"].text_color = get_color_from_hex('#10B34E')
        for i in range(4):
            if i != index:
                self.ids[f"button{i}"].text_color = get_color_from_hex('#000000')
                self.ids[f"label{i}"].text_color = get_color_from_hex('#000000')

    def get_all_product(self):
        """
        To retrieve all product from API
        :return:
        """
        if self.is_initialise_product:
            self.product = get_product()
            for index, obj in enumerate(self.product["product"]):
                self.ids.list_product.add_widget(CardItemProduct(
                    image=obj["Image"],
                    image_icon=obj["Image_icon"],
                    name=obj["Nom du produits"],
                    content=obj["Contenu net"],
                    types=obj["Type"],
                    description=obj["Description"],
                    usage=obj["Usage"],
                    function=obj["Fonction"],
                    garent=obj["Garentie"],
                    arome=obj["Arome"],
                    fluorure=obj["Fluorure"],
                    ingredients=obj["Ingredients"],
                ))
                self.is_initialise_product = False

    @mainthread
    def get_my_cart(self):
        data = get_all_data()
        self.ids.list_my_cart.clear_widgets()
        for obj in data:
            self.ids.list_my_cart.add_widget(CardItemMyCart(
                name=obj[0],
                image=obj[1],
                price="",
                category=obj[2],
            ))

    @mainthread
    def search_stockist(self, titre: str):
        value = list(
            filter(lambda obj_: find_key(obj_["name"], titre) != -1 or
                                find_key(obj_["address"], titre) != -1 or
                                find_key(obj_["phone"], titre) != -1,
                   MDApp.get_running_app().stockist))
        self.ids.list_stockist.clear_widgets()
        for obj in value:
            self.ids.list_stockist.add_widget(MDExpansionPanel(
                icon="account-circle-outline",
                content=Content_(address="".join(obj["address"]), phone=obj["phone"]),
                panel_cls=MDExpansionPanelOneLine(
                    text=obj['name']
                )
            ))

    @mainthread
    def search_product(self, titre: str):
        value = list(
            filter(lambda obj_: find_key(obj_["name"], titre) != -1 or
                                find_key(obj_["property"], titre) != -1 or
                                find_key(obj_["description"], titre) != -1,
                   self.product['product']))
        self.ids.list_product.clear_widgets()
        for obj in value:
            self.ids.list_product.add_widget(CardItemProduct(
                image=obj["image"],
                image_icon=obj["image_icon"],
                name=obj["name"],
                price=obj["price"],
                property=obj["property"],
                desc=obj["description"]
            ))
