# NVDA için İletişim Yöneticisi

* **Yazar**: Edilberto Fonseca <edilberto.fonseca@outlook.com>
* **Oluşturulma Tarihi**: 11/04/2024
* **Lisans**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Giriş

NVDA için İletişim Yöneticisi eklentisine hoş geldiniz! Bu, görme engelli bireylerin iletişim listelerini daha kolay ve verimli bir şekilde yönetmelerine yardımcı olmak için özel olarak geliştirilmiş bir eklentidir. Bu eklenti ile iletişim ekleyebilir, düzenleyebilir ve silebilir, ayrıca isimler ve iletişim bilgilerini hızlı ve basit bir şekilde arayabilirsiniz. Ayrıca, iletişim listenizi dışa aktarma ve içe aktarma imkanı da sunuyoruz, böylece paylaşabilirsiniz. NVDA için İletişim Yöneticisi, kullanımı kolay ve sezgisel bir arayüze sahip olup, iletişim listenizi verimli bir şekilde yönetmeniz için ideal bir seçimdir.

## Kurulum

NVDA için İletişim Yöneticisi'ni kurmak için adım adım talimatlar:

1. **Eklenti kurulum dosyasını indirin**: Dosyayı Eklenti Mağazası'ndan veya [İletişim Yöneticisi](https://github.com/EdilbertoFonseca/contactManager) resmi sayfasından edinin.
   **Not**: Eklenti mağazadan indirilirse, kurulum otomatik olarak gerçekleşecektir. Aksi takdirde, aşağıdaki talimatları izleyin.
2. **Eklentiyi kurun**: İndirilen eklenti dosyasının üzerine Enter tuşuna basın.
3. **Ekrandaki talimatları izleyin**: Kurulumu verilen talimatlara göre tamamlayın.
4. **NVDA'yı yeniden başlatın**: Eklentiyi etkinleştirmek için yeniden başlatmanız gerekmektedir.
5. **Kurulumu kontrol edin**: "NVDA + N" tuşuna basarak NVDA menüsünü açın, "Araçlar" kısmına gidin ve İletişim Yöneticisi eklentisinin listelendiğinden emin olun.

Artık NVDA için İletişim Yöneticisi'ni kullanmaya ve iletişimlerinizi doğrudan NVDA'dan kaydetmeye hazırsınız. Kullanımınızı ve ihtiyaçlarınıza göre özelleştirmenizi sağlamak için eklentinin belgelerini kontrol etmeyi unutmayın.

## Ayarlar

NVDA'nın Tercihler menüsünde, İletişim Yöneticisi için Ayarlar... kısmında aşağıdaki seçenekleri yapılandırabilirsiniz:

1. Telefon alanları için maske ekleyin.
   Bu seçenek, telefon numarasının formatlanması için `#` sembolünü kullanarak bir maske ekler. Varsayılan olarak, cep telefonu ve sabit telefon alanları Brezilya için formatlanmıştır.
2. Tüm rehberi silme seçeneğini göster, işaretlenmemiş kutu. Alt + e.
   Aktif hale getirildiğinde, rehberin tüm içeriğini silmenizi sağlar.
3. CSV dosyası içe aktarımı göster, işaretlenmemiş kutu. Alt + e.
   CSV dosyalarının içe aktarımına olanak tanır.
   Not: Tüm alanlar İletişim Yöneticisi ile uyumlu olmalıdır.
4. CSV dosyası dışa aktarımı göster, işaretlenmemiş kutu. Alt + e.
   Rehberdeki tüm iletişimleri bir CSV dosyasına kaydeder.
5. Rehber dosyalarının yolu.
   Varsayılanın dışında bir veritabanı dizini seçmenize veya eklemenize olanak tanır.

## Kullanım

NVDA için İletişim Yöneticisi'ne iki şekilde erişebilirsiniz:

1. Kısayol ile, Windows + Alt + L;
2. NVDA menüsünden (NVDA + N) Araçlar > İletişim Yöneticisi.

Eklentinin ana penceresine erişeceksiniz. Bu pencerede, iletişimleri kaydedebilir, düzenleyebilir, kaldırabilir ve arayabilirsiniz. Ayrıca, CSV içe aktarma, CSV dışa aktarma ve tüm rehberi silme seçeneklerine de sahiptir. Bu üç seçenek varsayılan olarak etkin durumdadır ve yapılandırma panelinde devre dışı bırakılabilir.

### Yeni bir iletişim kaydetme

Yeni bir iletişim kaydetmek için:

1. NVDA menüsünden İletişim Yöneticisi'ne erişin, Araçlar, İletişim Yöneticisi veya kısayol (Windows + Alt + L) ile;
2. İletişim Listesi penceresinde, yeni bir iletişim eklemek için Alt + N tuşuna basın.
3. Yeni İletişim penceresinde, tüm alanları doldurun ve kaydetmek için Alt + O'ya, kaydetmeden çıkmak için Alt + C'ye basın;

### Bir iletişimi düzenleme

Bir iletişimi düzenlemek için:

1. Listeden bir iletişimi seçin;
2. ALT + E tuşuna basın veya F2 tuşunu kullanın.

Düzenleme penceresi, isim alanına odaklanarak açılacaktır. Düzenleyin ve değişiklikleri kaydetmek için ALT + O, iptal etmek için ALT + C'ye basın.

### Arama

İletişim Listesi penceresinde, belirli bir iletişimi bulmak için arama alanını kullanabilirsiniz.
Aşağıdaki alanlara göre arama yapabilirsiniz:

* İsim;
* Cep telefonu;
* Sabit telefon;
* E-posta.

Alanı seçtikten sonra, arama terimini girin ve sonuçları listede görüntülemek için ALT + P kısayoluna basın. Hiçbir sonuç bulunamazsa, öğenin bulunamadığını belirten bir mesaj görüntülenecektir. Güncellemek için ALT + A kısayolunu veya F5 tuşunu kullanın.

## İpuçları ve Kısayollar

### İletişim Listesi Penceresi

* **Ara Butonu:** ALT + P
* **Düzenle Butonu:** ALT + E (F2 tuşu da kullanılabilir)
* **Yeni Buton:** ALT + N
* **Kaldır Butonu:** ALT + R (Delete tuşu da kullanılabilir)
* **Güncelle Butonu:** ALT + A (F5 tuşu da kullanılabilir)
* **CSV İçe Aktar:** ALT + I
* **CSV Dışa Aktar:** ALT + X
* **Tüm Kayıtları Sil:** ALT + T
* **Çıkış Butonu:** ALT + S

### Yeni İletişim ve Düzenleme Penceresi

* **Onay İşlemleri:** ALT + O
* **İptal Butonu:** ALT + C

>Tüm NVDA için İletişim Yöneticisi pencereleri, Esc tuşu veya Alt + F4 ile kapatılabilir.

## Teşekkürler

Bu eklenti, Abel Passos do Nascimento Jr. <abel.passos@gmail.com>, Rui Fontes <rui.fontes@tiflotecnia.com> ve Ângelo Abrantes <ampa4374@gmail.com> tarafından oluşturulan rehberden ilham alınarak hazırlanmıştır.
