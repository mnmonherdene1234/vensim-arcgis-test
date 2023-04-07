from arcgis.gis import GIS
from arcgis.geocoding import reverse_geocode
from arcgis.geometry import Point

gis = GIS(api_key="AAPK4ff8924cb8244c39bc845c0a78dae31drQ7ORcNDpIuIKL4bKChicSKMf8f5ufzBqem5RoEA8Pdy4aIf_V71MivCqwYHCe0W")

unknown_pt = Point({
    'Y': 47.9196434,
    'X': 106.9163444,
})

address = reverse_geocode(location=unknown_pt)
print(address)
