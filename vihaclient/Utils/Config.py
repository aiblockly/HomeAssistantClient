import yaml
import os
def _parse_plain_text(basedir):
    ret=[]
    with open(os.path.join(basedir,"configuration.yaml"),mode="r")as f:
        while True:
            line=f.readline()
            if not line:
                break
            elif str(line).strip("\n"):
                ret.append(str(line).strip("\n"))
            else:
                continue
    return ret
def _add_include(basedir,tag,text):
    need_add_include = True
    for line in _parse_plain_text(basedir):
        if tag in line:
            if text in line:
                need_add_include = False
            else:
                raise FileExistsError("write all in one file  is a bad habit !")
    if need_add_include:
        if not os.path.isdir(os.path.join(basedir,"device")):
            os.makedirs(os.path.join(basedir,"device"),exist_ok=True)
        with open(os.path.join(basedir,"configuration.yaml"),mode="a+")as f:
            f.write("\n%s\n"%text)
    return need_add_include


def add_yeelight(**kwargs):
    basedir="/home/hass/.homeassistant/" if "basedir" not in kwargs.keys() else str(kwargs["basedir"])
    _add_include(basedir,"yeelight:","yeelight: !include device/yeelight.yaml")
    ip = str(kwargs["ip"])
    name = str(kwargs["name"])
    if os.path.isfile(os.path.join(basedir,"device","yeelight.yaml")):

        with open(os.path.join(basedir,"device","yeelight.yaml"),mode="r+")as f:
            d=yaml.load(f)
            if "devices" in d.keys():
                d["devices"][ip]={"name":name}
            else:
                d["devices"]={}
            if "transition"in kwargs.keys():
                d["devices"][ip]["transition"]=int(kwargs["transition"])
            if "use_music_mode"in kwargs.keys():
                d["devices"][ip]["use_music_mode"]=bool(kwargs["use_music_mode"])
            if "save_on_change"in kwargs.keys():
                d["devices"][ip]["save_on_change"]=bool(kwargs["save_on_change"])
            f.seek(0)
            f.truncate()
            yaml.dump(d,f)
    else:
        with open(os.path.join(basedir, "device", "yeelight.yaml"), mode="w")as f:
            d={}
            d["devices"][ip] = {"name": name}
            if "transition"in kwargs.keys():
                d["devices"][ip]["transition"]=int(kwargs["transition"])
            if "use_music_mode"in kwargs.keys():
                d["devices"][ip]["use_music_mode"]=bool(kwargs["use_music_mode"])
            if "save_on_change"in kwargs.keys():
                d["devices"][ip]["save_on_change"]=bool(kwargs["save_on_change"])
            yaml.dump(d, f)
def add_broadlink_rm(**kwargs):
    basedir = "/home/hass/.homeassistant/" if "basedir" not in kwargs.keys() else str(kwargs["basedir"])
    ip = str(kwargs["ip"])
    mac = str(kwargs["mac"])
    name = str(kwargs["name"])
    _add_include(basedir, "remote:", "remote: !include device/remote.yaml")
    if os.path.isfile(os.path.join(basedir,"device","remote.yaml")):

        with open(os.path.join(basedir,"device","remote.yaml"),mode="r+")as f:
            d=yaml.load(f)
            data={"platform":"broadlink","host":ip,"mac":mac,"name":name}
            d.append(data)
            f.seek(0)
            f.truncate()
            yaml.dump(d, f)
    else:
        with open(os.path.join(basedir, "device", "remote.yaml"), mode="w")as f:
            yaml.dump([{"platform":"broadlink","host":ip,"mac":mac,"name":name}],f)



if __name__=="__main__":
    print(_parse_plain_text("/home/hass/.homeassistant"))
