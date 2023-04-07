# import the ArcGIS Python API
from arcgis.gis import GIS

# create a GIS object for your organization
gis = GIS("https://www.arcgis.com",
          "Monhnast_Monherdene_LearnArcGIS", "MnMonherdene0529;")

print(gis.content)
