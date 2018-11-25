from random import sample
from string import ascii_lowercase

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


kv = """
<Row@GridLayout>:
    canvas:
        Color:
            rgba: 0.941, 0.902, 0.56, 1
        Rectangle:
            size: self.size
            pos: self.pos
    cols: 6
    rows: 1
    size_hint_y: None
    height: dp(108)
    padding: dp(0)
    spacing: dp(5)
    value: ''
    TextInput:
        id: beer_name
        size_hint_x: 0.6
        hint_text: 'Biername'
        padding: dp(10), dp(10), 0, 0
    Label:
        text: root.value
    Label:
        text: root.value
    Label:
        text: root.value
    Label:
        text: root.value
    Label:
        text: root.value

<Test>:
    canvas:
        Color:
            rgba: 0.3, 0, 0, 1
        Rectangle:
            size: self.size
            pos: self.pos
    rv: rv
    orientation: 'vertical'
    
    GridLayout:
        cols: 6
        rows: 1
        row_force_default: True
        row_default_height: dp(90)
        size_hint_y: None
        height: dp(90)
        padding: dp(0)
        spacing: dp(0)
        canvas:
            Color:
                rgba: 0.941, 0.902, 0.56, 1
            Rectangle:
                size: self.size
                pos: self.pos
        GridLayout: 
            cols: 1
            rows: 3
            size_hint_y: self.parent.height
            padding: dp(2)
            spacing: dp(5)
            Button: 
                text: 'Biername'
            Button: 
                text: 'Braudatum'
            Button:
                text: 'Verantwortlich'
        GridLayout:
            cols: 1
            rows: 2
            size_hint_y: self.parent.height
            padding: dp(2)
            spacing: dp(5)
            Button:
                text: 'Fass-Nr.'
            Label:
                text: 'Menge [L]'
        GridLayout:
            cols: 1
            rows: 2
            size_hint_y: self.parent.height
            padding: dp(2)
            spacing: dp(5)
            Label:
                text: 'Geschlaucht'
            Label: 
                text: 'Datum'
        GridLayout:
            cols: 1
            rows: 2
            size_hint_y: self.parent.height
            padding: dp(2)
            spacing: dp(5)
            Label:
                text: 'Umgedrückt'
            Label: 
                text: 'Datum'
        GridLayout:
            cols: 1
            rows: 2
            size_hint_y: self.parent.height
            padding: dp(2)
            spacing: dp(5)
            Label:
                text: 'Gespundet'
            Label: 
                text: 'Startdatum'
        GridLayout:
            cols: 1
            rows: 3
            size_hint_y: self.parent.height
            padding: dp(2)
            spacing: dp(5)
            Label:
                text: 'Bemerkungen'
            Label: 
                text: '(A) Anmerkung'
            Button: 
                text: '(V) Verwendung'                
                
    
    RecycleView:
        id: rv
        scroll_type: ['bars', 'content']
        scroll_wheel_distance: dp(114)
        bar_width: dp(10)
        viewclass: 'Row'
        RecycleBoxLayout:
            default_size: None, dp(56)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
            spacing: dp(2)
    GridLayout:
        cols: 2
        rows: 1
        size_hint_y: None
        height: dp(108)
        padding: dp(8)
        spacing: dp(16)
        Button:
            text: 'Sort list'
            on_press: root.sort()
        BoxLayout:
            spacing: dp(8)
            Button:
                text: 'Insert new item'
                on_press: root.insert(new_item_input.text)
            TextInput:
                id: new_item_input
                size_hint_x: 0.6
                hint_text: 'value'
                padding: dp(10), dp(10), 0, 0
        

"""

Builder.load_string(kv)


class Test(BoxLayout):

    def populate(self):
        self.rv.data = [{'value': ''.join(sample(ascii_lowercase, 6))}
                        for x in range(50)]

    def sort(self):
        self.rv.data = sorted(self.rv.data, key=lambda x: x['value'])

    def clear(self):
        self.rv.data = []

    def insert(self, value):
        self.rv.data.insert(0, {'value': value or 'default value'})

    def update(self, value):
        if self.rv.data:
            self.rv.data[0]['value'] = value or 'default new value'
            self.rv.refresh_from_data()

    def remove(self):
        if self.rv.data:
            self.rv.data.pop(0)


class TestApp(App):
    def build(self):
        return Test()


if __name__ == '__main__':
    TestApp().run()
