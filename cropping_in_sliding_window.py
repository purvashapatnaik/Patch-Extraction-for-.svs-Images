# from _typeshed import NoneType
import argparse
import os
from math import ceil
from os import listdir
from os.path import isfile, join
import cv2

import openslide
from PIL import Image

compression_factor = 3
window_size = 3000
Image.MAX_IMAGE_PIXELS = 1e10


def cropping_in_sliding_window(image_name, output_path):  # converts svs image with meta data into just the jpeg image

    img = openslide.OpenSlide(image_name)
    width, height = img.level_dimensions[0]
    print ('width:', width)
    print ('height:', height)

    increment_x = int(ceil(width / window_size))
    print ('increment_x:', increment_x)
    increment_y = int(ceil(height / window_size))
    print ('increment_y:', increment_y)

    print("converting", image_name, "with width", width, "and height", height)

    for incre_x in range(increment_x):  # have to read the image in patches since it doesn't let me do it for larger things
        for incre_y in range(increment_y):

            begin_x = window_size * incre_x
            end_x = min(width, begin_x + window_size)
            begin_y = window_size * incre_y
            end_y = min(height, begin_y + window_size)
            patch_width = end_x - begin_x
            patch_height = end_y - begin_y

            patch = img.read_region((begin_x, begin_y), 0, (patch_width, patch_height))
            patch.load()
                
            patch_rgb = Image.new("RGB", patch.size, (225,225,225))
            patch_rgb.paste(patch, mask=patch.split()[3])

            # compress the image
            patch_rgb = patch_rgb.resize((int(patch_rgb.size[0] / compression_factor), int(patch_rgb.size[1] / compression_factor)), Image.ANTIALIAS)



            # save the image
            output_subfolder = join(output_path, image_name.split('/')[-1][:-4])
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)
            output_image_name = join(output_subfolder, image_name.split('/')[-1][:-4] + '_' + str(incre_x) + '_' + str(incre_y) + '.jpg')
            patch_rgb.save(output_image_name)

            w = patch_rgb.size[0]
            h = patch_rgb.size[1]

            image = cv2.imread(output_image_name)
            gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            sift = cv2.xfeatures2d.SIFT_create()
            kp = sift.detect(gray,None)
            kp, dsc = sift.compute(gray, kp)
            
            if (dsc is None) or len(dsc) <= 499 or (not(h == 1000 and w == 1000)):
                print ('removing', output_image_name)
                os.remove(output_image_name)

            else:
                print (output_image_name)
                print (len(dsc))
                print (patch_rgb.size)

    for incre_x in range(increment_x):  # have to read the image in patches since it doesn't let me do it for larger things
        for incre_y in range(increment_y):

            begin_x = window_size * incre_x
            begin_x = begin_x + 500
            print ('begin_x', begin_x)
            end_x = min(width, begin_x + window_size)
            begin_y = window_size * incre_y
            print ('begin_y', begin_y)
            end_y = min(height, begin_y + window_size)
            patch_width = end_y - begin_y
            print ('patch_width:', patch_width)
            patch_height = end_y - begin_y
            print ('patch_height:', patch_height)

            #only continue in this loop if patch_width and patch_height are positive numbers

            if (patch_width>=1 and patch_height>=1):
                patch = img.read_region((begin_x, begin_y), 0, (patch_width, patch_height))
                patch.load()
                patch_rgb = Image.new("RGB", patch.size, (225,225,225))
                patch_rgb.paste(patch, mask=patch.split()[3])
                # compress the image
                patch_rgb = patch_rgb.resize((int(patch_rgb.size[0] / compression_factor), int(patch_rgb.size[1] / compression_factor)), Image.ANTIALIAS)



            # save the image
            output_subfolder = join(output_path, image_name.split('/')[-1][:-4])
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)
            output_image_name = join(output_subfolder, image_name.split('/')[-1][:-4] + '_' + str(incre_x+0.5) + '_' + str(incre_y+0.5) + '.jpg')
            patch_rgb.save(output_image_name)

            w = patch_rgb.size[0]
            h = patch_rgb.size[1]

            image = cv2.imread(output_image_name)
            gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            sift = cv2.xfeatures2d.SIFT_create()
            kp = sift.detect(gray,None)
            kp, dsc = sift.compute(gray, kp)
            
            if (dsc is None) or len(dsc) <= 499 or (not(h == 1000 and w == 1000)):
                print ('removing', output_image_name)
                os.remove(output_image_name)

            else:
                print (output_image_name)
                print (len(dsc))
                print (patch_rgb.size)

    for incre_x in range(increment_x):  # have to read the image in patches since it doesn't let me do it for larger things
        for incre_y in range(increment_y):

            begin_x = window_size * incre_x
            print ('begin_x', begin_x)
            end_x = min(width, begin_x + window_size)
            begin_y = window_size * incre_y
            begin_y = begin_y + 500
            print ('begin_y', begin_y)
            end_y = min(height, begin_y + window_size)
            patch_width = end_y - begin_y
            print ('patch_width:', patch_width)
            patch_height = end_y - begin_y
            print ('patch_height:', patch_height)

            #only continue in this loop if patch_width and patch_height are positive numbers

            if (patch_width>=1 and patch_height>=1):
                patch = img.read_region((begin_x, begin_y), 0, (patch_width, patch_height))
                patch.load()
                patch_rgb = Image.new("RGB", patch.size, (225,225,225))
                patch_rgb.paste(patch, mask=patch.split()[3])
                # compress the image
                patch_rgb = patch_rgb.resize((int(patch_rgb.size[0] / compression_factor), int(patch_rgb.size[1] / compression_factor)), Image.ANTIALIAS)



            # save the image
            output_subfolder = join(output_path, image_name.split('/')[-1][:-4])
            if not os.path.exists(output_subfolder):
                os.makedirs(output_subfolder)
            output_image_name = join(output_subfolder, image_name.split('/')[-1][:-4] + '_' + str(incre_x+0.55) + '_' + str(incre_y+0.55) + '.jpg')
            patch_rgb.save(output_image_name)

            w = patch_rgb.size[0]
            h = patch_rgb.size[1]

            image = cv2.imread(output_image_name)
            gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            sift = cv2.xfeatures2d.SIFT_create()
            kp = sift.detect(gray,None)
            kp, dsc = sift.compute(gray, kp)
            
            if (dsc is None) or len(dsc) <= 499 or (not(h == 1000 and w == 1000)):
                print ('removing', output_image_name)
                os.remove(output_image_name)

            else:
                print (output_image_name)
                print (len(dsc))
                print (patch_rgb.size)


parser = argparse.ArgumentParser()
parser.add_argument("--input_folder", type=str, help="input folder")
parser.add_argument("--output_folder", type=str, help="output folder")
parser.add_argument("--start_at", type=str, default=None, help="resume from a certain filename")
args = parser.parse_args()

input_folder = args.input_folder
output_folder = args.output_folder
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

image_names = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
if '.DS_Store' in image_names:
    image_names.remove('.DS_Store')

if args.start_at is not None:
    start = image_names.index(args.start_at)
    print("skipping the first", start)
    image_names = image_names[start + 2:]

for image_name in image_names:
    full_image_path = input_folder + '/' + image_name
    output_path = output_folder + '/'
    cropping_in_sliding_window(full_image_path, output_path)