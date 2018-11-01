
#ODBC ÜZERİNDEN VERİ KAYNAĞINI ÇEKEBİLMEK İÇİN (pyppyodbc) kütüphanesini import ediyoruz.
import pypyodbc




con=pypyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048FIL={MS Access};DriverId=25;DefaultDir=C:/Users/Dogruyer_5/Documents;DBQ=C:/Users/Dogruyer_5/Documents/Database1.accdb')


cursor=con.cursor()

#Access ' te bulunan 'test' tablosundaki verileri çekme işlemi
cursor.execute('SELECT * FROM test')



#verileri döngü içerisinde Gösteriyoruz.
for row in cursor.fetchall():
    print(row)
