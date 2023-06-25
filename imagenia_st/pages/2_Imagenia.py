from core.controller import Page, Generator
class Imagenia(Page):
    def __init__(self, title:str, icon:str=None):
        super().__init__(title=title,icon=icon)
    def _init_globals(self):
        self.__hf = self.get_global(key="hf_key", default=None)
        self.__estilos = self.get_global(key="estilos",default =dict({}))
        self.__modelos = self.get_global(key="modelos_img",default =list([]))
    def _get_hf(self):
        return self.__hf
    def _get_estilos(self):
        return self.__estilos
    def _get_modelos(self):
        return self.__modelos
    def build(self):
        self._init_globals()
        self.get_body().text("Cree imágenes únicas hechas por Inteligencia Artificial")
        if self.check_password():
            self.get_body().success(f"¡Todo listo!\nhk-{self._get_hf()}")
            _modelo = self.get_body().selectbox("Seleccione un Modelo:",self._get_modelos())
            _opcion = self.get_body().selectbox("Seleccione un Estilo:",self._get_estilos().keys())
            _prompt = self.get_body().text_area("Prompt")
            _estilo = self._get_estilos().get(_opcion) if "CUSTOM" not in _opcion.upper() else self.get_body().text_input("Estilo")
            __boton = self.get_body().button("imaGenia")
            if __boton:
                self.get_body().write(f"Utilizando estilo: {_estilo}")
                _img = Generator(hf_key=self._get_hf(),model=_modelo).new_image(prompt=_prompt,estilo=_estilo)
                self.get_body().image(_img.get_img(),caption=_prompt)
        else:
            self.get_body().error("Error:\nAcceda a Configuraciones e ingrese su llave HuggingFace\n O ingrese su código secreto")
            

if __name__ == "__main__":
    Imagenia(title="ImaGenia",icon="🖼️").build()

    