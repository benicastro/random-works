# Import required libraries/modules
from rembg import remove
from PIL import Image

# Define input/output variables
input_path = ".\\images\\astroc.jpg"
output_path = ".\\images\\astroc.png"

# Open the input image
input_img = Image.open(input_path)

# Perform background removal and save
output = remove(input_img)
output.save(output_path)
