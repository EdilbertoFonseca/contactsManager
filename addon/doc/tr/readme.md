# NVDA için Kişi Yöneticisi

- **Yazar**: Edilberto Fonseca (<edilberto.fonseca@outlook.com>)  
- **Oluşturulma Tarihi**: 11/04/2024  
- **Lisans**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Giriş

**NVDA için Kişi Yöneticisi** eklentisine hoş geldiniz!

Bu eklenti, görme engelli kullanıcıların kişi listesini pratik, erişilebilir ve verimli bir şekilde yönetmelerine yardımcı olmak amacıyla geliştirilmiştir. Bu araç sayesinde:

- Kişi ekleyebilir, düzenleyebilir ve silebilirsiniz,
- Kişi bilgilerini hızlı bir şekilde arayabilirsiniz,
- Kişileri CSV formatında içe ve dışa aktarabilirsiniz — bu da yedekleme ve paylaşımı kolaylaştırır.

Kişi Yöneticisi basit ve sezgisel bir arayüz sunar; NVDA içinde kişilerle çalışmak isteyen kullanıcılar için ideal bir çözümdür.

## Kurulum

1. NVDA'da **Araçlar** menüsünü açın ve **Eklenti Mağazası**na girin.
2. **Mevcut Eklentiler** sekmesinde **Ara** alanını kullanın.
3. `contactsManager` yazın. Sonuçlar göründüğünde **Enter** tuşuna basın veya **Uygula**'ya tıklayın, ardından **Yükle**'yi seçin.
4. Değişikliklerin geçerli olması için NVDA’yı yeniden başlatın.

Artık eklenti kullanıma hazırdır.

Bir kişi seçildiğinde, bilgileri salt okunur bir metin kutusunda görüntülenir. Kişi listesinde, kişinin adının ilk harfine basarak da gezinebilirsiniz.

## Ayarlar

Ayar paneline şu şekilde ulaşabilirsiniz:  
**NVDA Menüsü > Tercihler > Ayarlar... > NVDA için Kişi Yöneticisi**

Mevcut seçenekler:

1. **Telefon alanlarına maske ekle**  
   Telefon numaralarını biçimlendirmek için `#` sembolü ile maske uygular. Varsayılan format Brezilya telefon standartlarını takip eder.

2. **Tüm kişileri silme seçeneğini göster** (`Alt+T`)  
   Etkinleştirildiğinde, kişi listesindeki tüm kayıtları tek bir komutla silmenizi sağlar.

3. **CSV dosyası içe aktarma düğmesini göster** (`Alt+I`)  
   CSV dosyasından kişi içe aktarmanıza olanak tanır.  
   > Not: CSV dosyasındaki alanlar, Kişi Yöneticisi yapısıyla uyumlu olmalıdır.

4. **CSV dosyasını dışa aktarma düğmesini göster** (`Alt+X`)  
   Kişi listesini bir CSV dosyasına dışa aktarır.

5. **Kişi dosyalarının klasörü**  
   Kişi veritabanının saklanacağı klasörü belirtmenizi sağlar. Varsayılan yol değiştirilebilir.

## Kullanım

Kişi Yöneticisini şu iki yolla açabilirsiniz:

1. Kısayol tuşu: `Windows+Alt+L`  
2. NVDA Menüsü: `NVDA+N > Araçlar > Kişi Yöneticisi > Kişi Yöneticisi`

Ana pencerede şunları yapabilirsiniz:

- Kişi ekleme, düzenleme ve silme;
- Kişi arama;
- CSV dosyası içe/dışa aktarma;
- Tüm kişileri silme (isteğe bağlı).

İçe aktarma, dışa aktarma ve tüm kişileri silme seçenekleri varsayılan olarak etkinleştirilmiştir, ancak ayarlardan devre dışı bırakılabilir.

### Yeni Kişi Ekleme

1. Kişi Yöneticisini açın (`Windows+Alt+L` veya NVDA menüsünden).
2. Kişi listesi penceresinde `Alt+N` tuşuna basarak yeni bir kişi ekleyin.
3. Alanları doldurun ve kaydetmek için `Alt+O`, iptal etmek için `Alt+C` tuşuna basın.

> **Not:**  
> Alanlar arasında geçiş yapmak için `Enter` tuşunu kullanmanız önerilir. `Tab` tuşu da çalışabilir, ancak bazı durumlarda öngörülemeyen davranışlara yol açabilir (henüz çözülememiş bir sorun nedeniyle).

### Kişi Düzenleme

1. Listeden bir kişiyi seçin.
2. Düzenleme penceresini açmak için `Alt+E` veya `F2` tuşuna basın.
3. Değişiklikleri yaptıktan sonra `Alt+O` ile kaydedin veya `Alt+C` ile iptal edin.

> **Not:**  
> Alanlar arasında gezinme, yeni kişi penceresindekiyle aynıdır.

### Arama

Kişi listesi penceresinde:

1. Aşağıdaki alanlara göre arama yapabilirsiniz:
   - Ad
   - Cep telefonu
   - Sabit telefon
   - E-posta
2. Arama terimini girdikten sonra `Alt+P` tuşuna basarak sonuçları görüntüleyin.
3. Listeyi yenilemek ve aramayı temizlemek için `Alt+A` veya `F5` tuşunu kullanın.

Eğer sonuç bulunamazsa, kullanıcıya bilgi veren bir mesaj gösterilir.

## Kısayollar ve İpuçları

### Kişi Listesi Penceresi

| İşlem                     | Kısayol              |
|---------------------------|----------------------|
| Ara                       | `Alt+P`              |
| Düzenle                   | `Alt+E` veya `F2`    |
| Yeni kişi                 | `Alt+N`              |
| Kişi sil                  | `Alt+R` veya `Delete`|
| Listeyi yenile            | `Alt+A` veya `F5`    |
| CSV içe aktar             | `Alt+I`              |
| CSV dışa aktar            | `Alt+X`              |
| Tüm kişileri sil          | `Alt+T`              |
| Çıkış                     | `Alt+S`              |

> **Önemli:**  
> Bir kişiyi **düzenlemek** veya **silmek** için, kişinin önceden **listede seçilmiş olması gerekir**.  
> Eğer hiçbir kişi seçilmediyse, **seçili kişi bulunamadı** uyarısı gösterilir.

### Yeni/Düzenle Penceresi

| İşlem          | Kısayol   |
|----------------|-----------|
| Onayla         | `Alt+O`   |
| İptal          | `Alt+C`   |

> **İpucu:**  
> Tüm pencereler `Esc` veya `Alt+F4` tuşlarıyla kapatılabilir.

## Teşekkürler

Bu eklenti, aşağıdaki kişilerin oluşturduğu kişi yöneticisinden ilham alınarak geliştirilmiştir:

- Abel Passos do Nascimento Jr. (<abel.passos@gmail.com>)  
- Rui Fontes (<rui.fontes@tiflotecnia.com>)  
- Ângelo Abrantes (<ampa4374@gmail.com>)
