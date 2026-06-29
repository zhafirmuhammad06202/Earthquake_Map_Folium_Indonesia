import folium
import requests
import pandas as pd
from datetime import datetime

# Fetch data dari USGS
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "geojson",
    "starttime": "2020-01-01",
    "endtime": "2025-12-31",
    "minmagnitude": 5.0,
    "minlatitude": -11,
    "maxlatitude": 6,
    "minlongitude": 95,
    "maxlongitude": 141,
    "limit": 1000
}

response = requests.get(url, params=params)
data = response.json()

# Parse data
records = []
for feature in data['features']:
    props = feature['properties']
    coords = feature['geometry']['coordinates']
    records.append({
        'longitude': coords[0],
        'latitude': coords[1],
        'depth': coords[2],
        'magnitude': props['mag'],
        'location': props['place'],
        'time': datetime.utcfromtimestamp(props['time']/1000).strftime('%Y-%m-%d')
    })

df = pd.DataFrame(records)

# Fungsi warna marker
def get_color(mag):
    if mag >= 6.0:
        return 'red'
    elif mag >= 5.5:
        return 'orange'
    else:
        return 'green'

# Buat peta
m = folium.Map(
    location=[-2.5, 118],
    zoom_start=5,
    tiles='https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png',
    attr='CartoDB'
)

# Tambah marker — bagian ini yang hilang!
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=row['magnitude'] * 2,
        color=get_color(row['magnitude']),
        fill=True,
        fill_opacity=0.7,
        popup=folium.Popup(
            f"<b>Lokasi:</b> {row['location']}<br>"
            f"<b>Magnitude:</b> {row['magnitude']}<br>"
            f"<b>Kedalaman:</b> {row['depth']} km<br>"
            f"<b>Tanggal:</b> {row['time']}",
            max_width=250
        )
    ).add_to(m)

# Tambah legend
legend_html = """
<div style="
    position: absolute;
    bottom: 30px;
    left: 30px;
    z-index: 1000;
    background-color: white;
    padding: 15px;
    border-radius: 8px;
    border: 1px solid #ccc;
    font-family: Arial, sans-serif;
    font-size: 13px;
    box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
">
    <b>Magnitudo Gempa</b><br><br>
    <span style="color:green;">●</span> M 5.0 – 5.5 &nbsp;(Sedang)<br>
    <span style="color:orange;">●</span> M 5.5 – 6.0 &nbsp;(Kuat)<br>
    <span style="color:red;">●</span> M ≥ 6.0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Sangat Kuat)<br><br>
    <small style="color:gray;">Sumber: USGS | 2020–2025</small>
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))
# Simpan sebagai HTML
m.save("peta_gempa_indonesia_2020_2025.html")
print(f"Peta berhasil disimpan! Total gempa: {len(df)}")