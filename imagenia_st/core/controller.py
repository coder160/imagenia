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
    


        