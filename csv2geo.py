"""
Script that takes a .csv file with with any number of EEG coordinates and trasforms it to a 3D .geo file 
For meshing EEG nets with individualized head models.
By Ido Haber March 1, 2024
"""

# You have to make sure that the CODEC is UTF-8 otherwise it will fail.
# If in doubt - open your file and Safe it as ".csv".
import csv


def format_electrode_data(INPUT_PATH, OUTPUT_PATH):
    with open(INPUT_PATH, "r", encoding="utf-8") as csvfile, open(
        OUTPUT_PATH, "w", encoding="utf-8"
    ) as outputfile:
        csvreader = csv.reader(csvfile)
        outputfile.write('View""{\n')

        for row in csvreader:
            # Assuming columns are in the order of ID, X, Y, Z, Name
            # Adjust the indices according to your CSV file
            x, y, z, name = row[1], row[2], row[3], row[4]
            outputfile.write(f"SP({x}, {y}, {z}){{0}};\n")
            outputfile.write(f'T3({x}, {y}, {z}, 0){{"{name}"}};')

        # Append the provided block at the end

        # fmt: off
        outputfile.write("""};\n
myView = PostProcessing.NbViews-1;
View[myView].PointType=1;
View[myView].PointSize=6;
View[myView].LineType=1;
View[myView].LineWidth=2; """)
        # fmt: on


INPUT_PATH = "/Users/idohaber/Desktop/Projects/16_Individualized_models/example_dataset/EGI_256.csv"
OUTPUT_PATH = "/Users/idohaber/Desktop/Projects/16_Individualized_models/EGI_256b.geo"


# Replace 'your_input.csv' and 'your_output.txt' with your actual file paths
format_electrode_data(INPUT_PATH, OUTPUT_PATH)
