from core.controller import Page

class Home(Page):
    def __init__(self, title:str, icon:str=None):
        super().__init__(title=title,icon=icon)
    def build(self):
        self.get_body().markdown(
            """

            # Bienvenido - *imagenia*

            #### Crea **imágenes únicas** con ayuda de **Inteligencia Artificial**.

            1- Configura tu cuenta y tus estilos.

            2- Crea y descarga tus creaciones!


            """)

if __name__ == "__main__":
    Home(title="Inicio",icon="🏠").build()