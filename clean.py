import os
from PIL import Image

def clean_dataset(root_dir):
    bad_files = 0
    for label in ['cat', 'dog']:
        folder = os.path.join(root_dir, label)
        for fname in os.listdir(folder):
            path = os.path.join(folder, fname)
            try:
                with Image.open(path) as img:
                    img.verify()  # Verify file is a valid image
            except Exception as e:
                print(f"Removing invalid image: {path} ({e})")
                os.remove(path)
                bad_files += 1
    print(f"Removed {bad_files} bad images.")

clean_dataset("data/train")