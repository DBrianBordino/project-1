import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.switch import Switch
from datetime import datetime

kivy.require('2.0.0')

class MyApp(App):
    inicio = None
    fin = None

    def build(self):
        self.layout = MyBoxLayout()
        return self.layout

    def registrar_inicio(self):
        self.inicio = datetime.now()
        self.layout.ids.hora_inicio.text = self.inicio.strftime('%H:%M')
        self.layout.ids.switch_lanzamiento.active = False
        self.layout.ids.tiempo_transcurrido.text = ''
        

    def registrar_fin(self):
        if self.inicio:
            fin = datetime.now()
            tiempo_transcurrido = fin - self.inicio
            horas, segundos = divmod(tiempo_transcurrido.seconds, 3600)
            minutos = segundos // 60
            self.layout.ids.tiempo_transcurrido.text = (
                f'\n{horas:02d}:{minutos:02d}\n'
                f'Inicio: {self.inicio.strftime("%H:%M")}\n'
                f'Fin: {fin.strftime("%H:%M")}'
            )
            self.layout.ids.hora_inicio.text = ''
            self.layout.ids.hora_fin.text = ''
        else:
            self.layout.ids.tiempo_transcurrido.text = 'Primero, registra el inicio.'
            self.layout.ids.hora_fin.text = 'Presione para comenzar'




    def habilitar_botones(self, active):
        self.layout.ids.boton_inicio.disabled = not active
        self.layout.ids.boton_fin.disabled = not active


class MyBoxLayout(BoxLayout):
    pass

class BotonInicio(Button):
    pass

class BotonFin(Button):
    pass

class SwitchLanzamiento(Switch):
    pass

if __name__ == '__main__':
    MyApp().run()