#Import
import sys
from pathlib import Path
#modules
from modules.converter import Convert_images

if __name__ == "__main__":
    path_folder = Path(sys.argv[1])
    output_format = sys.argv[2]
    output_folder = Path(sys.argv[1] +"-"+output_format)

    Convert_images(path_folder,output_folder,output_format)