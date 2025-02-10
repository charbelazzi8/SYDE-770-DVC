import os

# Check if directories exist
if not os.path.exists("images") or not os.path.exists("labels"):
    raise FileNotFoundError("Required directories 'images' or 'labels' are missing.")

# Simulate training
print("Training YOLO model...")
print(f"Number of images: {len(os.listdir('images'))}")
print(f"Number of labels: {len(os.listdir('labels'))}")

# Simulate creating a model file
with open("model.pth", "w") as f:
    f.write("dummy model")
