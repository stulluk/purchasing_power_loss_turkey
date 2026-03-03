# Zam Talebi Araştırma Prompt'u ve Kullanma Rehberi

---

## 📋 KULLANMA REHBERİ

### Nasıl Kullanılır?

1. Aşağıdaki prompt'u kopyala
2. Claude'da **yeni bir chat** aç (bu chat'te değil, temiz bir chat'te kullan)
3. Prompt'u yapıştır ve gönder
4. Claude sana sorular sorabilir — aşağıdaki "hazırda tut" listesine bak

### Hazırda Tutman Gereken Bilgiler

Claude senden şunları sorabilir:
- **Aylık USD maaşın** (yaklaşık aralık yeterli, tam rakam vermek zorunda değilsin)
- **Şahıs şirketi giderlerin** — muhasebeci ücreti, sanal ofis kirası, vergi oranları (2023 vs 2025 karşılaştırması)
- **Kaç kişilik bir ekipsiniz** (opsiyonel, etki gücünü artırır)
- **Talep ettiğin zam oranı veya miktarı** (eğer kafanda bir rakam varsa)

### Çıktıdan Sonra Yapabileceklerin

Claude sana İngilizce bir doküman üretecek. Bundan sonra şunları isteyebilirsin:

- `"Bunu PDF formatında hazırla"` — indirilebilir PDF çıktısı için
- `"Grafikleri daha büyük/farklı renklerde yap"` — görsel düzenleme için
- `"X bölümünü kısalt / genişlet"` — içerik ayarlaması için
- `"Bir de kısa bir e-posta taslağı hazırla, bu dokümanı ek olarak göndereceğim"` — e-posta için
- `"Executive summary ekle"` — yöneticinin hızlıca okuyabileceği 3-4 cümlelik özet için
- `"Ton'u daha diplomatik / daha net yap"` — üslup ayarı için

### İpuçları

- Grafiklerin anlaşılır olması çok önemli — yöneticin Türkiye'yi bilmiyor, görsel anlatım sözden daha etkili
- Dokümanı çok uzun tutma, 3-5 sayfa ideal. Yöneticiler uzun doküman okumaz
- Talep ettiğin zam oranını dokümanın **sonuna** koy, önce problemi anlat

---

## 🚀 PROMPT

Aşağıdaki prompt'u kopyalayıp yeni bir Claude chat'ine yapıştır:

---

```
Türkiye'de yaşayan ve Amerikan merkezli bir teknoloji şirketine uzaktan çalışan bir ekibin temsilcisi olarak, yönetimimize maaş ayarlaması (cost-of-living adjustment) talebi sunacağım. Bu talebi desteklemek için profesyonel, veri odaklı, İngilizce bir doküman hazırlamanı istiyorum.

## BAĞLAM

- Ekibimiz Ocak 2023'ten bu yana bu şirkette çalışıyor
- Maaşlarımızı USD olarak alıyoruz, hiç zam almadık
- Türkiye'de şahıs şirketi (sole proprietorship) üzerinden çalışıyoruz — bu yasal bir zorunluluk
- Şahıs şirketi sahibi olmak ek maliyetler getiriyor: gelir vergisi, muhasebeci ücreti, sanal ofis kirası, SGK primleri vs.
- Yöneticimiz Amerikalı ve Türkiye'nin ekonomik durumunu hiç bilmiyor
- Bu dokümanı önce toplantıda sözlü sunacağım, sonra e-posta ile ileteceğim

## DOKÜMANDA OLMASI GEREKENLER

### 1. Türkiye Enflasyon Tablosu (Ocak 2023 – Şubat 2026)
- TÜİK ve/veya ENAG verilerini kullanarak yıllık ve kümülatif enflasyon oranları
- ABD enflasyonu ile yan yana karşılaştırma (farkın ne kadar dramatik olduğunu göstermek için)
- **Grafik:** Çizgi grafik — Türkiye vs ABD kümülatif enflasyon, Ocak 2023'ten bugüne

### 2. Alım Gücü Kaybı Analizi
- Ocak 2023'te 1 USD = X TRY iken, bugün 1 USD = Y TRY
- Döviz kuru artmış olsa da, TRY cinsinden enflasyon döviz kuru artışını aştığı için NET alım gücü düşmüştür
- Bunu somut bir örnekle açıkla: "Ocak 2023'te bu maaşla alınabilen bir sepet, bugün aynı maaşla ne kadarına alınabiliyor"
- **Grafik:** Bar chart — Ocak 2023'teki 100 birimlik alım gücünün bugün kaça düştüğünü gösteren basit görsel

### 3. Şahıs Şirketi Ek Maliyetleri
- Türkiye'de freelancer/contractor olarak çalışmanın getirdiği ek yükler
- Muhasebeci ücretleri, sanal ofis kiraları, vergi dilimleri — bunların 2023'ten bugüne nasıl arttığını göster
- Bu maliyetlerin brüt maaştan ne kadar yediğini açıkla

### 4. Sektörel Karşılaştırma (Opsiyonel ama güçlü)
- Türkiye'deki teknoloji sektöründe benzer rollerde maaş artış oranları (varsa veri)
- Türkiye'deki asgari ücret artış oranları (referans noktası olarak)

### 5. Talep
- Dokümanın sonunda, nazik ama net bir dille, "cost-of-living adjustment" talebi
- Spesifik oran belirtme, bunun yerine "bize makul bir ayarlama yapılmasını talep ediyoruz" gibi açık uçlu bırak (ben gerekirse sonra eklerim)

## FORMAT VE ÜSLUP

- Dil: İNGİLİZCE (yöneticim Amerikalı)
- Üslup: Profesyonel, sakin, diplomatik — şikayet değil, mantıklı bir iş talebi
- Grafiklerde: Basit, temiz, kolay anlaşılır — yöneticim Türkiye'yi bilmiyor, karmaşık grafikler kafa karıştırır
- Uzunluk: 3-5 sayfa, daha fazla değil
- Hiçbir yerde suçlayıcı veya şikayetçi bir ton kullanma
- Verileri web'den araştırarak gerçek, güncel rakamlarla destekle
- Gerekli olan yerlerde kaynakları dipnot olarak belirt

## ÖNEMLİ NOT

Bu doküman sadece benim değil, ekibimizin ortak talebini temsil ediyor. Bu yüzden "I" yerine "we" / "our team" kullan.
```

---

## ⚡ EK PROMPT'LAR (İHTİYACIN OLURSA)

### PDF'e çevirmek için:
```
Bu dokümanı şimdi profesyonel görünümlü bir PDF olarak hazırla. Grafikleri de PDF'in içine göm. Şirket logosu ekleme, sade ve temiz kalsın.
```

### E-posta taslağı için:
```
Bu dokümanı ek olarak göndereceğim kısa bir e-posta taslağı hazırla. Yöneticime hitap edecek, toplantıda konuştuğumuz konunun detaylı dokümanını ekte sunduğumu belirtecek. 3-4 cümle yeterli, çok uzun olmasın.
```

### Daha diplomatik ton için:
```
Dokümanın tonunu biraz daha yumuşat. Talep kısmını daha diplomatik yap. Amacımız karşı tarafı köşeye sıkıştırmak değil, durumu anlamalarını sağlamak.
```

### Executive summary eklemek için:
```
Dokümanın en başına 3-4 cümlelik bir "Executive Summary" ekle. Yöneticim dokümanı tamamen okumasa bile bu özetten ana mesajı anlayabilmeli.
```
