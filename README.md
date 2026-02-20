

# ⛏️ DeepMine AI: Otonom Maden Analiz ve Ajan Tabanlı Planlama Sistemi

## 🚀 Proje Vizyonu

DeepMine AI, madencilik sektöründe hammadde ihracatçısı kimliğinden uç ürün teknolojisi üreten bir öncüye dönüşme vizyonuyla geliştirilmiştir. Bu proje; **Yapay Zeka (AI Agents)**, **Bilgisayar Görüsü (Computer Vision)** ve **Kestirimci Analiz** yöntemlerini kullanarak maden sahalarındaki verimliliği artırmayı ve iş kazalarını minimize etmeyi hedefler.

## 🧠 Neden Bu Proje? (Problem & Çözüm)

Geleneksel madencilikte operasyonel kararlar genellikle statik verilere dayanır. DeepMine AI, **Madencilik 4.0** yaklaşımıyla:

* 
**Problem:** İthal yazılımlara bağımlılık ve gerçek zamanlı veri analizindeki eksiklikler.


* 
**Çözüm:** Yerli imkanlarla geliştirilmiş, otonom navigasyon ve AI destekli rezerv tahminleme algoritmaları.



## 🛠️ Teknik Özellikler & Modüller

### 1. AI Agent Tabanlı Rezerv Planlama

Sondaj ve jeofizik verilerini analiz ederek 3D cevher modellemesi yapan karar destek sistemi.

* **Teknoloji:** Python, TensorFlow/PyTorch, AI Agents.
* 
**İşlev:** Rezerv alanlarını yüksek doğrulukla tahmin ederek plansız duruşları sıfıra indirir.



### 2. Otonom Navigasyon ve Sensör Füzyonu

GPS sinyalinin ulaşmadığı yer altı galerilerinde LiDAR ve sensör füzyonu kullanarak navigasyon sağlayan yazılım katmanı.

* **Teknoloji:** ROS 2 (Robot Operating System), C++, OpenCV.
* 
**İşlev:** İnsansız kazı ve nakliye araçlarının birbirleriyle gerçek zamanlı haberleşmesini sağlar.



### 3. Akıllı İSG ve Giyilebilir Takip

Personelin hayati verilerini ve ortamdaki gaz seviyelerini (Metan, CO2 vb.) anlık izleyen IoT ağı.

* 
**İşlev:** Tehlikeli durumlarda otomatik tahliye rotası çizer ve erken uyarı verir.



## 📂 Depo Yapısı

```text
├── src/
│   ├── ai_models/          # Rezerv tahminleme ve AI Agent algoritmaları
│   ├── autonomous_nav/     # LiDAR ve GPS-less navigasyon kodları
│   └── sensor_hub/         # IoT veri işleme ve İSG takip modülleri
├── docs/
[cite_start]│   ├── raporlar/           # Proje Ön Değerlendirme Raporları [cite: 240]
[cite_start]│   └── sunumlar/           # Yarı Final ve Final sunum dosyaları [cite: 256]
├── simulation/             # Gazebo/Unity tabanlı simülasyon ortamı
└── README.md

```

## 📈 Yarışma Süreci ve Yol Haritası

Proje, TEKNOFEST 2026 takvimine tam uyumlu olarak ilerlemektedir:

1. 
**Başvuru:** 20.02.2026 (Tamamlandı) 


2. 
**Ön Değerlendirme Raporu:** 01.04.2026 (Hazırlanıyor) 


3. 
**Yarı Final Sunumu:** Temmuz 2026 


4. 
**Final / Şanlıurfa:** Eylül 2026 



## 👤 Geliştirici Hakkında

Yazılım serüvenine Ağustos 2023'te başlamış, havacılık motorları ve otonom sistemler üzerine eğitim almış bir **Solopreneur** tarafından geliştirilmektedir. Multidisipliner bir yaklaşımı (Yazılım, Mekatronik, Veri Bilimi) merkeze alarak "Milli Teknoloji Hamlesi"ne katkı sunmayı amaçlar.

---

### ⚖️ Sorumluluk Beyanı

Bu proje T3 Vakfı ve TEKNOFEST Maden Teknolojileri Yarışması şartnamesine uygun olarak geliştirilmiştir.

