METHOD = "get"
PATH_GET_CONFIG = "/api/config"
PATH_GET_BASEINFO = "/api/discovery_info"
PATH_GET_EVENTS = "/api/events"
PATH_GET_SERVICE="/api/services"
PATH_GET_HISTORY_PERIOD = "/api/history/period/"
PATH_GET_STATES="/api/states"
from vihaclient.Core.RequestFactory import getResponse, urlgen


def getConfig(key: str, domain: str, port=8123, tls=False,**kwargs):
    url = urlgen(domain=domain, port=port, path=PATH_GET_CONFIG, enable_tls=tls)
    return getResponse(url, key, method=METHOD)


def getBaseInfo(key: str, domain: str, port=8123, tls=False,**kwargs):
    url = urlgen(domain=domain, port=port, path=PATH_GET_BASEINFO, enable_tls=tls)
    return getResponse(url, key, method=METHOD)


def getEvents(key: str, domain: str, port=8123, tls=False,**kwargs):
    url = urlgen(domain=domain, port=port, path=PATH_GET_EVENTS, enable_tls=tls)
    return getResponse(url, key, method=METHOD)

def getService(key: str, domain: str, port=8123, tls=False,**kwargs):
    url = urlgen(domain=domain, port=port, path=PATH_GET_SERVICE, enable_tls=tls)
    return getResponse(url, key, method=METHOD)

def getHistoryPeriod(key: str, domain: str, port=8123, tls=False,**kwargs):
    time="" if "time" not in kwargs.keys() else "/"+str(kwargs["time"])
    payload=None if "filter_entity_id" not in kwargs.keys() else {"filter_entity_id":str(kwargs["filter_entity_id"])}
    url = urlgen(domain=domain, port=port, path=PATH_GET_SERVICE, enable_tls=tls)
    url=url+time
    return getResponse(url, key, method=METHOD,payload=payload)

def getStates(key: str, domain: str, port=8123, tls=False,**kwargs):
    entity_id = "" if "entity_id" not in kwargs.keys() else "/"+str(kwargs["entity_id"])
    url = urlgen(domain=domain, port=port, path=PATH_GET_STATES, enable_tls=tls)+entity_id
    return getResponse(url, key, method=METHOD)


