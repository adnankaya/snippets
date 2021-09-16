## intro
1. Bu derste python'da debugging nasıl yapılır, temel komutlar nelerdir öğrenmeye çalışacağız.
2. Projedeki hataları ayıklarken veya projenin belirli bir parçasının nasıl çalıştığını anlamak için debugging araçlarını veya kütüphanelerini kullanabiliriz.
3. Bu videoda python pdb modülünü kullanacağız. Ayrıca python3.7+ ile beraber gelen breakpoint() modülünü de kullanabiliriz.
4. import pdb; diyerek pdb modülünü projemize dahil ediyoruz
   pdb.set_trace() diyerek debugger giriş yapıyoruz. Bunu kodunuzun herhangi bir yerine ekleyebiliriz. Böylece eklediğimiz yere bir breakpoint yerleştirmiş olur.
5. debug işlemi bittikten sonra kod içerisinde unutmamak için genelde
   import pdb; pdb.set_trace() diyerek kullanıyoruz. 
   Eğer herhangi bir kod linting(kod syntax'ına bakan, daha güzel ve okunur kod yazmaya yardımcı araç) aracı kullanıyorsanuz bu satırı gördüğünde uyarı verecektir.
6. önce p yani print komutu ile başlayalım 
   projede bulunduğumuz kod bloğundaki parametre veya değişkenlerin muhafaza ettikleri değerleri görmek için p komutunu kullanabiliriz.
7. pp(pretty print) komutu ile pretty print olarak değişken değerlerini görebiliriz.
8. s(step over) ile satır satır ilerleme gerçekleştiririz ve herhangi bir fonksiyon çağrısı varsa bu fonksiyonun içine giderek satır satır ilerleme yaparız.
9. n(next) ile satır satır ilerleme gerçekleştiririz ancak herhangi bir fonksiyon çağrısı olsa bile direkt o satırı çalıştırır.
10. c(continue) diyerek programın çalışmasını devam ettiriririz. Ancak ilk eklediğimiz pdb.set_trace() haricinde başka breakpoint noktaları da varsa program orada durur.

11. l diyerek bulunduğumuz kod bloğundaki 11 satırlık yeri ve breakpoint noktanızı görebiliriz. l start, stop diyerek belirli satır aralıklarını görebiliriz.

12. ll diyerek bulunduğunuz fonksiyona ait veya frame'e ait bütün kaynak kodu görebiliriz.

13. a diyerek bulunduğunuz fonksiyona ait parametreleri görebiliriz.

14. b satır_no diyerek debugging yaparken kodun herhangi bir yerine breakpoint koyabiliriz. aktif breakpointleri görmek için b komutu verebiliriz.
disable 1  diyerek ilk eklediğimiz breakpointi pasif hale getirebiliriz.

15. b module:satır_no diyerek istediğimiz bir modülün istediğimiz satırına breakpoint koyabiliriz.

16. pdb.run('print(f"d -> {d}")') diyerek istediğimiz bir kod ibaresini yani expression'ı çalıştırabiliriz. pdb.run() string olarak parametre alır. yani expression string olmalıdır.

17. pdb.runcall(fonksiyon_adı, param1, param2, ..) diyerek fonksiyon çağrısı yapabiliriz.

18. q(quit) diyerek debugging frame'den çıkış yaparız.

