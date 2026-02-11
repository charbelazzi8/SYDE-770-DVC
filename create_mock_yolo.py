from PIL import Image, ImageDraw
import os

# Create directories for images and labels
os.makedirs("images", exist_ok=True)
os.makedirs("labels", exist_ok=True)

# Generate mock images
for i in range(3):
    img = Image.new("RGB", (256, 256), color=(i * 50, i * 50, i * 50))
    draw = ImageDraw.Draw(img)
    draw.rectangle([50, 50, 200, 200], outline="red", width=3)  # Simulated object
    img.save(f"images/image_{i}.jpg")

# Generate YOLO-format labels
labels = [
    "0 0.5 0.5 0.6 0.6\n",  # Class 0
    "1 0.4 0.4 0.3 0.3\n",  # Class 1
    "0 0.3 0.3 0.5 0.5\n"   # Class 0
]
for i, label in enumerate(labels):
    with open(f"labels/image_{i}.txt", "w") as f:
        f.write(label)

print("YOLO dataset created.")
