from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget


'''
class ImagesExample(Image):
    pass
'''


class WidgetExample(GridLayout):
    counter = 1
    startingState = 50
    my_text = StringProperty(str(counter))
    SliderText = StringProperty(str(startingState))
    text_input = StringProperty("foo")
    OnOffProperty = StringProperty("Off")
    State = BooleanProperty(False)

    def on_button_click(self):
        # print("Button Clicked")
        self.counter += 1
        self.my_text = str(self.counter)

    def enabled(self):
        return self.State

    def secondButton(self):
        self.onActivated()

    def onActivated(self):
        self.State = not self.State

    def onSlider(self, widget):
        print(widget.value)
        self.SliderText = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input = widget.text
        pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     # self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)


class Canvas1(Widget):
    pass


class Canvas2(Widget):
    pass


class MainWidget(Widget):
    pass


class TheLabApp(App):
    timer = 0

    def __init__(self):
        super().__init__()


TheLabApp().run()
