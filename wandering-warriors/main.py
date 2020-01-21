from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from assets.DrawPad import DrawPad


class Calculator(Screen):
    pass


class Settings(Screen):
    pass


class Screen_Holder(Screen):
    pass


class TopMenu(Widget):
    pass


class Abacus(Widget):
    pass


class Ledger(Widget):
    pass


class OperationsBar(Widget):
    pass


class CuneiformDrawingInput(DrawPad):
    pass


class Screen:
    def __init__(self):
        self.sm = ScreenManager()
        self.sm.add_widget(Calculator(name='calculator'))

    def get_manager(self):
        return self.sm


class CalculatorApp(App):
    def build(self):
        Builder.load_file("calculator.kv")
        return Screen().get_manager()


if __name__ == "__main__":
    CalculatorApp().run()
