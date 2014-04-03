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
        Cuaca.daftarUrl.append('http://data.bmkg.go.id/alamatbalai.xml')
        Cuaca.daftarUrl.append('http://data.bmkg.go.id/alamatstasiun_NEW.xml')
        Cuaca.daftarUrl.append('http://data.bmkg.go.id/statistikblngempa2012.xml')
        Cuaca.daftarUrl.append('http://data.bmkg.go.id/warningklimat.xml')
    
    def getRss(self, index):
        if index>4:
            index=4
        
        if index == 0 :    
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
        
        elif index == 1 :
            rss = parse(urllib.urlopen(Cuaca.daftarUrl[index])).getroot()
            arrayBalai = []
            for row in rss.findall('Row'):    
                balai = row.find('Balai').text
                alamat = row.find('Alamat').text
                telp = row.find('telp').text
                fax = row.find('fax').text
                kepalaBalai = row.find('kepalabal').text
                arrayBalai.append([balai,alamat,telp,fax,kepalaBalai])
                print 'Balai\t:'+balai+'\nAlamat\t:'+alamat+'\nTelp\t:'+telp+'\nFax\t:'+fax+'\nKepala\t:'+kepalaBalai
                print '======================================'
            
            return arrayBalai
        
        elif index == 2 :
            rss = parse(urllib.urlopen(Cuaca.daftarUrl[index])).getroot()
            arrayStasiun = []
            for row in rss.findall('Row'):    
                kota = row.find('Kota').text
                stasiun = row.find('Stasiun').text
                tipe = row.find('Tipe').text
                balai = row.find('Balai').text
                alamat = row.find('Alamat').text
                telp = row.find('telp').text
                fax = row.find('fax').text
                kepalaStasiun = row.find('kepalasta').text
                nip = row.find('nip').text
                mail = row.find('mail').text
                web = row.find('web').text
                arrayStasiun.append([kota,stasiun,tipe,balai,alamat,telp,fax,kepalaStasiun,nip,mail,web])
                print 'Kota\t:'+kota
                print'Stasiun\t:'+stasiun
                print 'Tipe\t:'+tipe
                print'Balai\t:'+balai
                #print'Alamat\t:'+alamat
                print'Telp\t:'+telp
                print'Fax\t:'+fax
                print'Kepala\t:'+kepalaStasiun
                print'NIP\t:'+nip
                print'Mail\t:'+mail
                print'Web\t:'+web
                print '======================================'
            return arrayStasiun
        
        elif index==3:
            rss = parse(urllib.urlopen(Cuaca.daftarUrl[index])).getroot()
            arrayGempa = []
            for row in rss.findall('gempa'):    
                bulan = row.find('Bulan').text
                jumlah = row.find('Jumlah').text
                arrayGempa.append([bulan,jumlah])
                print 'Bulan\t:'+bulan+'\nJumlah\t:'+jumlah
                print '======================================'               
            return arrayGempa
        
        else :
            rss = parse(urllib.urlopen(Cuaca.daftarUrl[index])).getroot()
            arrayKlimat = []
            for row in rss.findall('Warning'):    
                tanggal = row.find('Tanggal').text
                jam = row.find('Jam').text
                subject = row.find('Subject').text
                isi = row.find('Isi').text
                arrayKlimat.append([tanggal,jam,subject,isi])
                print 'Tanggal\t:'+tanggal+'\nJam\t:'+jam+'\nSubject\t:'+subject+'\nIsi\t:'+isi
                print '======================================'
            return arrayKlimat