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

  1. Download The current `Automated_Speed_Enforcement_Camera_Locations.csv` from 
    [https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-locations/explore](https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-locations/explore)
  2. Clone this repo and cd into the repo directory.
  3. Install the `pyov2` package.
  4. Run `python speedcams.py` to generate an updated `Speed_Cameras.ov2` file   
  5. If you know what you're doing, Issue a pull request 
  6. If you're not quite sure, create an issue requesting an update.

## If you have graphic design abilities...

The `Speed_Cameras.bmp` file is currently a pretty awful 16x16 bitmap. 

It's displayed above a position marker on a TomTom. Something which looks
a bit like a red camera would be much better.  

Don't use any clever bitmap formats - they won't work on all devices.

## Last Speed Camera Update
2024-05-16

