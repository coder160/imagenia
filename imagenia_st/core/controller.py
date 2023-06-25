import streamlit as BaseBuilder
class Generator():
    def __init__(self, hf_key:str):
        self.__url = "https://api-inference.huggingface.co/models/prompthero/openjourney-v4"
        self.__headers = {"Authorization": f"Bearer {hf_key}"}
    def set_prompt(self,prompt:str,estilo:str):
        self.__json = {"inputs": str(prompt + estilo)}
        return self
    def get_url(self):
        return self.__url
    def get_headers(self):
        return self.__headers
    def get_json(self):
        return self.__json
    def new_image(self):
        import requests
        self.__image = requests.post(url=self.get_url(),
                                     headers=self.get_headers(), 
                                     json=self.get_json()).content
        return self
    def get(self):
        import io
        return io.BytesIO(self.__image)

class Page():
    def __init__(self, title:str, icon:str=None):
        self.__ = BaseBuilder
        self.__.set_page_config(page_title=title, page_icon=icon)
        self.__.title(f"# {icon} {title}")
        self.__body = self.__.container()
        self.set_global(key="reset_opciones",
                        value=["SURREALISTA","ACUARELA","CARTOON","ANIME",
                               "RETRATO","FANTASY","CYBERPUNK","ABSTRACT","CUSTOM"])
    def page(self):
        return self.__
    def get_body(self):
        return self.__body
    def set_global(self, key:str, value):
        self.page().session_state[key] = value
    def get_global(self,key:str,default=None):
        return self.page().session_state.get(key, default)
    @BaseBuilder.cache_data
    def convert_dataframe(_self,df):
        return df.to_csv(index=False).encode('utf-8')
    def check_password(self):
        if "password_correct" not in self.page().session_state:
            self.page().sidebar.subheader("# 👨‍💻 Secret Code!")
            self.page().sidebar.write("¡Ingresa tu Código Secreto y desbloquea todas las funciones!")
            self.page().sidebar.text_input("Username", on_change=None, key="username")
            self.page().sidebar.text_input("Password", type="password", on_change=self.password_entered, key="password")
            return False
        elif not self.page().session_state["password_correct"]:
            self.page().sidebar.text_input("Username", on_change=self.password_entered, key="username")
            self.page().sidebar.text_input("Password", type="password", on_change=self.password_entered, key="password")
            self.page().sidebar.error("😕 Contraseña incorrecta")
            return False
        else:
            self.page().sidebar.success("👨‍💻 Conectado")
            return True
    def password_entered(self):
        if (self.page().session_state["username"] in self.page().secrets["passwords"]
            and self.page().session_state["password"] == self.page().secrets["passwords"][self.page().session_state["username"]]):
            self.page().session_state["password_correct"] = True
            self.page().session_state["hf_key"] = self.page().secrets["PRIVATE_CONFIG"]["HUGGINGFACE_KEY"]
            self.page().session_state["estilos"] = self.page().secrets["PRIVATE_CONFIG"]["ESTILOS_BASE"]
            del self.page().session_state["password"]
            del self.page().session_state["username"]
        else:
            self.page().session_state["password_correct"] = False
