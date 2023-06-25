from core.controller import Page
import json
class Settings(Page):
    def __init__(self, title:str, icon:str=None):
        super().__init__(title=title,icon=icon)
    def _init_globals(self):
        self.__hf = self.get_global(key="hf_key", default=None)
        self.__estilos = self.get_global(key="estilos",default =dict({"CUSTOM":""}))
        self.__opciones = self.get_global(key="opciones",default =list([]))
    def _get_hf(self):
        return self.__hf
    def _get_estilos(self):
        return self.__estilos
    def _get_opciones(self):
        return self.__opciones
    def _key_section(self):
        __hf = self._get_hf()
        self.get_body().subheader("HuggingFace Key")
        self.get_body().write("Agregue su api-key de HuggingFace para hacer uso de la aplicación:")
        __hf_input = self.get_body().text_input("HuggingFace-Key:",value=__hf)
        __boton_hf = self.get_body().button("Actualizar HuggingFace-Key", use_container_width=True, type="primary")
        if __boton_hf:
            self.set_global(key="hf_key",value= __hf_input)
            self.get_body().success(f"¡Llave HF Actualizada!\n{__hf_input}")
    def _style_section(self):
        __estilos = self._get_estilos()
        self.get_body().subheader("Estilos")
        self.get_body().write("Importe o Exporte sus Estilos desde un archivo .CSV")
        _import, _export= self.get_body().columns(spec=2)

        _uploaded_file = _import.file_uploader("Importar Estilos", label_visibility="collapsed")
        if _uploaded_file is not None:
            _json_data = json.loads(_uploaded_file.getvalue().decode("utf-8"))
            for _k,_v in _json_data.items():
                __estilos[_k] = _v
            self.set_global(key="estilos",value=__estilos)

        if _export.download_button('Exportar Estilos', json.dumps(self._get_estilos()), mime="application/json",use_container_width=True):
            self.page().balloons()
            print(str(self._get_estilos()))
        

        self.get_body().write("O Agregue manualmente sus Estilos:")
        _new_style, _submit = self.get_body().columns(spec=2)
        _new_tag = _new_style.text_input("Nuevo Estilo", label_visibility="collapsed")
        if _submit .button("Agregar Estilo",use_container_width=True):
            __estilos[_new_tag] = str()
            self.set_global(key="estilos",value=__estilos)
        for _k,_v in self._get_estilos().items():
            __estilos[_k] = self.get_body().text_input(f"Descripción de {_k}:",value=_v)
            self.set_global(key="estilos",value=__estilos)
    def build(self):
        self._init_globals()
        self._key_section()
        self._style_section()
        if self.check_password():
            self.get_body().success("¡Bienvenido!")
        
if __name__ == "__main__":
    Settings(title="Configuraciones",icon="⚙️").build()