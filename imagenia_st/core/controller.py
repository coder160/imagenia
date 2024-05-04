import streamlit as BaseBuilder
import requests
import json
class Generator():
    def __init__(self, hf_key:str, model:str):
        self.__url = str(f"https://api-inference.huggingface.co/models/{model}")
        self.__headers = {"Authorization": f"Bearer {hf_key}"}
    def get_url(self)->str:
        return self.__url
    def get_headers(self):
        return self.__headers
    def get_googleFlan(self)->str:
        return str(self.get_base()+"google/flan-t5-xxl")
    def new_image(self,prompt:str,estilo:str):
        self.__image = requests.post(url=self.get_url(),
                                     headers=self.get_headers(), 
                                     json={"inputs": str(prompt + estilo)}).content
        return self
    def get_img(self):
        import io
        return io.BytesIO(self.__image)
    def new_text(self, prompt:str):
        self.__text = requests.post(url=self.get_url(),
                                    headers=self.get_headers(), 
                                    json={"inputs": str(prompt)}).json()
        return self
    def get_text(self):
        return self.__text
    



class Page():
    def __init__(self, title:str, icon:str=None):
        self.__ = BaseBuilder
        self.__.set_page_config(page_title=title, page_icon=icon)
        self.__.title(f"# {icon} {title}")
        self.__body = self.__.container()
        self.set_global(key="modelos_img",
                        value=["prompthero/openjourney-v4",
                               "prompthero/openjourney",
                               "stabilityai/stable-diffusion-2-1-base",
                               "stabilityai/stable-diffusion-2-1",
                               "runwayml/stable-diffusion-v1-5",
                              "stabilityai/stable-diffusion-xl-base-1.0",])
        self.set_global(key="modelos_txt",
                        value=["google/flan-t5-xxl",
                               "bigcode/santacoder",
                               "tiiuae/falcon-7b-instruct",
                               "decapoda-research/llama-7b-hf",
                               "bigscience/bloom-560m",
                               "gpt2",
                               "Helsinki-NLP/opus-mt-ar-en",
                               "facebook/bart-large-cnn"])
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
            __estilos = self.get_global(key="estilos",default =dict({"CUSTOM":""}))
            _secretos = json.loads(str(self.page().secrets["PRIVATE_CONFIG"]["ESTILOS_BASE"]))
            for _k,_v in _secretos.items():
                __estilos[_k] = _v
            self.set_global(key="estilos",value=__estilos)
            del self.page().session_state["password"]
            del self.page().session_state["username"]
        else:
            self.page().session_state["password_correct"] = False
