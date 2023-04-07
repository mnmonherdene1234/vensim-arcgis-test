from arcgis.features import FeatureSet
import geojson

with open("data/LA_Hub_Datasets/Trails.geojson") as f:
    geojson_data = geojson.load(f)

print(geojson_data)

# use the FeatureLayer.from_geojson() method to read the GeoJSON file and create a feature layer object
feature_set = FeatureSet.from_dict(geojson_data)

# iterate through the feature set and print the attributes of each feature
for feature in feature_set.features:
    print(feature.fields)
