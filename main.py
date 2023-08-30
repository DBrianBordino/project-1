from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.clipboard import Clipboard
from datetime import datetime, timedelta

class SleepTimeApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.hora_acostado_input = TextInput(hint_text='Hora de acostarse (HH:MM)')
        self.hora_despertado_input = TextInput(hint_text='Hora de despertarse (HH:MM)')
        
        self.calcular_button = Button(text='Calcular tiempo de sueño')
        self.calcular_button.bind(on_release=self.calcular_tiempo)
        
        self.resultado_label = Label(text='')
        
        self.layout.add_widget(self.hora_acostado_input)
        self.layout.add_widget(self.hora_despertado_input)
        self.layout.add_widget(self.calcular_button)
        self.layout.add_widget(self.resultado_label)
        
        return self.layout
    
    def calcular_tiempo(self, instance):
        hora_acostado = self.hora_acostado_input.text
        hora_despertado = self.hora_despertado_input.text
        
        if hora_acostado and hora_despertado:
            tiempo_dormido, hora_acostado_real, hora_despertado_real = self.calcular_tiempo_dormido(hora_acostado, hora_despertado)
            horas = int(tiempo_dormido.total_seconds() // 3600)
            minutos = int((tiempo_dormido.total_seconds() % 3600) // 60)

            hoy = datetime.now().strftime("%Y-%m-%d")
            fecha_acostado = hora_acostado_real.strftime("%Y-%m-%d")
            if hoy != fecha_acostado:
                aclaracion_acostado = "ayer"
            else:
                aclaracion_acostado = "hoy"

            hora_despertado_str = hora_despertado_real.strftime('%H:%M')

            informe = f"\nDESCANSO\nFecha de hoy: {hoy}\n"
            informe += f"Hora que me acosté: {hora_acostado_real.strftime('%H:%M')}\n"
            informe += f"Hora que me levanté: {hora_despertado_str}\n"
            informe += f"Tiempo de descanso: {horas} horas y {minutos} minutos.\n"

            self.resultado_label.text = informe
            Clipboard.copy(informe)  # Copiar al portapapeles
        else:
            self.resultado_label.text = "Por favor, ingresa las horas de acostarse y despertarse."

    def calcular_tiempo_dormido(self, hora_acostado, hora_despertado):
        ahora = datetime.now()
        
        hora_acostado, minutos_acostado = map(int, hora_acostado.split(':'))
        hora_despertado, minutos_despertado = map(int, hora_despertado.split(':'))
        
        acostado = ahora.replace(hour=hora_acostado, minute=minutos_acostado, second=0, microsecond=0)
        despertado = ahora.replace(hour=hora_despertado, minute=minutos_despertado, second=0, microsecond=0)
        
        if acostado > ahora:
            acostado -= timedelta(days=1)
        
        tiempo_dormido = despertado - acostado
        return tiempo_dormido, acostado, despertado

if __name__ == '__main__':
    SleepTimeApp().run()
