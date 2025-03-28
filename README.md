# Speed Cameras of Ottawa

Got a TomTom and want to be warned about Ottawa Speed Cameras?

Grab the `Speed_Cameras.ov2` and `Speed_Cameras.bmp` files from this 
repository.

  1. Connect your TomTom device to your computer
  2. Copy the `Speed_Cameras.ov2` and `Speed_Cameras.bmp` files to the map 
     directory (e.g. `USA_Canada`) on your TomTom
  3. Disconnect your TomTom device and allow it to reboot.
  4. Under the *Manage POIs* option select *Warn when near POI*. 
  5. Choose how near you have to approach the Camera
     to get a warning, and what the appropriate warning should be.

## Files not up-to-date and know a little Python?

  1. Clone this repo and cd into the repo directory.
  2. Install the `pyov2` package.
  3. Run `python speedcams.py` to generate an updated `Speed_Cameras.ov2` file   
  4. If you know what you're doing, Issue a pull request 
  5. If you're not quite sure, create an issue requesting an update.
  6. API call not working - see below.

## If you have graphic design abilities...

The `Speed_Cameras.bmp` file is currently a pretty awful 16x16 bitmap. 

It's displayed above a position marker on a TomTom. Something which looks
a bit like a red camera would be much better.  

Don't use any clever bitmap formats - they won't work on all devices.

## Got a Garmin or another make?

 1. Update `speedcams.py` to generate the correct CSV or other format files. 
 2. Submit a pull request.

## License

This software is released under the MIT license - see `LICENSE.txt`

## Last Speed Camera Update
2025-01-14

## API Call out of date?

The API URL in the Python script can be obtained as follows.
 
 1. Go to [https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-locations]
 2. Click on *I want to use this...* then *View API Resources*
 3. Copy the GeoJSON API call: [https://services.arcgis.com/G6F8XLCl5KtAlZ2G/arcgis/rest/services/Automated_Speed_Enforcement_Camera_Locations/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson](API Call)
 4. Update the `speedcams.py` `API_URL` value in `speedcams.py`.
 5. in the project directory, run (using uv - recommended) `uv run speedcams.py` 
 6. Submit a pull request for the updated URL and the updated data.

