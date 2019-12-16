#面向对象的调用，不要再写一大坨的Token了
from vihaclient import Client
#简单粗暴的调用方式，从Core里面直接调方法
from vihaclient.Core.method_get import *
from vihaclient.Core.method_post import *
#如果你和自己过不去，你可以用下面两个函数
#from vihaclient.Core.RequestFactory import getResponse,urlgen
#打算继续填坑的部分,包含了一些配置文件生成方法
#import vihaclient.Utils.Config
import json
import sys
payload={
    "entity_id": "light.yeelight_color1_286c071130ed"
}
d=postService(key="YOUR_PASSWD",
              domain="192.168.1.176",payload=payload,service_domain="light",service="toggle")

json.dump(d,sys.stdout,indent=4)
d=getConfig(key="YOUR_PASSWD",
              domain="192.168.1.176")
json.dump(d,sys.stdout,indent=4)
c=Client(key="YOUR_PASSWD",ip="192.168.1.176")
print(c.get_all_domain())
c.light(operation="toggle",entity="light.yeelight_color1_286c071130ed")
json.dump(c.weather(entity="weather.jia"),sys.stdout,indent=4)