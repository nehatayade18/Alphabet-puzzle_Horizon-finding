#!/usr/local/bin/python3
#
# Authors: [Neha Tayade ntayade, Viral Prajapati vkprajap]
#
# Mountain ridge finder
# Based on skeleton code by D. Crandall, Oct 2019
#

from PIL import Image
from numpy import *
from scipy.ndimage import filters
import sys
import imageio
import numpy as np
import copy
# calculate "Edge strength map" of an image
#
def edge_strength(input_image):
    grayscale = array(input_image.convert('L'))
    filtered_y = zeros(grayscale.shape)
    filters.sobel(grayscale,0,filtered_y)
    return sqrt(filtered_y**2)

# draw a "line" on an image (actually just plot the given y-coordinates
#  for each x-coordinate)
# - image is the image to draw on
# - y_coordinates is a list, containing the y-coordinates and length equal to the x dimension size
#   of the image
# - color is a (red, green, blue) color triple (e.g. (255, 0, 0) would be pure red
# - thickness is thickness of line in pixels
#
def draw_edge(image, y_coordinates, color, thickness):
    for (x, y) in enumerate(y_coordinates):
        for t in range( int(max(y-int(thickness/2), 0)), int(min(y+int(thickness/2), image.size[1]-1 )) ):
            image.putpixel((x, t), color)
    return image

def emission_probability_calculator_simple(edge_strength):
    emission_prob=copy.deepcopy(edge_strength)
    emission_prob=np.transpose(emission_prob)
    for i in range(len(emission_prob)):
        emission_prob[i]=np.log(emission_prob[i]/np.sum(emission_prob[i])+0.0001)
    return emission_prob
# main program
#
(input_filename, gt_row, gt_col) = (sys.argv[1], sys.argv[2], sys.argv[3])

# load in image 
input_image = Image.open(input_filename)

# compute edge strength mask
edge_strength = edge_strength(input_image)
imageio.imwrite('edges.jpg', uint8(255 * edge_strength / (amax(edge_strength))))

#ridge=[np.argmax(i) for i in np.transpose(edge_strength)]
emission_prob = emission_probability_calculator_simple(edge_strength)
ridge=[np.argmax(i) for i in np.transpose(edge_strength)]
#for i in np.transpose(emission_prob):
#    ridge+=[np.argmax(i)]
# output answer
imageio.imwrite("output.jpg", draw_edge(input_image, ridge, (255, 0, 0), 5))
