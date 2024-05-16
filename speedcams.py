
import csv
from pyov2.file import list_to_ov2 
from pyov2 import ov2




def csv_to_ov2(csv_path, ov2_path, skip_header=True, dialect='excel', lat=3,lon=4,id=0,prefix='Camera '):
    """
        Convert a csv to an ov2 file.
        The csv should consist of at least three columns.
        Use dialect parameter to fit your csv.

        Parameters
        ----------
        csv_path : str
            Path of csv file to convert.
        ov2_path : str
            Path where to save ov2 file.
        skip_header : bool
            If the csv contains headers use True (default) otherwise use False.
        dialect : str
            Default is 'semicolon' but you can use 'excel' for comma seperated csv.
        lat : 
           Is the latitude column index (default is 3)
        lon : 
            Is the longitude column index (default is 4)
        id :
            Is the label suffix column index (default is 0)
    """

    if not ov2_path.endswith('.ov2'):
        ov2_path += '.ov2'

    count = 0
    with open(csv_path, 'r', newline='') as in_file:
        with open(ov2_path, 'wb') as target_file:
            reader = csv.reader(in_file, dialect=dialect)

            if skip_header:
                next(reader)

            for row in reader:
                longitude = float(row[lon])
                latitude = float(row[lat])
                label = f"{prefix}{row[id]}"
                #print( f"lon={longitude}, lat={latitude}, label={label}")
                buff = ov2.serialize(longitude, latitude, label.strip())
                target_file.write(buff)
                count += 1

            print(f"Wrote {count} records to {ov2_path}")


# The Automated_Speed_Enforcement_Camera_Locations.csv file is available at:
# https://open.ottawa.ca/datasets/ottawa::automated-speed-enforcement-camera-locations/explore


if __name__ == '__main__':
    csv_to_ov2('Automated_Speed_Enforcement_Camera_Locations.csv', 'Speed_Cameras.ov2', lat=3, lon=4, id=0, prefix='Camera ')


