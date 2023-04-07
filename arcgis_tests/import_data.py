from arcgis.gis import GIS

gis = GIS(api_key="AAPK4ff8924cb8244c39bc845c0a78dae31drQ7ORcNDpIuIKL4bKChicSKMf8f5ufzBqem5RoEA8Pdy4aIf_V71MivCqwYHCe0W")

trails_properties = {}

geojson_file = 'data/LA_Hub_Datasets/Trails.geojson'
geojson_item = gis.content.add(trails_properties, geojson_file)

trails_service = geojson_item.publish()
print(trails_service)
