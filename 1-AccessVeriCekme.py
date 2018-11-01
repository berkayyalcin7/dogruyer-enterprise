
"""
ODBC Üzerinden Oluşturduğumuz Access Veri Kaynağını Python'a Entegre Edebilmek için
Python'da bulunan :
-pypyodbc (Kütüphanesinden yararlanıyoruz)..

"""
import pypyodbc

"""
 'connect' fonksiyonuyla düzenlediğimiz Veri Kaynağını giriyoruz.
"""
con=pypyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};UID=admin;UserCommitSync=Yes;Threads=3;SafeTransactions=0;PageTimeout=5;MaxScanRows=8;MaxBufferSize=2048FIL={MS Access};DriverId=25;DefaultDir=C:/Users/Dogruyer_5/Documents;DBQ=C:/Users/Dogruyer_5/Documents/Database1.accdb')

"""
Veritabanını cursor 'ın içine atıyoruz.
"""
cursor=con.cursor()

"""
Veritabanı içindeki Tablodan SQL Sorgusuyla Örnek Veri Çekme İşlemi

"""
cursor.execute('SELECT * FROM test')


""" Verileri for döngüsü içerisinde Ekrana Bastırma """
for row in cursor.fetchall():
    print(row)
