from random import sample
from string import ascii_lowercase

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


kv = """
<Row@GridLayout>:
    canvas:
        Color:
            rgba: 0.996, 0.941, 0.757, 1
        Rectangle:
            size: self.size
            pos: self.pos
    cols: 6
    rows: 1
    row_force_default: True
    row_default_height: dp(90)
    size_hint_y: None
    height: self.minimum_height
    padding: dp(0)
    spacing: dp(0)
    value: ''
    GridLayout:
        cols: 1
        rows: 3
        size_hint_y: self.parent.height
        padding: dp(2)
        spacing: dp(5)
        TextInput:
            id: beer_name
            size_hint_x: self.parent.width
            hint_text: 'Biername'
        Label: 
            text: root.value
        Label: 
            text: root.value
    GridLayout:
        cols: 1
        rows: 2
        size_hint_y: self.parent.height
        padding: dp(2)
        spacing: dp(5)
        Label:
            text: root.value
        Label:
            text: root.value
            color: (0.345, 0.169, 0.145, 1)
    GridLayout:
        cols: 1
        rows: 2
        size_hint_y: self.parent.height
        padding: dp(2)
        spacing: dp(5)
        Label: 
            text: root.value
            color: (0.345, 0.169, 0.145, 1)
        Label: 
            text: root.value
            color: (0.345, 0.169, 0.145, 1)

<Test>:
    canvas:
        Color:
            rgba: 0.345, 0.169, 0.145, 1
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
        height: self.minimum_height
        padding: dp(0)
        spacing: dp(0)
        canvas:
            Color:
                rgba: 0.996, 0.941, 0.757, 1
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
                color: (0.345, 0.169, 0.145, 1)
        GridLayout:
            cols: 1
            rows: 3
            size_hint_y: self.parent.height
            padding: dp(2)
            spacing: dp(5)
            Label:
                text: 'Bemerkungen'
                color: (0.345, 0.169, 0.145, 1)
            Label: 
                text: '(A) Anmerkung'
                color: (0.345, 0.169, 0.145, 1)
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
        cols: 4
        rows: 1
        row_force_default: True
        row_default_height: dp(90)
        size_hint_y: None
        height: self.minimum_height
        padding: dp(0)
        spacing: dp(0)
        canvas:
            Color:
                rgba: 0.996, 0.941, 0.757, 1
            Rectangle:
                size: self.size
                pos: self.pos
        GridLayout:
            cols: 1
            rows: 3
            size_hint_y: self.parent.height
            TextInput:
                id: beer_name
                size_hint_x: self.parent.width
                hint_text: 'Biername'
            TextInput:
                id: brewing_date
                size_hint_x: self.parent.width
                hint_text: 'Braudatum'
            TextInput:
                id: responsible_name
                size_hint_x: self.parent.width
                hint_text: 'Brauverantwortlicher'
        GridLayout:
            cols: 1
            rows: 3
            size_hint_y: self.parent.height
            TextInput:
                id: keg_number
                size_hint_x: self.parent.width
                hint_text: 'Fass-Nr.'
            TextInput:
                id: content_liter
                size_hint_x: self.parent.width
                hint_text: 'Menge'
            TextInput:
                id: packing_date
                size_hint_x: self.parent.width
                hint_text: 'Geschlaucht am ?'
        GridLayout:
            cols: 1
            rows: 3
            size_hint_y: self.parent.height
            Label:
                text: 'Bemerkungen'
                color: (0.345, 0.169, 0.145, 1)
            TextInput:
                id: note
                size_hint_x: self.parent.width
                hint_text: 'Anmerkung'
            TextInput:
                id: intendet_use
                size_hint_x: self.parent.width
                hint_text: 'Verwendung, Datum'        
            
        GridLayout:
            cols: 1
            rows: 2
            size_hint_y: self.parent.height  
            Button:
                text: 'Insert new item'
                on_press: root.insert(intendet_use.text)
            Button: 
                text: 'Clear'
                
            
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
        self.rv.data.insert(100, {'intendet_use': value or 'default value'})

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
