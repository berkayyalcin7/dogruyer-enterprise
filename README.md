# dogruyer-enterprise
Corporate Consulting

###  MS ACCESS  - ODBC Bağlantısı

1- **ODBC Veri Kaynağına Access'in 64 bit sürümünü tanıtmak için MicrosoftAccessDatabaseEngine 'i bilgisayarımza kurmamız gerekiyor (Linkte Verilen 2016 -64 bit sürüm için)**
[Microsoft Database Engine İndir](https://www.microsoft.com/en-us/download/details.aspx?id=54920)

![sc1](https://user-images.githubusercontent.com/25421144/47853890-49cf9d80-ddf1-11e8-9f1e-9b4be5c608ad.png)
----------------------------------------------------------------------------------------------------------
2- **ODBC Veri Kaynağı Yöneticisi - 64 Bit (Burada MS Access Database 64 bit olarak gözükmektedir)..**
![sc2](https://user-images.githubusercontent.com/25421144/47854001-99ae6480-ddf1-11e8-8312-07c348761208.png)
--------------------------------------------------------------------------------------------------------
3- **Dosya DSN kısmından** Ekle dedikten sonra Yeni Veri Kaynağı 'nı kullanacağımız Access Driver'ı seçip **Veritabanımızı** dosya yolundan bulup seçiyoruz...
![sc2 5](https://user-images.githubusercontent.com/25421144/47854334-8c45aa00-ddf2-11e8-913e-ee1aa27a6b29.png)

![sc3](https://user-images.githubusercontent.com/25421144/47854332-89e35000-ddf2-11e8-8686-d13bda97acec.png)
--------------------------------------------------------------------------------------------------------
**4-Daha sonra Açılacak Setup Bölümünde Select ile Veritabanımızı işaretleyip işlemi tamamlıyoruz ...**
![sc4](https://user-images.githubusercontent.com/25421144/47854548-0fff9680-ddf3-11e8-9b51-672c01108d41.png)
--------------------------------------------------------------------------------------------------------
**5- Database1 ' in bulunduğu dizinin içinde ODBC bize Veri Kaynağını oluşturmuş oluyor Veri Kaynağını Not Defteri ile açıyoruz.** 
![src5](https://user-images.githubusercontent.com/25421144/47854952-3540d480-ddf4-11e8-9558-d6e0b079b34d.png)
--------------------------------------------------------------------------------------------------------
****6-Son İşlemde Veri Kaynağını Python için düzenliyoruz ...**
![sc7](https://user-images.githubusercontent.com/25421144/47855486-ccf2f280-ddf5-11e8-9740-75a50ef2100d.png)
