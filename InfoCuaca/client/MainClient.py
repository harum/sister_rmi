#Percobaan client rpyc

import rpyc

class Client():
    
    def start(self):
        print "Program Client Started!"
        self.connecting()
        
    def connecting(self):
        Client.server = rpyc.connect('localhost', 1450, config={'allow_public_attrs':True})
        kalimat = Client.server.root.say_hello()
        print kalimat
        self.getData()
        

    def getData(self):
        
        while True:
            print '\n\n==========PILIH SALAH SATU=========='
            print '0. Data Cuaca'
            print '1. Data Balai'
            print '2. Data Stasiun'
            print '3. Statistik Gempa 2012'
            print '4. Info Klimat'
            
            index = input('Masukan pilihan >> ')
            
            if index == 0 :
                print "Tekan 1 untuk mengambil seluruh ramalan cuaca untuk kota tertentu dan \ntekan 2 untuk mengambil semua ramalan cuaca "
                pilihan = input()
                print pilihan
                print "Mengambil data dari server... "
                informasiLengkap = Client.server.root.get_data(index)
                
                arrayTanggal = informasiLengkap[0]
                informasi = informasiLengkap[1]
                    
                if pilihan == 1 :  
                    print 'Masukan Kota contoh: Jepara'
                    pilihanKota = raw_input()
                    print '\n==============DATA CUACA JAWA TENGAH==============='
                    print 'Tanggal Mulai: '+arrayTanggal[0]+' Pukul '+ arrayTanggal[1]+'\n'+ 'Tanggal Akhir: '+arrayTanggal[2]+' Pukul '+ arrayTanggal[3]+'\n'
                    for baris in informasi:
                        if baris[0] == pilihanKota :
                            print 'Kota\t\t: '+baris[0]
                            print 'Balai\t\t: '+baris[1]
                            print 'Provinsi\t: '+baris[2]
                            print 'Cuaca\t\t: '+baris[3]
                            print 'Suhu Min\t: '+baris[4]
                            print 'SuhuMax\t\t: '+baris[5]
                            print 'Kelembapan Min\t: '+baris[6]
                            print 'Kelembapan Max\t: '+baris[7]
                            print 'Kecepatan Angin\t: '+baris[8]
                            print 'Arah Angin\t: '+baris[9]
                            print'\n================================'
                    
                elif pilihan==2 :
                    print '\n==============DATA CUACA==============='
                    print 'Tanggal Mulai: '+arrayTanggal[0]+' Pukul '+ arrayTanggal[1]+'\n'+ 'Tanggal Akhir: '+arrayTanggal[2]+' Pukul '+ arrayTanggal[3]+'\n'
                    for baris in informasi:
                        print 'Kota\t\t: '+baris[0]
                        print 'Balai\t\t: '+baris[1]
                        print 'Provinsi\t: '+baris[2]
                        print 'Cuaca\t\t: '+baris[3]
                        print 'Suhu Min\t: '+baris[4]
                        print 'SuhuMax\t\t: '+baris[5]
                        print 'Kelembapan Min\t: '+baris[6]
                        print 'Kelembapan Max\t: '+baris[7]
                        print 'Kecepatan Angin\t: '+baris[8]
                        print 'Arah Angin\t: '+baris[9]
                        print'\n================================'
                        
            elif index == 1 :
                
                print "Tekan 1 untuk mengambil data balai tertentu dan \ntekan 2 untuk mengambil semua data balai "
                pilihan = input()
                print pilihan
                print "Mengambil data dari server... "
                informasiLengkap = Client.server.root.get_data(index)
                
                    
                if pilihan == 1 :  
                    print 'Masukan nama balai contoh: Balai Besar Wilayah III Denpasar'
                    pilihanBalai = raw_input()
                    print '\n=============DATA BALAI================'
                    for baris in informasiLengkap:
                        if baris[0] == pilihanBalai :
                            print 'Balai\t:'+baris[0]
                            print 'Alamat\t:'+baris[1]
                            print 'Telp\t:'+baris[2]
                            print 'Fax\t:'+baris[3]
                            print 'Kepala\t:'+baris[4]
                            print '======================================'
                    
                elif pilihan==2 :
                    print '\n=============DATA BALAI================'
                    for baris in informasiLengkap:
                        print 'Balai\t:'+baris[0]
                        print 'Alamat\t:'+baris[1]
                        print 'Telp\t:'+baris[2]
                        print 'Fax\t:'+baris[3]
                        print 'Kepala\t:'+baris[4]
                        print '======================================'
                        
            elif index == 2 :
                
                print "Tekan 1 untuk mengambil data stasiun tertentu dan \ntekan 2 untuk mengambil semua data stasiun "
                pilihan = input()
                print pilihan
                print "Mengambil data dari server... "
                informasiLengkap = Client.server.root.get_data(index)
                
                    
                if pilihan == 1 :  
                    print 'Masukan Stasiun contoh: Timika: '
                    pilihanStasiun = raw_input()
                    print '\n=============DATA STASIUN================'
                    for baris in informasiLengkap:
                        if baris[0] == pilihanStasiun :
                            print 'Kota\t:'+baris[0]
                            print'Stasiun\t:'+baris[1]
                            print 'Tipe\t:'+baris[2]
                            print'Balai\t:'+baris[3]
                            #print'Alamat\t:'+baris[4]
                            print'Telp\t:'+baris[5]
                            print'Fax\t:'+baris[6]
                            print'Kepala\t:'+baris[7]
                            print'NIP\t:'+baris[8]
                            print'Mail\t:'+baris[9]
                            print'Web\t:'+baris[10]
                            print '======================================'
                    
                elif pilihan==2 :
                    print '\n=============DATA STASIUN================'
                    for baris in informasiLengkap:
                        print 'Kota\t:'+baris[0]
                        print'Stasiun\t:'+baris[1]
                        print 'Tipe\t:'+baris[2]
                        print'Balai\t:'+baris[3]
                        #print'Alamat\t:'+baris[4]
                        print'Telp\t:'+baris[5]
                        print'Fax\t:'+baris[6]
                        print'Kepala\t:'+baris[7]
                        print'NIP\t:'+baris[8]
                        print'Mail\t:'+baris[9]
                        print'Web\t:'+baris[10]
                        print '======================================'
                        
            elif index == 3 :
                
                print "Tekan 1 untuk mengambil data statistik gempa tertentu dan \ntekan 2 untuk mengambil semua data statistik gempa "
                pilihan = input()
                print pilihan
                print "Mengambil data dari server... "
                informasiLengkap = Client.server.root.get_data(index)
                
                    
                if pilihan == 1 :  
                    print 'Masukan Nomor Bulan contoh : 01'
                    pilihanBulan = raw_input()
                    print '\n=============DATA GEMPA================'
                    for baris in informasiLengkap:
                        if baris[0] == pilihanBulan :
                            print 'Bulan\t:'+baris[0]
                            print 'Jumlah\t:'+baris[1]
                            print '======================================'
                    
                elif pilihan==2 :
                    print '\n=============DATA GEMPA================'
                    for baris in informasiLengkap:
                        print 'Bulan\t:'+baris[0]
                        print 'Jumlah\t:'+baris[1]
                        print '======================================'
                        
            else:
                informasiLengkap = Client.server.root.get_data(index)
                print '\n=============DATA KLIMAT================'
                for baris in informasiLengkap:
                    print 'Tanggal\t:'+baris[0]
                    print 'Jam\t:'+baris[1]
                    print 'Subject\t:'+baris[2]
                    print 'Isi\t:'+baris[3]
                    print '======================================'

c = Client()
c.start()





