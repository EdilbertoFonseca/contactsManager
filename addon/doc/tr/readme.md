# NVDA İçin Kişi Yöneticisi

* **Author**: Edilberto Fonseca <edilberto.fonseca@outlook.com>
* **Created on**: 11/04/2024
* **License**: [GPL 2.0](https://www.gnu.org/licenses/gpl-2.0.html)

## Giriş

**NVDA Kişi Yöneticisi**'ne hoş geldiniz!

Bu eklenti, görme engelli veya görme engelli kullanıcıların kişi listelerini pratik, erişilebilir ve verimli bir şekilde yönetmelerine yardımcı olmak için geliştirilmiştir.

Bu araçla şunları yapabilirsiniz:

* Add, edit, delete, and search for contacts;
* Import and export contact lists in CSV format;
* Apply custom phone number formatting;
* Choose a custom location to store your contact database;
* Navigate an intuitive and fully keyboard-accessible interface.

## Kurulum

1. NVDA'da **Araçlar** menüsünü açın ve **Eklenti Mağazası**'na gidin.
2. **Kullanılabilir Eklentiler** sekmesi altında **Arama** alanını kullanın ve "Kişi Yöneticisi"ni arayın.
3. Seçin, **Enter** tuşuna basın veya **Uygula**'ya tıklayın ve **Yükle**'yi seçin.
4. Kurulumu tamamlamak için NVDA'yı yeniden başlatın.

Eklenti yüklendikten sonra kullanıma hazırdır.

Listeden bir kişiyi seçtiğinizde ayrıntıları salt okunur bir metin kutusunda gösterilecektir. Kişi adının ilk harfini kullanarak listede dolaşabilirsiniz.

## Yapılandırma

Ayarlar paneline şu adresten erişin:
**NVDA Menüsü > Tercihler > Ayarlar > NVDA İçin Kişi Yöneticisi**

Mevcut seçenekler:

1. **Telefon numarası maskeleme**: Biçimlendirme maskesi uygulamak için "#" kullanın (ör. Brezilya numaraları için).
2. **Tüm kişilerin silinmesine izin ver** (`Alt+T`): Kişi listesindeki tüm girişleri silmek için bir düğmeyi etkinleştirir.
3. **CSV içe aktarmayı etkinleştir** (`Alt+I`): Kişileri CSV dosyalarından içe aktarmak için bir düğme gösterir.
4. **CSV dışa aktarmayı etkinleştir** (`Alt+X`): Kişi listesini bir CSV dosyasına aktarmak için kullanılan düğmeyi gösterir.
5. **İletişim dosyası dizini**: Ajanda dosyanızı saklamak için özel bir yol ayarlayın.

## Eklentiye Erişim

Kişi Yöneticisini iki şekilde açabilirsiniz:

1. Klavye kısayolu: 'Windows+Alt+L'
2. NVDA Menüsü: `NVDA+N > Araçlar > Kişi Yöneticisi`

Ana pencerede şunları yapabilirsiniz:

* Add, edit, and delete contacts;
* Search for specific contacts;
* Import and export CSV files;
* Delete all records in the contact list (if enabled).

## Yeni Kişi Ekleme

1. Kişi Yöneticisini açın (`Windows+Alt+L` veya menü aracılığıyla).
2. Yeni bir kişi eklemek için 'Alt+N' tuşlarına basın.
3. Alanları doldurun.
4. Kaydetmek için 'Alt+O' ya da iptal etmek için 'Alt+C' tuşlarına basın.

> **Not:** Alanlar arasında dolaşmak için **Enter** tuşunu kullanın.
> **Sekme** tuşu, bilinen bir sorun nedeniyle beklenmedik şekilde davranabilir.

## Bir Kişiyi Düzenleme

1. Listeden bir kişi seçin.
2. 'Alt+E' veya 'F2' tuşuna basın.
3. Değişikliklerinizi yapın.
4. Kaydetmek için 'Alt+O' ya da iptal etmek için 'Alt+C' tuşlarına basın.

## Kişileri Arama

1. Bir arama terimi yazın (isim, telefon veya e-posta).
2. Sonuçları filtrelemek için 'Alt+P' tuşlarına basın.
3. Tüm listeyi yenilemek için 'Alt+A' veya 'F5' tuşlarına basın.

> Eşleşme bulunamazsa mesajla sizi bilgilendirecektir.

## Klavye Kısayolları

### Ana Pencere

| Action                  | Shortcut            |
| ----------------------- | ------------------- |
| Add new contact         | `Alt+N`             |
| Edit selected contact   | `Alt+E` or `F2`     |
| Remove selected contact | `Alt+R` or `Delete` |
| Search                  | `Alt+P`             |
| Refresh contact list    | `Alt+A` or `F5`     |
| Import CSV file         | `Alt+I`             |
| Export to CSV           | `Alt+X`             |
| Delete all contacts     | `Alt+T`             |
| Exit                    | `Alt+S`             |

> Bir kişiyi **düzenlemek** veya **kaldırmak** için listede seçili olduğundan emin olun.
> Hiçbir kişi seçilmezse bir uyarı mesajı gösterilecektir.

### Kişi Ekle/Düzenle Penceresi

| Action  | Shortcut |
| ------- | -------- |
| Confirm | `Alt+O`  |
| Cancel  | `Alt+C`  |

> Tüm pencereleri 'Esc' veya 'Alt+F4' ile kapatabilirsiniz.

## Teşekkür

This add-on was inspired by the Accessible Agenda, originally developed by:

* Rui Fontes (<rui.fontes@tiflotecnia.com>)
* Ângelo Abrantes (<ampa4374@gmail.com>)
* Abel Passos do Nascimento Jr. (<abel.passos@gmail.com>)

## Translation

Translations for this add-on are managed through the [NVDA Add-ons Crowdin project](https://crowdin.com/project/nvdaaddons).

To contribute a translation, create a Crowdin account, join the appropriate language team if required, and translate the available interface and documentation strings directly in Crowdin.

You can also use Poedit to work with `.po` and `.xliff` files locally. Completed translations are synchronized to the add-on repository through the localization workflow.

For questions or assistance, please join the [NVDA Translations mailing list](https://groups.io/g/nvda-translations).
