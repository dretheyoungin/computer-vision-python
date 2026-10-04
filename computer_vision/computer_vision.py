import numpy as np
from PIL import Image

print("Bot: Initializing Computer Vision Matrix Pipeline...")

# 1. Simulate a digital camera image using raw numbers (Pixels)
# This creates a grid of 100x100 pixels filled with gray and white pattern data
raw_pixel_grid = np.random.randint(0, 255, (100, 100, 3), dtype=np.uint8)

print("\nBot: Loading pixel multi-dimensional array into memory layer...")
# 2. Image Ingestion: Turn the raw mathematical numbers into an actual image asset
simulated_camera_frame = Image.fromarray(raw_pixel_grid)

# 3. Metadata Extraction: Read the dimensions and color depth channel maps
width, height = simulated_camera_frame.size
color_channels = len(simulated_camera_frame.getbands())

print(f"-> Camera Frame Width: {width}px")
print(f"-> Camera Frame Height: {height}px")
print(f"-> Color Data Channels: {color_channels} (RGB)")

print("\nBot: Matrix tracking complete. Exporting image to system drive...")
# 4. Save: Automatically output the image into your portfolio folder!
simulated_camera_frame.save("processed_camera_frame.png")

print("Bot: Success! Computer vision framework generated 'processed_camera_frame.png'.")