import yaml
from yamlinclude import YamlIncludeConstructor
from .Core.method_post import postService
from .Core.method_get import getStates,getConfig,getService
import os,inspect

SERVICE_DOMAIN_LIST=["local","light","homeassistant"]
def getConf(basedir):
    YamlIncludeConstructor.add_to_loader_class(loader_class=yaml.FullLoader, base_dir=basedir)
    f = open('/home/hass/.homeassistant/configuration.yaml', encoding="utf-8")
    conf = yaml.load(f)
    return conf
def _get_current_function_name():
    return inspect.stack()[1][3]

def _api_service_call_protype(self, operation: str, entity: str, **kwargs):
    service_domain = _get_current_function_name()
    print(service_domain)
    payload = {"entity_id": entity}
    if len(kwargs.keys()): payload.update(kwargs)
    return postService(key=self.__key, payload=payload, domain=self.__ip, service_domain=service_domain,
                        service=operation)

class Client(object):
    def __init__(self,**kwargs):
        base_dir="/home/hass/.homeassistant/" if "confdir" not in kwargs.keys() else os.path.realpath(str(kwargs["confdir"]))
        self.__ip = "127.0.0.1" if "ip" not in kwargs.keys() else str(kwargs["ip"])
        self.__port = 8123 if "port" not in kwargs.keys() else int(kwargs["port"])
        self.__tls = False if "tls" not in kwargs.keys() else bool(kwargs["tls"])
        self.__key=None
        if "key" in kwargs.keys():
            self.__key=str(kwargs["key"])
        else:
            conf = getConf(basedir=base_dir)
            if "homeassistant" in conf.keys() and "auth_providers" in conf["homeassistant"].keys():
                for provider in conf["homeassistant"]["auth_providers"]:
                    if provider["type"]=="legacy_api_password":
                        self.__key=str(provider["api_password"])
        if not self.__key:
            raise RuntimeError("You should put an longtime key in kwargs['key'] or using legacy_api_password in config")


    def get_all_domain(self):
        ret=[]
        for domain in  getService(key=self.__key,domain=self.__ip):
            ret.append(domain["domain"])
        return ret

    def get_state(self,entity:str):
        return getStates(key=self.__key,domain=self.__ip,port=self.__port,tls=self.__tls,entity_id=entity)



    def light(self,operation:str,entity:str):
        service_domain="light"
        payload={"entity_id": entity}
        return postService(key=self.__key,payload=payload,domain=self.__ip,service_domain=service_domain,service=operation)

    def homeassistant(self,operation:str,entity:str):
        service_domain = "homeassistant"
        payload = {"entity_id": entity}
        return postService(key=self.__key, payload=payload, domain=self.__ip, service_domain=service_domain,
                           service=operation)

    def lock(self,operation:str,entity:str,**kwargs):
        service_domain = _get_current_function_name()
        payload = {"entity_id": entity}
        if len(kwargs.keys()):payload.update(kwargs)
        return postService(key=self.__key, payload=payload, domain=self.__ip, service_domain=service_domain,
                           service=operation)

    def switch(self,operation:str,entity:str,**kwargs):
        service_domain = _get_current_function_name()
        payload = {"entity_id": entity}
        if len(kwargs.keys()):payload.update(kwargs)
        return postService(key=self.__key, payload=payload, domain=self.__ip, service_domain=service_domain,
                           service=operation)

    def remote(self,operation:str,entity:str,**kwargs):
        service_domain = _get_current_function_name()
        payload = {"entity_id": entity}
        if len(kwargs.keys()):payload.update(kwargs)
        return postService(key=self.__key, payload=payload, domain=self.__ip, service_domain=service_domain,
                           service=operation)

    def weather(self,entity:str,**kwargs):
        return getStates(key=self.__key,domain=self.__ip,port=self.__port,tls=self.__tls,entity_id=entity)["attributes"]





