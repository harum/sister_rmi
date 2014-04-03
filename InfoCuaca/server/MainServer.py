#Percobaan server rpyc

import rpyc
import GetRss
from elementtree.ElementTree import parse

class MyService(rpyc.Service):
    def exposed_say_hello(self):
        return "Anda berhasil terhubung dengan pusat Cuaca!"
    
    def exposed_get_data(self, index):
        data = GetRss.Cuaca()
        data.setUrl()
        a = data.getRss(index)
        return a

print "Program Server Started!"
b = GetRss.Cuaca()
b.setUrl()
koko = b.getRss(1)

from rpyc.utils.server import ThreadedServer
t = ThreadedServer(MyService, port = 1452)
t.start()
