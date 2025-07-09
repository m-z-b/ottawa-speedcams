# Speed Cameras of Ottawa

Want to be warned when you are approaching one of the new Ottawa Speed Cameras?

## TomTom Users

Grab the `Speed_Cameras.ov2` and `Speed_Cameras.bmp` files from this 
repository.

  1. Connect your TomTom device to your computer
  2. Copy the `Speed_Cameras.ov2` and `Speed_Cameras.bmp` files to the map 
     directory (e.g. `USA_Canada`) on your TomTom
  3. Disconnect your TomTom device and allow it to reboot.
  4. Under the *Manage POIs* option select *Warn when near POI*. 
  5. Choose how near you have to approach the Camera
     to get a warning, and what the appropriate warning should be.

## Garmin Users

Grab the `Speed_Cameras.csv` from this repository.

  1. Download and install the **POILoader** software from the Garmin website. 
  2. Connect your Garmin device to your computer.
  3. Run the POI Loader program and follow its instructions.
  4. Select the folder containing the `Speed_Cameras.csv` file.
  5. Select the option to _Install new custom POIs onto your device_.
  6. **Select _Manual_ mode, not _Express_ mode.**
  7. Set the option to warn when within (say) 150m of a POI - if you need a greater
  distance you're driving much too fast.
  8. Upload to the GPS. Restart the device. 
  9. If you browse the Points of Interest Categories, you should find the speed cameras under__Custom POIs_.


## Other Device Users

There is probably a way of importing the `Speed_Cameras.csv` file. 
If you're a developer, issue a pull request to:
 - Update the instructions in this document
 - Modify the `speedcams.py` file to generate another format.


# Developer?

## Files not up-to-date and know a little Python?

  1. Clone this repo and cd into the repo directory.
  2. Experienced pythonista? `uv run speedcams.py` should update the files.
  3. No `uv`? Install the `pyov2` package.
  4. Run `python speedcams.py` to generate an updated `Speed_Cameras.ov2` file   
  5. If you know what you're doing, Issue a pull request 
  6. If you're not quite sure, create an issue requesting an update.
  7. API call not working - see below.

## If you have graphic design abilities...

The `Speed_Cameras.bmp` file is currently a pretty awful 16x16 bitmap. 

It's displayed above a position marker on a TomTom. Something which looks
a bit like a red camera would be much better.  

Don't use any clever bitmap formats - they won't work on all devices.


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

