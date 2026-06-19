from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class EcoScannerApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.3, 0.15, 1)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        title = Label(
            text='[b]ECO-SCANNER[/b]',
            markup=True,
            font_size='40sp',
            color=(0.5, 1, 0.5, 1),
            size_hint_y=0.3
        )
        
        message = Label(
            text='Bienvenue dans votre assistant eco-responsable !',
            font_size='24sp',
            color=(1, 1, 1, 1),
            size_hint_y=0.3
        )
        
        btn = Button(
            text='LANCER LE SCAN',
            font_size='22sp',
            size_hint_y=0.2,
            background_color=(0.2, 0.7, 0.3, 1)
        )
        
        self.co2_label = Label(
            text='CO2 economise : 0.0 kg',
            font_size='20sp',
            color=(0.8, 1, 0.8, 1),
            size_hint_y=0.2
        )
        
        layout.add_widget(title)
        layout.add_widget(message)
        layout.add_widget(btn)
        layout.add_widget(self.co2_label)
        return layout

if __name__ == '__main__':
    EcoScannerApp().run()