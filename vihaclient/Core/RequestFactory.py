import requests
import json
def urlgen(domain,port,path,enable_tls=False):
    if enable_tls:
        if port==443:
            return "https://"+domain+path
        else:
            return "https://" + domain+":%s"%str(port) + path
    else:
        if port==80:
            return "http://"+domain+path
        else:
            return "http://" + domain+":%s"%str(port) + path
def getResponse(url,key,payload=None,method="get"):
    headers = {
        'Authorization': 'Bearer %s'%str(key),
        'content-type': 'application/json',
    }
    if payload:
        if method.lower() == "get":
            r = requests.get(url, headers=headers, data=json.dumps(payload))
        elif method.lower() == "post":
            r = requests.post(url, headers=headers, data=json.dumps(payload))
        else:
            raise AttributeError("method not supoort")
    else:
        if method.lower() == "get":
            r = requests.get(url, headers=headers)
        elif method.lower() == "post":
            r = requests.post(url, headers=headers)
        else:
            raise AttributeError("method not supoort")
    #print(r.text)
    return r.json()


