from kivy.metrics import dp
from kivy.utils import rgba
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.screen import MDScreen

from back_end.get_data import get_stockist


class ValidationScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.menu_stockist = None

    def on_enter(self, *args):
        if not MDApp.get_running_app().stockist:
            data = get_stockist()
            MDApp.get_running_app().stockist = data["stockist"]

        self.menu_stockist = MDDropdownMenu(
            caller=self.ids.stockist,
            items=self.get_all_stockist(),
            width_mult=5,
        )

    def get_all_stockist(self):
        stockist = []
        for titre in MDApp.get_running_app().stockist:
            stockist.append(f"{titre['name']}, {titre['address']}")
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"{stockist[i]}",
                "height": dp(50),
                "on_release": lambda x=f"{stockist[i]}": self.menu_calback_stockist(x),
            } for i in range(len(stockist))
        ]
        return menu_items

    def menu_calback_stockist(self, text_item):
        self.ids.stockist.text = text_item
        self.menu_stockist.dismiss()
