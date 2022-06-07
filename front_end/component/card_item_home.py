import threading

from kivy.clock import mainthread
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout


class CardItem(MDCard):
    image = StringProperty()
    title = StringProperty()
    description = StringProperty()


class CardItemProduct(MDFloatLayout):
    image_icon = StringProperty()
    image = StringProperty()
    types = StringProperty()
    name = StringProperty()
    content = StringProperty()
    usage = StringProperty()
    function = StringProperty()
    garent = StringProperty()
    arome = StringProperty()
    fluorure = StringProperty()
    description = StringProperty()
    ingredients = StringProperty()

    def process_spinner_toogle(self):
        threading.Thread(target=(
            self.detail_product)).start()

    @mainthread
    def detail_product(self, name, content, image, types,
                       usage, function, garent, arome, fluorure, description, ingredients):
        """
        View product detail
        :param types:
        :param ingredients:
        :param description:
        :param fluorure:
        :param arome:
        :param garent:
        :param function:
        :param desc:
        :param content:
        :param image:
        :param usage:
        :param name:
        :return:
        """
        data: dict = {
            "name": name, "types": types, "content": content,
            "image": image,
            "info": {"Description": description, "Usage": usage,
                     "Fonction": function, "Garentie": garent,
                     "Arome": arome, "Fluorure": fluorure,
                     "Ingredients": ingredients}
        }
        MDApp.get_running_app().data = data
        MDApp.get_running_app().sm.current = "product_detail"


class CardItemMyCart(MDBoxLayout):
    image = StringProperty()
    name = StringProperty()
    price = StringProperty()
    category = StringProperty()
