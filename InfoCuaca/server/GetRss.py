'''
Created on Apr 2, 2014

@author: Herleeyandi
'''

import urllib
from elementtree.ElementTree import parse

class Cuaca():
    daftarUrl = []
    
    def cekTes(self):
        return "Mencoba mendapatkan data cuaca!"
    
    def setUrl(self):
        #bisa ditambah sesuai kebutuhan
        Cuaca.daftarUrl.append('http://data.bmkg.go.id/propinsi_14_1.xml')
        Cuaca.daftarUrl.append('http://data.bmkg.go.id/propinsi_14_1.xml')
        Cuaca.daftarUrl.append('http://data.bmkg.go.id/propinsi_14_1.xml')
        Cuaca.daftarUrl.append('http://data.bmkg.go.id/propinsi_14_1.xml')
        Cuaca.daftarUrl.append('http://data.bmkg.go.id/propinsi_14_1.xml')
    
    def getRss(self, index):
        if index>4:
            index=4
            
        rss = parse(urllib.urlopen(Cuaca.daftarUrl[index])).getroot()
        arrayTanggal = []
        for tanggal in rss.findall('Tanggal'):    
            mulai = tanggal.find('Mulai').text
            arrayTanggal.append(mulai)
            mulaiPukul = tanggal.find('MulaiPukul').text
            arrayTanggal.append(mulaiPukul)
            sampai = tanggal.find('Sampai').text
            arrayTanggal.append(sampai)
            sampaiPukul = tanggal.find('SampaiPukul').text
            arrayTanggal.append(sampaiPukul)
            print 'Tanggal Mulai: '+mulai+' Pukul '+ mulaiPukul+'\n'+ 'Tanggal Akhir: '+sampai+' Pukul '+ sampaiPukul+'\n'


        informasi=[]
        for isi in rss.findall('Isi/Row'):
            kota = isi.find('Kota').text
            balai = isi.find('Balai').text
            provinsi = isi.find('Propinsi').text
            cuaca = isi.find('Cuaca').text
            suhuMin = isi.find('SuhuMin').text
            suhuMax = isi.find('SuhuMax').text
            kelembapanMin = isi.find('KelembapanMin').text
            kelembapanMax = isi.find('KelembapanMax').text
            kecepatanAngin = isi.find('KecepatanAngin').text
            arahAngin = isi.find('ArahAngin').text
            informasi.append([kota,balai,provinsi,cuaca,suhuMin,suhuMax,kelembapanMin,kelembapanMax,kecepatanAngin,arahAngin])
           
            print 'Kota\t\t: '+kota+'\n'+'Balai\t\t: '+balai+'\n'+'Provinsi\t: '+provinsi+'\n'+'Cuaca\t\t: '+cuaca+'\n'+'Suhu Min\t: '+suhuMin+'\n'+'SuhuMax\t\t: '+suhuMax+'\n'+'Kelembapan Min\t: '+kelembapanMin+'\n'+'Kelembapan Max\t: '+kelembapanMax+'\n'+'Kecepatan Angin\t: '+kecepatanAngin+'\n'+'Arah Angin\t: '+arahAngin+'\n'
            print'\n================================'
        
        informasiTotal = []
        informasiTotal.append(arrayTanggal)
        informasiTotal.append(informasi)
        
        return informasiTotal