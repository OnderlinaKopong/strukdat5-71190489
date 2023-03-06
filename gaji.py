class Karyawan:
    def __init__(self, nama,umur):
        self._nama = nama
        self._umur = umur
        self._jenisKelamin = None
        self._UpahPerHari = None

    def setjenisKelamin(self,jenisKelamin):
        self._jenisKelamin = jenisKelamin

    def setUpahPerHari(self, UpahPerHari):
        self._UpahPerHari = UpahPerHari
        
    def printInfo(self):
        print("============Info============")
        print("Nama : \t{}".format(self._nama))
        print("Umur : \t{}".format(self._umur))
        print("Jenis Kelamin : \t{}".format(self._jenisKelamin))
        print("Upah Per Hari : \t{}".format(self._UpahPerHari))

    def hitumgGajiBulanan(self, jumlahHari):
        if self._UpahPerHari is None:
            print("ERROR! Upah per hari belum di inputkan")
        else:
            gajiBulanan = self._UpahPerHari * jumlahHari
            print("Gaji Bulan ini : Rp\t{}".format(gajiBulanan))


    

orang1 = Karyawan("Hanif", 90)
orang1.printInfo()
orang2 = Karyawan("Sindu", 190)
orang2.setjenisKelamin("Laki-laki")
orang2.setUpahPerHari(30000)
orang2.printInfo
orang1.hitumgGajiBulanan(28)
orang2.hitumgGajiBulanan(30)
