# Speed Cameras of Ottawa

This Python script generates an ov2 file which can be used on a TomTom to
warn if a Speed Camera is nearby. 

How to use it:

  1. Connect your TomTom device to your computer
  2. Copy the `Speed_Cameras.ov2` and `Speed_Cameras.bmp` files to the map 
     directory (e.g. `USA_Canada`) on your TomTom
  3. Disconnect your TomTom device and allow it to reboot.
  4. Under the *Manage POIs* option select *Warn when near POI*. 
  5. Choose how near you have to approach the Camera
     to get a warning, and what the appropriate warning should be.

## Updating

The current `Automated_Speed_Enforcement_Camera_Locations.csv` file can be downloaded at:
https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-locations/explore

Run `python speedcams.py` to generate an updated `Speed_Cameras.ov2` file   and issue a pull request for the update.

## Last Speed Camera Update
2024-05-16

