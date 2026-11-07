"""CP101 Lab 10: example station map. Requires folium (pip install folium)."""
import folium

stations = [
    ("Downtown Berkeley", 37.870, -122.268),
    ("North Berkeley", 37.874, -122.283),
    ("Ashby", 37.853, -122.270),
    ("MacArthur", 37.829, -122.268),
    ("Rockridge", 37.845, -122.252),
    ("19th St Oakland", 37.808, -122.269),
]
m = folium.Map(location=[37.850, -122.269], zoom_start=12)
for name, lat, lon in stations:
    folium.Marker((lat, lon), tooltip=name).add_to(m)
    folium.Circle((lat, lon), radius=800, color="#e16a8d",
                  fill=True, fill_opacity=0.11).add_to(m)
m.save("interactive_map.html")
print("Wrote interactive_map.html. Circles are straight-line, not walking distances.")
