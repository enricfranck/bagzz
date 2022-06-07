import threading
import time

from kivy.clock import mainthread
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.screen import MDScreen
from back_end.base import insert_data, get_by_name


class Content(BoxLayout):
    desc = StringProperty()


class ProductDetailScreen(MDScreen):

    def process_spinner_toogle(self):
        threading.Thread(target=(
            self.retrieve_product)).start()

    @mainthread
    def retrieve_product(self):
        data = MDApp.get_running_app().data
        info = data["info"]
        key = ['Description', 'Usage', 'Fonction',
               'Garentie', 'Arome', 'Fluorure', 'Ingredients']
        for i in range(len(key)):
            if info[key[i]] != "":
                self.ids.description_panel.add_widget(MDExpansionPanel(
                    icon="",
                    content=Content(desc="".join(info[key[i]])),
                    panel_cls=MDExpansionPanelOneLine(
                        text=key[i]
                    )
                ))

    def on_enter(self, *args):
        data = MDApp.get_running_app().data
        self.ids.name.text = f"[b]{data['name']}[/b]"
        self.ids.types.text = data["types"]
        self.ids.image.source = data["image"]
        self.ids.description_panel.clear_widgets()
        self.ids.content.text = data["content"]
        self.process_spinner_toogle()

    def save_product(self, name, image, category):
        product = get_by_name(name)
        if not product:
            insert_data(name, image, category)
            toast("produit bien ajouté")
        else:
            toast("Produit déjà dans le panier")
