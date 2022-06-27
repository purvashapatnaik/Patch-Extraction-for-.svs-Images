# Patch Extraction (Cropping in a Sliding Window)
This project is a part of the thesis titled Automated Detection of Placental Lesions at the University of Ottawa.

#### -- Project Status: [Completed]

## Project Intro/Objective
The purpose of this project is to automate the patch extraction of .svs images captured from placental histological slides. The method of patch extraction is cropping in a sliding window. The objective is to input an .svs image and output a folder containing cropped images in .jpg format.

### Methods Used
* Computer Vision
* Image acquisition, processing, and analysis

### Technologies
* Python
* OpenCV

## Project Description
The image dataset was pre-processed from 166 WSIs captured in ‘.svs’ format from 166 patients. One or more images were cropped from each slide using Aperio ImageScope software, minimizing the amount of empty/white space included in the image and separating the tissue samples into separate images if there were multiple samples present from the same patient on the slide. These 263 cropped images underwent patch extraction using the ‘sliding window’ approach. Briefly, image patches were extracted using a window of size 1000 x 1000 pixels (px) sliding from the top left corner to the right by 500 px and down by 500 px of the cropped images. The total number of patches extracted from one cropped image ranged from 3 – 328 patches, dependent on the amount of tissue on the WSI. 

## Needs of this project
- image data exploration
- image data processing/cleaning
- writeup/reporting/analysis

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.

    *If using offline data mention that and how they may obtain the data from the froup)*
    
3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks) 

5. Follow setup [instructions](Link to file)

## Featured Notebooks/Analysis/Deliverables
* ['Thesis Proposal - Patch Extraction'](link)



## Contact
* purvasha.patnaik@gmail.com
* Feel free to contact me with any questions or if you are interested in my thesis project!
