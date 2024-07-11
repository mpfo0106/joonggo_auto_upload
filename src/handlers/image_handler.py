import os
from config import PROJECT_ROOT, IMAGES_DIR


class ImageHandler:
    @staticmethod
    def get_image_files(directory_name):
        image_directory = os.path.join(PROJECT_ROOT, IMAGES_DIR, directory_name)
        return [
            os.path.join(image_directory, f)
            for f in os.listdir(image_directory)
            if f.lower().endswith((".png", ".jpg", ".jpeg", ".gif"))
        ]
