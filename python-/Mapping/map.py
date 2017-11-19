import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")

map = folium.Map(location = [40.420424, -74.430486], zoom_start=6, tiles="Mapbox Bright")

lat = list(data["LAT"])
lon = list(data["LON"])
el = list(data["ELEV"])

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif 1000<=elevation < 3000:
        return 'orange'
    else:
        return 'red'

fgv =folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, el):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el) + " m", radius=6, fill_color = color_producer(el), color = 'grey', fill_opacity=.7))

fgp =folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r',encoding='utf-8-sig'),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save("Map1.html")
