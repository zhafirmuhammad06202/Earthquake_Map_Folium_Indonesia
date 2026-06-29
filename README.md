# 🗺️ Earthquake Map Indonesia 2020–2025

> Peta interaktif sebaran gempa bumi Indonesia menggunakan Folium dan data USGS.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python) ![Folium](https://img.shields.io/badge/Folium-Map-green) ![USGS](https://img.shields.io/badge/Data-USGS-orange)

---

## 📌 Project Overview

Peta interaktif untuk memvisualisasikan sebaran gempa bumi di Indonesia periode 2020–2025 menggunakan data real-time dari **USGS Earthquake Catalog**. Setiap marker dikodekan dengan warna berdasarkan magnitudo gempa, dilengkapi popup informasi detail untuk setiap kejadian.

**Wilayah yang dianalisis:** Seluruh wilayah Indonesia — Sumatera · Jawa · Kalimantan · Sulawesi · Maluku · Papua

---

## 🎨 Color Legend

| Warna | Magnitudo | Kategori |
|---|---|---|
| 🟢 Hijau | M 5.0 – 5.5 | Sedang |
| 🟠 Orange | M 5.5 – 6.0 | Kuat |
| 🔴 Merah | M ≥ 6.0 | Sangat Kuat |

---

## 📊 Key Statistics

| Parameter | Nilai |
|---|---|
| Total gempa (M≥5.0) | 1000 kejadian |
| Periode | 2020 – 2025 |
| Sumber data | USGS Earthquake Catalog |
| Library visualisasi | Folium (Leaflet.js) |

---

## 🛠️ Tech Stack

| Library | Fungsi |
|---|---|
| Folium | Interactive map visualization |
| Pandas | Data manipulation |
| Requests | Fetch data dari USGS API |
| Branca | Custom HTML elements (legend) |

---

## ▶️ How to Run

```bash
git clone https://github.com/zhafirmuhammad06202/Earthquake_Map_Folium_Indonesia.git
cd Earthquake_Map_Folium_Indonesia
pip install folium requests pandas branca
python peta_gempa.py
```

Buka file output: **peta_gempa_indonesia_2020_2025.html**

---

## 📁 Repository Structure
Earthquake_Map_Folium_Indonesia/

├── peta_gempa.py                        # Main script

├── peta_gempa_indonesia_2020_2025.html  # Output map (HTML)

└── README.md                            # Documentation

---

## 👤 Author

**Muhammad Zhafir** — Geophysics Graduate · Universitas Syiah Kuala, Banda Aceh, Indonesia

[![GitHub](https://img.shields.io/badge/GitHub-zhafirmuhammad06202-black?logo=github)](https://github.com/zhafirmuhammad06202)

---

## 📄 License

MIT License
