
<div align="center">

# ⛏️ DeepMine AI
### Otonom Maden Analiz ve Ajan Tabanlı Planlama Sistemi

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![ROS 2 Humble](https://img.shields.io/badge/ROS%202-Humble-red.svg)](https://docs.ros.org/en/humble/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)
[![Status](https://img.shields.io/badge/Status-Development-green.svg)]()

<br />

**Milli Teknoloji Hamlesi İçin Yerli ve Otonom Çözümler**

[Proje Vizyonu](#-proje-vizyonu) •
[Özellikler](#-teknik-özellikler--modüller) •
[Kurulum](#-kurulum) •
[Geliştirici](#-geliştirici-hakkında)

</div>

---

## 🚀 Proje Vizyonu

**DeepMine AI**, madencilik sektöründe hammadde ihracatçısı kimliğinden **uç ürün teknolojisi üreten bir öncüye** dönüşme vizyonuyla geliştirilmiştir.

> "Geleceğin madenciliği yerin altında değil, verinin derinliklerinde başlar."

Bu proje; **Yapay Zeka (AI Agents)**, **Bilgisayar Görüsü (Computer Vision)** ve **Kestirimci Analiz** yöntemlerini birleştirerek maden sahalarındaki verimliliği maksimize etmeyi ve iş kazalarını sıfıra indirmeyi hedefler.

---

## 🧠 Neden Bu Proje? (Problem & Çözüm)

Geleneksel madencilikte operasyonel kararlar genellikle statik verilere dayanır. **DeepMine AI**, **Madencilik 4.0** yaklaşımıyla bu paradigmayı değiştiriyor:

| Problem 🛑 | Çözüm ✅ |
| :--- | :--- |
| **İthal Bağımlılık:** Yüksek maliyetli yabancı yazılımlar. | **Yerli Teknoloji:** Tamamen yerli imkanlarla geliştirilmiş algoritmalar. |
| **Veri Körlüğü:** Anlık analiz eksikliği. | **Otonom Karar:** AI tabanlı rezerv tahminleme ve gerçek zamanlı analiz. |
| **Güvenlik Riski:** Yüksek iş kazası oranları. | **Akıllı İSG:** Giyilebilir sensörler ve otonom tahliye planlaması. |

---

## 🛠️ Teknik Özellikler & Modüller

### 1. 🤖 AI Agent Tabanlı Rezerv Planlama
Sondaj ve jeofizik verilerini analiz ederek **3D cevher modellemesi** yapan karar destek sistemi.
*   **Teknoloji:** `Python`, `TensorFlow/PyTorch`, `Deep Learning`
*   **İşlev:** Rezerv alanlarını %95+ doğrulukla tahmin ederek plansız duruşları engeller.

### 2. 🛸 Otonom Navigasyon (GPS-Free)
GPS sinyalinin ulaşmadığı yer altı galerilerinde **LiDAR** ve **Sensör Füzyonu** ile tam otonom hareket.
*   **Teknoloji:** `ROS 2`, `C++`, `SLAM`, `OpenCV`
*   **İşlev:** İnsansız araçların karanlık ve dar tünellerde güvenle ilerlemesini sağlar.

### 3. ⌚ Akıllı İSG ve Giyilebilir Takip
Personelin hayati verilerini ve ortamdaki gaz seviyelerini (Metan, CO2) anlık izleyen IoT ağı.
*   **Teknoloji:** `IoT`, `Embedded Systems`, `Real-time Monitoring`
*   **İşlev:** Tehlike anında otomatik tahliye rotası oluşturur ve acil durum protokollerini devreye sokar.

---

## 🏗️ Sistem Mimarisi

DeepMine AI, dağıtık bir **Multi-Agent System (MAS)** mimarisi üzerine kuruludur. Aşağıdaki diyagram, sistemin veri akışını ve modüller arası etkileşimi özetler:

```mermaid
graph TD
    subgraph "Saha Veri Toplama (Edge Layer)"
        A[LiDAR & Kameralar] -->|Nokta Bulutu/Görüntü| B(ROS 2 Sensor Hub)
        C[loT Sensör Ağı] -->|Gaz/Nabız/Konum| B
    end

    subgraph "Merkezi İşleme (Fog/Cloud Layer)"
        B -->|Ham Veri| D{Veri Ön İşleme & Füzyon}
        D --> E[Rezerv Tahmin AI Modeli]
        D --> F[SLAM & Haritalama]
        E -->|Rezerv Haritası| G[Karar Destek Sistemi]
        F -->|Konum Bilgisi| G
    end

    subgraph "Aksiyon & Arayüz (Application Layer)"
        G --> H[Otonom Navigasyon Rotası]
        G --> I[Dashboard & Uyarılar]
        H --> J((Otonom Maden Aracı))
        I --> K((Operatör))
    end
```

---

## � Matematiksel Model ve Algoritmalar

### 1. Rezerv Kestirimi (Gausian Process Regression)
Cevher dağılımını modellemek için olasılıksal yöntemler kullanıyoruz. Belirsizliği minimize etmek için hedef fonksiyonumuz:

$$ J(\theta) = - \frac{1}{2} \log |K| - \frac{1}{2} y^T K^{-1} y - \frac{n}{2} \log (2\pi) $$

Burada $K$ kovaryans matrisini, $y$ gözlemlenen sondaj verilerini temsil eder.

### 2. Otonom Rota Planlama (RRT* + Potential Fields)
Dinamik engellerden kaçınmak için potansiyel alanlar yöntemiyle optimize edilmiş RRT* algoritması kullanılır:

$$ U(q) = U_{att}(q) + \sum U_{rep}(q) $$

$$ F(q) = -\nabla U(q) $$

Bu sayede araç, hedefe (attraction) yönelirken engellerden (repulsion) matematiksel olarak itilir.

---

## 💻 Kurulum

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları takip edin:

### Gereksinimler
*   **OS:** Ubuntu 22.04 LTS (Önerilen) / Windows 10+ (WSL2 ile)
*   **Python:** 3.8+
*   **ROS 2:** Humble Hawksbill

### Adım Adım Kurulum

1.  **Depoyu Klonlayın:**
    ```bash
    git clone https://github.com/bahattinyunus/teknofest_maden_teknolojileri.git
    cd teknofest_maden_teknolojileri
    ```

2.  **Bağımlılıkları Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **ROS 2 Çalışma Alanını Derleyin:**
    ```bash
    colcon build --symlink-install
    source install/setup.bash
    ```

4.  **Simülasyonu Başlatın:**
    ```bash
    ros2 launch autonomous_nav simulation_launch.py
    ```

---

```bash
teknofest_maden_teknolojileri/
├── src/
│   ├── ai_models/          # 🧠 Rezerv tahminleme ve AI Agent algoritmaları
│   ├── autonomous_nav/     # 🛸 LiDAR ve GPS-less navigasyon kodları
│   └── sensor_hub/         # ⌚ IoT veri işleme ve İSG takip modülleri
├── docs/
│   ├── raporlar/           # 📄 Proje Ön Değerlendirme Raporları
│   └── sunumlar/           # 📊 Yarı Final ve Final sunum dosyaları
├── simulation/             # 🎮 Gazebo/Unity tabanlı simülasyon ortamı
└── README.md
```

---

## 📈 Yarışma Süreci ve Yol Haritası

Proje, **TEKNOFEST 2026** takvimine tam uyumlu olarak ilerlemektedir:

- [x] **Başvuru:** 20.02.2026 ✅
- [ ] **Ön Değerlendirme Raporu:** 01.04.2026 📝
- [ ] **Yarı Final Sunumu:** Temmuz 2026 🎤
- [ ] **Final / Şanlıurfa:** Eylül 2026 🏆

---

## 👤 Geliştirici Hakkında

<div align="center">

**Bahattin Yunus**
*Yazılım, Mekatronik ve Veri Bilimi Tutkunu*

Havacılık motorları ve otonom sistemler üzerine eğitim almış, **Solopreneur** ruhuyla hareket eden bir mühendis. "Milli Teknoloji Hamlesi"ne katkı sunmak için disiplinlerarası tecrübesini bu projede birleştiriyor.

[GitHub](https://github.com/bahattinyunus) • [LinkedIn](#) • [Email](#)

</div>

---

### ⚖️ Sorumluluk Beyanı
Bu proje **T3 Vakfı** ve **TEKNOFEST Maden Teknolojileri Yarışması** şartnamesine uygun olarak geliştirilmiştir.

<div align="center">
<sub>Made with ❤️ by Bahattin Yunus</sub>
</div>
