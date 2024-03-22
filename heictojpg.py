# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 09:45:32 2023

@author: adon.augustin
"""

import os
import PIL
from PIL import Image
import pillow_heif
import pathlib
from pillow_heif import register_heif_opener

register_heif_opener()
path=pathlib.Path(__file__).parent.resolve()
""" 
create a directory
"""
conv_file_path=(str(path)+"\\convertedFiles")
path_exist=os.path.exists(conv_file_path)
if(path_exist==False):
    os.mkdir(str(path)+"\\ConvertedFiles")  
for filename in os.listdir(path):
    if filename.endswith(".heic"):
        im = Image.open(filename)
        im.save(conv_file_path+"\\"+filename.split('.')[0]+".jpg")
        