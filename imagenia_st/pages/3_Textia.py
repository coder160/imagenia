from core.controller import Page, Generator
class Textia(Page):
    def __init__(self, title:str, icon:str=None):
        super().__init__(title=title,icon=icon)
    def _init_globals(self):
        self.__hf = self.get_global(key="hf_key", default=None)
        self.__modelos = self.get_global(key="modelos_txt",default =list([]))
    def _get_hf(self):
        return self.__hf
    def _get_modelos(self):
        return self.__modelos
    def build(self):
        self._init_globals()
        self.get_body().text("Cree textos únicos hechas por Inteligencia Artificial")
        if self.check_password():
            self.get_body().success(f"¡Todo listo!\nhk-{self._get_hf()}")
            _modelo = self.get_body().selectbox("Seleccione un Modelo:",self._get_modelos())
            _prompt = self.get_body().text_area("Prompt")
            __boton = self.get_body().button("texTia")
            if __boton:
                _text = Generator(hf_key=self._get_hf(),model=_modelo).new_text(prompt=_prompt)
                self.get_body().success(_text.get_text())
        else:
            self.get_body().error("Error:\nAcceda a Configuraciones e ingrese su llave HuggingFace\n O ingrese su código secreto")
            

if __name__ == "__main__":
    Textia(title="ImaGenia",icon="🖼️").build()

    