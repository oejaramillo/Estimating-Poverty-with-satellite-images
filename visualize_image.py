import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Load TIFF file
tiff_path = input("Ubicación del archivo (.tiff): ")

with rasterio.open(tiff_path) as src:
    img = src.read()  # Read all bands (shape: [bands, height, width])

# Print image shape
print(f"Image shape: {img.shape}")  # (bands, height, width)

# Check pixel value range
print(f"Min pixel value: {img.min()}, Max pixel value: {img.max()}")

# Extract RGB bands (Assuming B02, B03, B04 are RGB)
rgb = np.stack([img[0], img[1], img[2]], axis=-1)

# Fix: Convert from [0,1] to uint8 [0,255]
rgb = (rgb * 255).astype(np.uint8)

# Plot the image
plt.figure(figsize=(10, 10))
plt.imshow(rgb)
plt.axis("off")
plt.title("TIFF Image (RGB)")
plt.show()
