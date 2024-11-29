# NVDA için Kişi Yöneticisi

* **Yazar**: Edilberto Fonseca <edilberto.fonseca@outlook.com>
* **Oluşturulma Tarihi**: 11/04/2024
* **Lisans**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## giriş

NVDA Kişi Yöneticisi Eklentisine hoş geldiniz! Bu, görme engelli kişilerin kişi listelerini daha kolay ve verimli bir şekilde yönetmelerine yardımcı olmak için özel olarak tasarlanmış bir eklentidir. Eklentimiz ile kişi ekleyebilir, düzenleyebilir ve silebilirsiniz. Ayrıca isim ile kişi bilgilerini hızlı ve basit bir şekilde arayabilirsiniz. Ek olarak, kişi listenizi paylaşabilmeniz veya başka bir cihaza taşıyabilmeniz için size dışa ve içe aktarma olanağı da sağlıyoruz. NVDA'nın Kişi Yöneticisi Eklentisinin kullanımı kolaydır ve sezgisel bir arayüz sunar, bu da onu kişi listelerini verimli bir şekilde yönetmesi gereken herkes için ideal bir seçim haline getirir.

## Kurulum

NVDA'da Kişi Yöneticisi Eklentisini kurmak için adım adım talimatlar:

1. Eklenti kurulum dosyasını [Kişi Yöneticisi](https://github.com/EdilbertoFonseca/contactManager) indirin.
   **Not**: Eklenti mağazadan indirilirse kurulum otomatik olarak gerçekleşir. Aksi halde aşağıdaki talimatları izleyin.
2. İndirdiğiniz Eklenti dosyası üzerinde enter tuşuna basın.
3. Eklentiyi yüklemek için ekrandaki talimatları izleyin.
4. NVDA'yı yeniden başlatın.
5. **Kurulumu kontrol edin**:Ayarlar menüsünü açmak için "NVDA + N" tuşlarına basın ve Eklentiler listesinde NVDA İçin Kişi Yöneticisi Eklentisinin listelenip listelenmediğini kontrol edin.
Artık Kişi Yöneticisi Eklentisini kullanmaya ve kişilerinizi doğrudan NVDA'dan kaydetmeye hazırsınız. Nasıl kullanılacağı ve ihtiyaçlarınıza göre nasıl özelleştirileceği hakkında ek bilgi için Eklentinin belgelerine baktığınızdan emin olun.

## Ayarlar

Tercihler menüsünde, ayarlar iletişim kutusunda NVDA için Kişi Yöneticisi öğesini seçin. Varsayılan olarak işaretli olmayan aşağıdaki seçenekleri yapılandırabilirsiniz:

1. Telefon alanları için maske ekleyin:
Bu başlık altında, iki yazma alanı bulunur. İlk yazma alanı cep telefonu ve ikinci alan da sabit hat için kullanılır.
Telefon mumaramızın rehberde görünmesini istediğimiz şekilde # diyez işareti ekleyerek numara görüntülenme şeklini yapılandırmış oluruz.
Örneğin: (####) ### ### ## ## şeklinde yazıp ayar penceresini enter ile kapattığımızda, yazdığımız numara:
(0090) 512 345 67 89
Şeklinde görünecektir.
2. Tüm rehberi silme seçeneğini göster, işaretlenmemiş onay kutusu. Alt+r.
etkinleştirildiğinde, ajandanın tüm içeriğinin silinmesine izin verir.
3. CSV dosyasını içe aktar düğmesini göster, onay kutusu işaretli değil. Alt+c.
CSV dosyalarının içe aktarılmasına izin verir. Not: Tüm alanlar Kişi Yöneticisiyle uygun olmalıdır.
4. CSV dosyasını dışa aktar düğmesini göster, onay kutusu işaretli değil. Alt+c.
Tüm telefon defteri kişilerini bir csv dosyasına kaydeder.
5. Ajanda dosyalarının yolu.
   Veritabanı için varsayılandan farklı bir dizin seçmenizi veya eklemenizi sağlar.

## kullanım

Kişi Yöneticisine iki şekilde erişebilirsiniz

1. Windows+Alt+L kısayolunu kullanabilirsiniz.
2. NVDA menüsü>Araçlar>Kişi Yöneticisi alt menüsünden Kişi listesi.

eklentinin ana penceresine erişebileceksiniz. Bu pencerede kişileri kaydedebilir, düzenleyebilir, kaldırabilir ve arayabilirsiniz. Ayrıca csv'yi içe aktarma, csv'yi dışa aktarma ve tüm kayıtları silme seçeneklerine sahiptir. Bu üç seçenek varsayılan olarak devre dışıdır.

### Yeni bir kişi kaydetme ###

Yeni bir kişi kaydetmek için:

1. NVDA menüsü>Araçlar>Kişi Yöneticisi>Kişi Listesi'ne erişin. veya kısayolla (windows+Alt+L);
2. Kişi Listesi penceresinde, yeni bir kişi eklemek için Alt+N tuşlarına basın.
3. Yeni Kişi penceresinde, tüm alanları doldurun, kaydetmek için Alt+T,, ve kaydetmeden çıkmak için Alt+L tuşlarına basın;

### Bir kişiyi düzenleme

Bir kişiyi düzenlemek için:

1. Listeden bir kişi seçin;
2. ALT+E'ye basın;

İsim alanına odaklanan düzenleme penceresi açılacaktır. Sadece düzenleyin ve değişiklikleri kaydetmek için ALT+T'ye veya iptal etmek için ALT+L'ye basın.

### Arama

Kişi Listesi penceresinde, belirli bir kişiyi bulmak için arama alanını kullanabilirsiniz.
Alanlara göre arama yapabilirsiniz:

* İsim;
* Cep telefonu;
* sabit hat;
* E-posta.

Alanı seçtikten sonra, arama öğesini yazın ve arama sonucunu listede görüntüleyecek olan ALT+A kısayoluna basın. Hiçbir sonuç bulunamazsa, ALT+Y veya F5 kısayolunu kullanarak yenileyin.

## İpuçları ve Kısayollar

### Kişi Listesi penceresi:

* **Ara Alt+A**
* **Düzenle Alt+e. F2 tuşuna da bsabilirsiniz.**
* **Yeni Alt+n**
* **Kaldır Alt+r**
* **Yenile düğmesi Alt+Y**
* **CSV dosyasını içe aktar... Alt+i**
* **CSV olarak dışa aktar... Alt+ı**
* **Tüm kayıtları sil. alt+t**
* **Çıkış düğmesi Alt+Ç**
### Yeni Kişi ve Düzenle Penceresi:

* **Kişi ekle Alt+T**
* **Kişiyi düzenle Alt+e**
 * **İptal düğmesi Alt+l**

> Kişi Yöneticisi eklentisinin tüm pencereleri escape tuşu ile veya ALT+L kısayol tuşuna basarak kapatılabilir.

## Teşekkürler

Bu eklenti, Abel Passos do Nascimento Jr. <abel.passos@gmail.com>, Rui Fontes <rui.fontes@tiflotecnia.com> ve Ângelo Abrantes <ampa4374@gmail.com> tarafından oluşturulan Erişilebilir Ajanda Eklentisinden ilham almıştır. .