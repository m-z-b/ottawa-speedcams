#
# speedcams.py
# 
# A Python script to generate files which can be imported into a GPS to 
# warn if you are approaching a speed camera location
#
# See the README file for more information
#
# Mike Bell, Albion Research Ltd., 2024
#
# NO WARRANTIES - USE ENTIRELY AT OWN RISK
#




import urllib.request,json
from pathlib import Path

from pyov2 import ov2

# See the README.md file for how to get the API URL

API_URL = "https://services.arcgis.com/G6F8XLCl5KtAlZ2G/arcgis/rest/services/Automated_Speed_Enforcement_Camera_Locations/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson"

def get_json(url):
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
        return data 

def generate_files( data: str, ov2_path: Path ):
  if not ov2_path.endswith('.ov2'):
      ov2_path += '.ov2'

  # TomTom devices
  with open(ov2_path, 'wb') as target_file: 
      for feature in data['features']:
          longitude = feature['properties']['Longitude']
          latitude = feature['properties']['Latitude']
          label = feature['properties']['ID']
          buff = ov2.serialize(longitude, latitude, F"Camera {label}")
          target_file.write(buff)
  print(f"Wrote {len(data['features'])} camera locations to {ov2_path}")

def main():
    data = get_json(API_URL)
    generate_files(data, 'Speed_Cameras.ov2')# G


if __name__ == '__main__':
    main()


