from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty, Clock
from datetime import datetime, timedelta
from kivy.core.clipboard import Clipboard

def calcular_tiempo_dormido(hora_acostado, minutos_acostado, hora_despertado, minutos_despertado):
    ahora = datetime.now()
    
    hora_acostado = int(hora_acostado)
    minutos_acostado = int(minutos_acostado)
    hora_despertado = int(hora_despertado)
    minutos_despertado = int(minutos_despertado)
    
    acostado = ahora.replace(hour=hora_acostado, minute=minutos_acostado, second=0, microsecond=0)
    despertado = ahora.replace(hour=hora_despertado, minute=minutos_despertado, second=0, microsecond=0)
    
    if acostado > ahora:
        acostado -= timedelta(days=1)
    
    tiempo_dormido = despertado - acostado
    return tiempo_dormido


class BoxLayoutExample(BoxLayout):
    acostado_text = StringProperty("")
    despertado_text = StringProperty("")
    informe_text = StringProperty("")

    def guardar_informe(self):
        hora_acostado = self.ids.acostado_horas.text
        minutos_acostado = self.ids.acostado_minutos.text
        hora_despertado = self.ids.despertado_horas.text
        minutos_despertado = self.ids.despertado_minutos.text

        if hora_acostado and minutos_acostado and hora_despertado and minutos_despertado:
            tiempo_dormido = calcular_tiempo_dormido(hora_acostado, minutos_acostado, hora_despertado, minutos_despertado)
            horas = int(tiempo_dormido.total_seconds() // 3600)
            minutos = int((tiempo_dormido.total_seconds() % 3600) // 60)

            # Configurar el estado de los check boxes según las condiciones
            self.ids.descansar_checkbox.active = 6 < horas < 9
            self.ids.acostarse_checkbox.active = (22 <= int(hora_acostado) <= 23 or 0 <= int(hora_acostado) <= 2) and int(minutos_acostado) <= 30

            self.ids.despertar_checkbox.active = 5 <= float(hora_despertado) <= 8.5

            informe = f"\nDESCANSO\nFecha de hoy: {datetime.now().strftime('%Y-%m-%d')}\n"
            informe += f"Hora que me acosté: {hora_acostado}:{minutos_acostado}\n"
            informe += f"Hora que me levanté: {hora_despertado}:{minutos_despertado}\n"
            informe += f"Tiempo de descanso: {horas} horas y {minutos} minutos.\n"

            with open("informe_descanso.txt", "w") as archivo:
                archivo.write(informe)

            # Copiar al portapapeles
            Clipboard.copy(informe)

            self.informe_text = informe



    def actualizar_informe(self, dt):
        self.informe_text = ""

class MainApp(App):
    def build(self):
        root = BoxLayoutExample()
        Clock.schedule_once(root.actualizar_informe, 0)
        return root

if __name__ == '__main__':
    MainApp().run()
