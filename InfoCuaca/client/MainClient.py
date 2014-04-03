#Percobaan client rpyc

import rpyc

class Client():
    
    def start(self):
        print "Program Client Started!"
        self.connecting()
        
    def connecting(self):
        Client.server = rpyc.connect('localhost', 1452, config={'allow_public_attrs':True})
        kalimat = Client.server.root.say_hello()
        print kalimat
        self.getData()
        

    def getData(self):
        print "Silahkan masukkan index yang dicari [0..4] : "
        index = raw_input()
        
        print "Mengambil data dari server... "
        informasiLengkap = Client.server.root.get_data(index)
        
        arrayTanggal = informasiLengkap[0]
        informasi = informasiLengkap[1]
        
        #tambahin ngeprint data

c = Client()
c.start()





