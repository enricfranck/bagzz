from kivy.clock import mainthread
from kivy.properties import StringProperty
from kivy.utils import rgba
from kivymd.uix.screen import MDScreen

from back_end.get_data import get_historic
from front_end.component.card_item_home import CardItem


class HistoricScreen(MDScreen):
    title = StringProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.is_initialise = True

    @mainthread
    def on_enter(self, *args):
        data = get_historic()
        if self.is_initialise and len(data) > 0:
            for obj in data["historic_general"]:
                self.ids.hist_gen.add_widget(CardItem(
                    image=obj["image"],
                    title=obj["titre"],
                    description="".join(obj["description"])
                ))
            for obj in data["historic_mada"]:
                self.ids.hist_mada.add_widget(CardItem(
                    image=obj["image"],
                    title=obj["titre"],
                    description="".join(obj["description"])
                ))
            self.is_initialise = False

    def current_slide(self, index):
        for i in range(2):
            if index == i:
                self.ids[f"slide{index}"].color = rgba(253, 140, 95, 255)
                self.ids[f"historic{index}"].opacity = 1
            else:
                self.ids[f"slide{i}"].color = rgba(233, 237, 240, 255)
                self.ids[f"historic{i}"].opacity = 0
