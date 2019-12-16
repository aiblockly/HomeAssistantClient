METHOD = "post"
PATH_POST_STATES = "/api/states/"
PATH_POST_SERVICE="/api/services/<domain>/<service>"
from vihaclient.Core.RequestFactory import getResponse,urlgen
def postStates(key: str, domain: str,payload:dict, port=8123, tls=False,**kwargs):
    if "entity_id" not in kwargs.keys():
        raise AttributeError("Requried Arg:entity_id")
    url = urlgen(domain=domain, port=port, path=PATH_POST_STATES, enable_tls=tls)+str(kwargs["entity_id"])
    return getResponse(url, key, method=METHOD,payload=payload)

def postService(key: str, domain: str,payload:dict, port=8123, tls=False,**kwargs):
    if "service_domain" not in kwargs.keys():
        raise AttributeError("Requried Arg:service_domain")
    else:
        service_domain=str(kwargs["service_domain"])
    if "service" not in kwargs.keys():
        raise AttributeError("Requried Arg:service")
    else:
        service_name=str(kwargs["service"])
    url = urlgen(domain=domain, port=port,
                 path=PATH_POST_SERVICE.replace("<domain>",service_domain).replace("<service>",service_name), enable_tls=tls)
    return getResponse(url, key, method=METHOD,payload=payload)

