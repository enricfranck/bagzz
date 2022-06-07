from kivy.clock import mainthread
from kivy.properties import StringProperty
from kivy.utils import rgba
from kivymd.uix.screen import MDScreen

from back_end.get_data import get_marketing
from front_end.component.card_item_home import CardItem


class MarketingScreen(MDScreen):
    title = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_initialise = True

    @mainthread
    def on_enter(self, *args):
        data = get_marketing()
        if self.is_initialise and len(data) > 0:
            for obj in data["marketing"]:
                self.ids.marketing.add_widget(CardItem(
                    image=obj["image"],
                    title=obj["titre"],
                    description="".join(obj["description"])
                ))

    def current_slide(self, index):
        for i in range(2):
            if index == i:
                self.ids[f"slide{index}"].color = rgba(253, 140, 95, 255)
                self.ids[f"historic{index}"].opacity = 1
            else:
                self.ids[f"slide{i}"].color = rgba(233, 237, 240, 255)
                self.ids[f"historic{i}"].opacity = 0
