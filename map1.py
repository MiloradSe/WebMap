import folium

map = folium.Map(location=[45.25231,19.83561], tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', attr = 'Google', zoom_start=14)

fg_cof = folium.FeatureGroup(name="Kafa za poneti", show=True)

fg_cof.add_child(folium.Marker(location=[45.260275, 19.830411], popup="Kafeterija ZRNO", icon=folium.Icon(icon='fa-coffee', prefix='fa', color='black')))
fg_cof.add_child(folium.Marker(location=[45.25056, 19.84829], popup="Coffee To Go", icon=folium.Icon(icon='fa-coffee', prefix='fa', color='black')))
fg_cof.add_child(folium.Marker(location=[45.25985, 19.82166], popup="Skočko ", icon=folium.Icon(icon='fa-coffee', prefix='fa', color='black')))
fg_cof.add_child(folium.Marker(location=[45.257451, 19.850577], popup="Pržionica kafe", icon=folium.Icon(icon='fa-coffee', prefix='fa', color='black')))

fg_gal = folium.FeatureGroup(name="Galerije i ateljei", show=True)

fg_gal.add_child(folium.Marker(location=[45.25871, 19.84106], popup="Atelje Aleksandar Mirkovic", icon=folium.Icon(icon='fa-paint-brush', prefix='fa', color='darkblue')))
fg_gal.add_child(folium.Marker(location=[45.25309, 19.83997], popup="Atelje Arhaica", icon=folium.Icon(icon='fa-paint-brush', prefix='fa', color='darkblue')))
fg_gal.add_child(folium.Marker(location=[45.24774, 19.83471], popup="Atelje Artworkshopmi", icon=folium.Icon(icon='fa-paint-brush', prefix='fa', color='darkblue')))
fg_gal.add_child(folium.Marker(location=[45.25277, 19.84550], popup="Galerija Matice Srpske", icon=folium.Icon(icon='fa-picture-o', prefix='fa', color='darkblue')))
fg_gal.add_child(folium.Marker(location=[45.25229, 19.84517], popup="Galerija likovne umetnosti Rajko Mamuzić", icon=folium.Icon(icon='fa-picture-o', prefix='fa', color='darkblue')))

fg_mus = folium.FeatureGroup(name="Muzeji", show=True)

fg_mus.add_child(folium.Marker(location=[45.25628, 19.85167], popup="Muzej Vojvodine", icon=folium.Icon(icon='fa-university', prefix='fa', color='darkgreen')))
fg_mus.add_child(folium.Marker(location=[45.25224, 19.86201], popup="Muzej grada Novog Sada", icon=folium.Icon(icon='fa-university', prefix='fa', color='darkgreen')))
fg_mus.add_child(folium.Marker(location=[45.25292, 19.84603], popup="Spomen-zbirka Pavla Beljanskog", icon=folium.Icon(icon='fa-university', prefix='fa', color='darkgreen')))

map.add_child(fg_cof)
map.add_child(fg_gal)
map.add_child(fg_mus)

map.add_child(folium.LayerControl())

map.save("Map1.html")
