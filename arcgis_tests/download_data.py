from arcgis.gis import GIS
from pathlib import Path
from zipfile import ZipFile

gis = GIS()

public_data_item_id = 'a04933c045714492bda6886f355416f2'
# `ContentManager.get` will return `None` if there is no Item with ID `a04933c045714492bda6886f355416f2`
data_item = gis.content.get(public_data_item_id)
print(data_item)

data_path = Path('./data')
if not data_path.exists():
    data_path.mkdir()
zip_path = data_path.joinpath('LA_Hub_Datasets.zip')
extract_path = data_path.joinpath('LA_Hub_datasets')
data_item.download(save_path=data_path)

zip_file = ZipFile(zip_path)
zip_file.extractall(path=data_path)

files = [file.name for file in extract_path.glob('*')]
print(files)
