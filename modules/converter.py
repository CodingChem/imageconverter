import os
from pathlib import Path
#Import module
from PIL import Image

class Convert_images:
    def __init__(self, input_folder, output_folder, output_format):
        self.images = Img_list()
        print("Loading images to memory...")
        self.images.load_images_from_folder(input_folder)
        self.images.save_images(output_folder,output_format)
        print(f"Complete! Files written to '{output_folder}'")
        
class Img:
    def __init__(self, path):
        self.name = path.stem
        self.image = Image.open(path)
    def save(self, path, format):
        print(f"Saving image: {self.name}")
        self.image.save(path.joinpath(self.name+"."+format),format)

class Img_list:
    def __init__(self):
        self.images = []
    def add_image(self, image):
        self.images.append(image)
    def save_images(self, folder, format):
        print("Create folder...")
        os.mkdir(folder)
        print("Folder created.")
        print("Writing image files...")
        for image in self.images:
            image.save(folder,format)
    def load_images_from_folder(self, folder):
        for file in os.listdir(folder):
            path = folder.joinpath(file)
            image = Img(path)
            self.add_image(image)