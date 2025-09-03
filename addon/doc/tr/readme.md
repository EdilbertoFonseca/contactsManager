# NVDA için Kişi Yöneticisi

**Yazar**: Edilberto Fonseca (<edilberto.fonseca@outlook.com>)  
**Oluşturulma Tarihi**: 11.04.2024  
**Lisans**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Giriş

**NVDA için Kişi Yöneticisi** eklentisine hoş geldiniz!

Bu eklenti, görme engelli kullanıcıların kişi listesini pratik, erişilebilir ve verimli bir şekilde yönetmelerine yardımcı olmak amacıyla geliştirilmiştir. Bu araç sayesinde:

- Kişi ekleyebilir, düzenleyebilir ve silebilirsiniz;
- Kişi bilgilerini hızlı bir şekilde arayabilirsiniz;
- Kişileri CSV formatında içe ve dışa aktarabilirsiniz — bu da yedekleme ve paylaşımı kolaylaştırır;
- Telefon numarası biçimlerini özelleştirebilirsiniz;
- Veritabanını dilediğiniz klasöre kaydedebilirsiniz;
- Klavye kısayolları ile hızlı ve verimli bir kullanım sağlayabilirsiniz.

Kişi Yöneticisi, NVDA içinde kişilerle çalışmak isteyen kullanıcılar için sade ve sezgisel bir arayüz sunar.

## Kurulum

1. NVDA'da **Araçlar** menüsünü açın ve **Eklenti Mağazası**na girin.
2. **Mevcut Eklentiler** sekmesinde arama alanına `Kişi Yöneticisi` yazın.
3. Sonuçlardan eklentiyi seçin, `Enter` tuşuna basın veya **Uygula**'ya tıklayın, ardından **Yükle**'yi seçin.
4. Kurulumu tamamlamak için NVDA'yı yeniden başlatın.

Kurulumdan sonra eklenti kullanıma hazırdır. Bir kişiyi seçtiğinizde bilgileri salt okunur bir kutuda görüntülenir. Listede gezinmek için kişinin isminin ilk harfine basabilirsiniz.

## Yapılandırma

Ayar paneline şu şekilde ulaşabilirsiniz:  
**NVDA Menüsü > Tercihler > Ayarlar... > NVDA için Kişi Yöneticisi**

Mevcut seçenekler:

1. **Telefon alanlarına maske ekle**  
   Telefon numaralarını biçimlendirmek için `#` sembolü ile maske uygular. Varsayılan format Brezilya telefon biçimidir.

2. **Tüm kişileri silme seçeneğini göster** (`Alt+T`)  
   Etkinleştirildiğinde, tüm kayıtları tek bir komutla silmenize olanak tanır.

3. **CSV dosyası içe aktarma düğmesini göster** (`Alt+I`)  
   CSV dosyasından kişi bilgilerini içe aktarmanızı sağlar.  
   > Not: CSV dosyasındaki alanlar, Kişi Yöneticisi ile uyumlu olmalıdır.

4. **CSV dosyasını dışa aktarma düğmesini göster** (`Alt+X`)  
   Tüm kişileri CSV formatında dışa aktarır.

5. **Kişi veritabanı klasörü**  
   Kişi veritabanının saklanacağı dizini belirlemenizi sağlar. Varsayılan yol değiştirilebilir.

## Kişi Yöneticisini Açma

Kişi Yöneticisi’ne aşağıdaki yollarla erişebilirsiniz:

1. Kısayol tuşu: `Windows+Alt+L`  
2. NVDA Menüsü: `NVDA+N > Araçlar > Kişi Yöneticisi`

Ana pencerede şunları yapabilirsiniz:

- Kişi ekleme, düzenleme ve silme;
- Kişi arama;
- CSV içe / dışa aktarma;
- Tüm kişileri silme (isteğe bağlı olarak).

## Yeni Kişi Ekleme

1. Ana pencereyi açın;
2. `Alt+N` tuşuna basarak yeni kişi ekleyin;
3. Gerekli alanları doldurun;
4. `Alt+O` ile kaydedin veya `Alt+C` ile iptal edin.

> **Not:**  
> Alanlar arasında geçiş yapmak için `Enter` tuşunu kullanın. `Tab` tuşu bazı durumlarda öngörülemeyen davranışlara neden olabilir.

## Kişi Düzenleme

1. Listeden düzenlemek istediğiniz kişiyi seçin;
2. `Alt+E` veya `F2` tuşuna basın;
3. Gerekli değişiklikleri yapın;
4. `Alt+O` ile kaydedin veya `Alt+C` ile iptal edin.

> Alanlar arasında gezinme, yeni kişi penceresi ile aynıdır.

## Kişi Arama

Kişi listesi penceresinde şu alanlara göre arama yapabilirsiniz:

- Ad
- Cep telefonu
- Sabit telefon
- E-posta

Arama terimini girdikten sonra `Alt+P` tuşuna basın.  
Listeyi yenilemek ve aramayı sıfırlamak için `Alt+A` veya `F5` tuşunu kullanın.

> Eşleşme bulunamazsa kullanıcıya bir bilgilendirme mesajı gösterilir.

## Klavye Kısayolları

### Ana Pencere

| İşlem                    | Kısayol               |
|--------------------------|-----------------------|
| Yeni kişi                | `Alt+N`               |
| Kişi düzenle             | `Alt+E` veya `F2`     |
| Kişi sil                 | `Alt+R` veya `Delete` |
| Arama yap                | `Alt+P`               |
| Listeyi yenile           | `Alt+A` veya `F5`     |
| CSV içe aktar            | `Alt+I`               |
| CSV dışa aktar           | `Alt+X`               |
| Tüm kişileri sil         | `Alt+T`               |
| Kapat                    | `Alt+S`               |

> **Not:**  
> Kişiyi düzenlemek veya silmek için önce listeden bir kişinin seçilmiş olması gerekir. Aksi hâlde, “seçili kişi yok” mesajı gösterilir.

### Yeni/Düzenle Penceresi

| İşlem    | Kısayol   |
|----------|-----------|
| Kaydet   | `Alt+O`   |
| İptal    | `Alt+C`   |

> Tüm pencereler `Esc` veya `Alt+F4` ile kapatılabilir.

## Teşekkürler

Bu eklenti, aşağıdaki kişilerin geliştirdiği kişi yöneticisinden esinlenilerek oluşturulmuştur:

- Abel Passos do Nascimento Jr. (<abel.passos@gmail.com>)  
- Rui Fontes (<rui.fontes@tiflotecnia.com>)  
- Ângelo Abrantes (<ampa4374@gmail.com>)

## Çeviriler

- **Portekizce (Brezilya)** – Edilberto Fonseca  
- **Portekizce (Portekiz)** – Edilberto Fonseca  
- **Ukraynaca** – George‑br  
- **Türkçe** – Umut KORKMAZ
