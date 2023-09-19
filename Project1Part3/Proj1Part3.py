
'''
                                            HCIRA - Project 1 Part 3
                                                    Group 23
                                                     Names: 
                                          Sai Mohan Sujay Kanchumarthi 
                                                Priti Gumaste
'''


from math import pi, atan2, cos, sin, inf, sqrt
from tkinter import *
import tkinter as tk
import numpy as np
import numpy.linalg as linalg
import csv
import os
import random
from lxml import etree


#This class has the templates to all the 16 gestures that has been discussed in the paper. 
class template():
    
    def __init__(self, name, points):
        super(template, self).__init__()
        self.name = name
        self.points = points


#UNISTROKES = [
#    ("triangle",
#            [[137, 139], [135, 141], [133, 144], [132, 146], [130, 149], [128, 151], [126, 155], [123, 160], [120, 166],
#             [116, 171], [112, 177], [107, 183], [102, 188], 
#             [100, 191], [95, 195], [90, 199], [86, 203], [82, 206],
#             [80, 209], [75, 213], [73, 213], [70, 216], [67, 219], 
#             [64, 221], [61, 223], [60, 225], [62, 226],
#             [65, 225], [67, 226], [74, 226], [77, 227], [85, 229], 
#             [91, 230], [99, 231], [108, 232], [116, 233],
#             [125, 233], [134, 234], [145, 233], [153, 232], [160, 233], 
#             [170, 234], [177, 235], [179, 236], [186, 237],
#             [193, 238], [198, 239], [200, 237], [202, 239], [204, 238], 
#             [206, 234], [205, 230], [202, 222], [197, 216],
#             [192, 207], [186, 198], [179, 189], [174, 183], [170, 178], 
#             [164, 171], [161, 168], [154, 160], [148, 155],
#             [143, 150], [138, 148], [136, 148]]), 

   # ("x",
   #  [[87, 142], [89, 145], [91, 148], [93, 151], [96, 155], [98, 157], [100, 160], [102, 162], [106, 167], [108, 169],
   #   [110, 171], [115, 177], [119, 183], [123, 189], [127, 193], [
   #       129, 196], [133, 200], [137, 206], [140, 209],
   #   [143, 212], [146, 215], [151, 220], [153, 222], [155, 223], [
   #       157, 225], [158, 223], [157, 218], [155, 211],
   #   [154, 208], [152, 200], [150, 189], [148, 179], [147, 170], [
   #       147, 158], [147, 148], [147, 141], [147, 136],
   #   [144, 135], [142, 137], [140, 139], [135, 145], [131, 152], [
   #       124, 163], [116, 177], [108, 191], [100, 206],
   #   [94, 217], [91, 222], [89, 225], [87, 226], [87, 224]]), 

   #("rectangle",
   #          [[78, 149], [78, 153], [78, 157], [78, 160], [79, 162], [79, 164], [79, 167], [79, 169], [79, 173],
   #           [79, 178], [79, 183], [80, 189], [80, 193], [80, 198], [
   #               80, 202], [81, 208], [81, 210], [81, 216],
   #           [82, 222], [82, 224], [82, 227], [83, 229], [83, 231], [
   #               85, 230], [88, 232], [90, 233], [92, 232],
   #           [94, 233], [99, 232], [102, 233], [106, 233], [109, 234], [
   #               117, 235], [123, 236], [126, 236], [135, 237],
   #           [142, 238], [145, 238], [152, 238], [154, 239], [
   #               165, 238], [174, 237], [179, 236], [186, 235],
   #           [191, 235], [195, 233], [197, 233], [200, 233], [
   #               201, 235], [201, 233], [199, 231], [198, 226],
   #           [198, 220], [196, 207], [195, 195], [195, 181], [
   #               195, 173], [195, 163], [194, 155], [192, 145],
   #           [192, 143], [192, 138], [191, 135], [191, 133], [
   #               191, 130], [190, 128], [188, 129], [186, 129],
   #           [181, 132], [173, 131], [162, 131], [151, 132], [
   #               149, 132], [138, 132], [136, 132], [122, 131],
   #           [120, 131], [109, 130], [107, 130], [90, 132], [81, 133], [76, 133]]),
   #("circle",
   #       [[127, 141], [124, 140], [120, 139], [118, 139], [116, 139], [111, 140], [109, 141], [104, 144], [100, 147],
   #        [96, 152], [93, 157], [90, 163], [87, 169], [85, 175], [
   #            83, 181], [82, 190], [82, 195], [83, 200], [84, 205],
   #        [88, 213], [91, 216], [96, 219], [103, 222], [108, 224], [
   #            111, 224], [120, 224], [133, 223], [142, 222],
   #        [152, 218], [160, 214], [167, 210], [173, 204], [178, 198], [
   #            179, 196], [182, 188], [182, 177], [178, 167],
   #        [170, 150], [163, 138], [152, 130], [143, 129], [140, 131], [129, 136], [126, 139]]),

   #("check",
   #      [[91, 185], [93, 185], [95, 185], [97, 185], [100, 188], [102, 189], [104, 190], [106, 193], [108, 195],
   #       [110, 198], [112, 201], [114, 204], [115, 207], [117, 210], [
   #           118, 212], [120, 214], [121, 217], [122, 219],
   #       [123, 222], [124, 224], [126, 226], [127, 229], [129, 231], [
   #           130, 233], [129, 231], [129, 228], [129, 226],
   #       [129, 224], [129, 221], [129, 218], [129, 212], [129, 208], [
   #           130, 198], [132, 189], [134, 182], [137, 173],
   #       [143, 164], [147, 157], [151, 151], [155, 144], [161, 137], [
   #           165, 131], [171, 122], [174, 118], [176, 114],
   #       [177, 112], [177, 114], [175, 116], [173, 118]]),

   #("caret",
   #      [[79, 245], [79, 242], [79, 239], [80, 237], [80, 234], [81, 232], [82, 230], [84, 224], [86, 220], [86, 218],
   #       [87, 216], [88, 213], [90, 207], [91, 202], [92, 200], [
   #           93, 194], [94, 192], [96, 189], [97, 186], [100, 179],
   #       [102, 173], [105, 165], [107, 160], [109, 158], [112, 151], [
   #           115, 144], [117, 139], [119, 136], [119, 134],
   #       [120, 132], [121, 129], [122, 127], [124, 125], [126, 124], [
   #           129, 125], [131, 127], [132, 130], [136, 139],
   #       [141, 154], [145, 166], [151, 182], [156, 193], [157, 196], [
   #           161, 209], [162, 211], [167, 223], [169, 229],
   #       [170, 231], [173, 237], [176, 242], [177, 244], [179, 250], [181, 255], [182, 257]]),

   #("arrow",
   #      [[68, 222], [70, 220], [73, 218], [75, 217], [77, 215], [80, 213], [82, 212], [84, 210], [87, 209], [89, 208],
   #       [92, 206], [95, 204], [101, 201], [106, 198], [112, 194], [
   #           118, 191], [124, 187], [127, 186], [132, 183],
   #       [138, 181], [141, 180], [146, 178], [154, 173], [159, 171], [
   #           161, 170], [166, 167], [168, 167], [171, 166],
   #       [174, 164], [177, 162], [180, 160], [182, 158], [183, 156], [
   #           181, 154], [178, 153], [171, 153], [164, 153],
   #       [160, 153], [150, 154], [147, 155], [141, 157], [137, 158], [
   #           135, 158], [137, 158], [140, 157], [143, 156],
   #       [151, 154], [160, 152], [170, 149], [179, 147], [185, 145], [
   #           192, 144], [196, 144], [198, 144], [200, 144],
   #       [201, 147], [199, 149], [194, 157], [191, 160], [186, 167], [
   #           180, 176], [177, 179], [171, 187], [169, 189],
   #       [165, 194], [164, 196]]), 

   # ("zig-zag", [[307, 216], [333, 186],
   #        [356, 215], [375, 186], [399, 216], [418, 186]]), 

   # ("left_square_bracket",
   #                    [[140, 124], [138, 123], [135, 122], [133, 123], [130, 123], [128, 124], [125, 125], [122, 124],
   #                     [120, 124], [118, 124], [116, 125], [113, 125], [
   #                         111, 125], [108, 124], [106, 125], [104, 125],
   #                     [102, 124], [100, 123], [98, 123], [95, 124], [
   #                         93, 123], [90, 124], [88, 124], [85, 125],
   #                     [83, 126], [81, 127], [81, 129], [82, 131], [
   #                         82, 134], [83, 138], [84, 141], [84, 144],
   #                     [85, 148], [85, 151], [86, 156], [86, 160], [
   #                         86, 164], [86, 168], [87, 171], [87, 175],
   #                     [87, 179], [87, 182], [87, 186], [88, 188], [
   #                         88, 195], [88, 198], [88, 201], [88, 207],
   #                     [89, 211], [89, 213], [89, 217], [89, 222], [
   #                         88, 225], [88, 229], [88, 231], [88, 233],
   #                     [88, 235], [89, 237], [89, 240], [89, 242], [
   #                         91, 241], [94, 241], [96, 240], [98, 239],
   #                     [105, 240], [109, 240], [113, 239], [116, 240], [
   #                         121, 239], [130, 240], [136, 237], [139, 237],
   #                     [144, 238], [151, 237], [157, 236], [159, 237]]),

   # ("right_bracket",
   #                     [[112, 138], [112, 136], [115, 136], [118, 137], [120, 136], [123, 136], [125, 136], [128, 136],
   #                      [131, 136], [134, 135], [137, 135], [140, 134], [
   #                          143, 133], [145, 132], [147, 132], [149, 132],
   #                      [152, 132], [153, 134], [154, 137], [155, 141], [
   #                          156, 144], [157, 152], [158, 161], [160, 170],
   #                      [162, 182], [164, 192], [166, 200], [167, 209], [
   #                          168, 214], [168, 216], [169, 221], [169, 223],
   #                      [169, 228], [169, 231], [166, 233], [164, 234], [
   #                          161, 235], [155, 236], [147, 235], [140, 233],
   #                      [131, 233], [124, 233], [117, 235], [114, 238], [112, 238]]),

   #("v",
   #  [[89, 164], [90, 162], [92, 162], [94, 164], [95, 166], [96, 169], [97, 171], [99, 175], [101, 178], [103, 182],
   #   [106, 189], [108, 194], [111, 199], [114, 204], [117, 209], [
   #       119, 214], [122, 218], [124, 222], [126, 225],
   #   [128, 228], [130, 229], [133, 233], [134, 236], [136, 239], [
   #       138, 240], [139, 242], [140, 244], [142, 242],
   #   [142, 240], [142, 237], [143, 235], [143, 233], [145, 229], [
   #       146, 226], [148, 217], [149, 208], [149, 205],
   #   [151, 196], [151, 193], [153, 182], [155, 172], [157, 165], [
   #       159, 160], [162, 155], [164, 150], [165, 148],
   #   [166, 146]]), 

   # ("delete",
   #       [[123, 129], [123, 131], [124, 133], [125, 136], [127, 140], [129, 142], [133, 148], [137, 154], [143, 158],
   #        [145, 161], [148, 164], [153, 170], [158, 176], [160, 178], [
   #            164, 183], [168, 188], [171, 191], [175, 196],
   #        [178, 200], [180, 202], [181, 205], [184, 208], [186, 210], [
   #            187, 213], [188, 215], [186, 212], [183, 211],
   #        [177, 208], [169, 206], [162, 205], [154, 207], [145, 209], [
   #            137, 210], [129, 214], [122, 217], [118, 218],
   #        [111, 221], [109, 222], [110, 219], [112, 217], [118, 209], [
   #            120, 207], [128, 196], [135, 187], [138, 183],
   #        [148, 167], [157, 153], [163, 145], [165, 142], [172, 133], [177, 127], [179, 127], [180, 125]]),

   # ("left_curly",
   #                 [[150, 116], [147, 117], [145, 116], [142, 116], [139, 117], [136, 117], [133, 118], [129, 121],
   #                  [126, 122], [123, 123], [120, 125], [118, 127], [
   #                      115, 128], [113, 129], [112, 131], [113, 134],
   #                  [115, 134], [117, 135], [120, 135], [123, 137], [
   #                      126, 138], [129, 140], [135, 143], [137, 144],
   #                  [139, 147], [141, 149], [140, 152], [139, 155], [
   #                      134, 159], [131, 161], [124, 166], [121, 166],
   #                  [117, 166], [114, 167], [112, 166], [114, 164], [
   #                      116, 163], [118, 163], [120, 162], [122, 163],
   #                  [125, 164], [127, 165], [129, 166], [130, 168], [
   #                      129, 171], [127, 175], [125, 179], [123, 184],
   #                  [121, 190], [120, 194], [119, 199], [120, 202], [
   #                      123, 207], [127, 211], [133, 215], [142, 219],
   #                  [148, 220], [151, 221]]), 

   # ("right_curly_brace",
   #                  [[117, 132], [115, 132], [115, 129], [117, 129], [119, 128], [122, 127], [125, 127], [127, 127],
   #                   [130, 127], [133, 129], [136, 129], [138, 130], [
   #                       140, 131], [143, 134], [144, 136], [145, 139],
   #                   [145, 142], [145, 145], [145, 147], [145, 149], [
   #                       144, 152], [142, 157], [141, 160], [139, 163],
   #                   [137, 166], [135, 167], [133, 169], [131, 172], [
   #                       128, 173], [126, 176], [125, 178], [125, 180],
   #                   [125, 182], [126, 184], [128, 187], [130, 187], [
   #                       132, 188], [135, 189], [140, 189], [145, 189],
   #                   [150, 187], [155, 186], [157, 185], [159, 184], [
   #                       156, 185], [154, 185], [149, 185], [145, 187],
   #                   [141, 188], [136, 191], [134, 191], [131, 192], [
   #                       129, 193], [129, 195], [129, 197], [131, 200],
   #                   [133, 202], [136, 206], [139, 211], [142, 215], [
   #                       145, 220], [147, 225], [148, 231], [147, 239],
   #                   [144, 244], [139, 248], [134, 250], [126, 253], [119, 253], [115, 253]]),

   # ("star",
   #     [[75, 250], [75, 247], [77, 244], [78, 242], [79, 239], [80, 237], [82, 234], [82, 232], [84, 229], [85, 225],
   #      [87, 222], [88, 219], [89, 216], [91, 212], [92, 208], [
   #          94, 204], [95, 201], [96, 196], [97, 194], [98, 191],
   #      [100, 185], [102, 178], [104, 173], [104, 171], [105, 164], [
   #          106, 158], [107, 156], [107, 152], [108, 145],
   #      [109, 141], [110, 139], [112, 133], [113, 131], [116, 127], [
   #          117, 125], [119, 122], [121, 121], [123, 120],
   #      [125, 122], [125, 125], [127, 130], [128, 133], [131, 143], [
   #          136, 153], [140, 163], [144, 172], [145, 175],
   #      [151, 189], [156, 201], [161, 213], [166, 225], [169, 233], [
   #          171, 236], [174, 243], [177, 247], [178, 249],
   #      [179, 251], [180, 253], [180, 255], [179, 257], [177, 257], [
   #          174, 255], [169, 250], [164, 247], [160, 245],
   #      [149, 238], [138, 230], [127, 221], [124, 220], [
   #          112, 212], [110, 210], [96, 201], [84, 195], [74, 190],
   #      [64, 182], [55, 175], [51, 172], [49, 170], [51, 169], [
   #          56, 169], [66, 169], [78, 168], [92, 166], [107, 164],
   #      [123, 161], [140, 162], [156, 162], [171, 160], [173, 160], [
   #          186, 160], [195, 160], [198, 161], [203, 163],
   #      [208, 163], [206, 164], [200, 167], [187, 172], [174, 179], [
   #          172, 181], [153, 192], [137, 201], [123, 211],
   #      [112, 220], [99, 229], [90, 237], [80, 244], [73, 250], [69, 254], [69, 252]]), 

   # ("pigtail",
   #        [[81, 219], [84, 218], [86, 220], [88, 220], [90, 220], [92, 219], [95, 220], [97, 219], [99, 220],
   #         [102, 218], [105, 217], [107, 216], [110, 216], [113, 214], [
   #             116, 212], [118, 210], [121, 208], [124, 205],
   #         [126, 202], [129, 199], [132, 196], [136, 191], [139, 187], [
   #             142, 182], [144, 179], [146, 174], [148, 170],
   #         [149, 168], [151, 162], [152, 160], [152, 157], [152, 155], [
   #             152, 151], [152, 149], [152, 146], [149, 142],
   #         [148, 139], [145, 137], [141, 135], [139, 135], [134, 136], [
   #             130, 140], [128, 142], [126, 145], [122, 150],
   #         [119, 158], [117, 163], [115, 170], [114, 175], [117, 184], [
   #             120, 190], [125, 199], [129, 203], [133, 208],
   #         [138, 213], [145, 215], [155, 218], [164, 219], [166, 219], [
   #             177, 219], [182, 218], [192, 216], [196, 213],
   #         [199, 212], [201, 211]])]


RESAMPLE_SIZE = 64
NumUnistrokes = 16;
NumPoints = 64;
SQUARE_SIZE = 250.0;
ORIGIN = (0,0);
Diagonal = sqrt(SQUARE_SIZE * SQUARE_SIZE + SQUARE_SIZE * SQUARE_SIZE);
HalfDiagonal = 0.5 * Diagonal;
ANGLE_RANGE = (2 / 180) * pi
ANGLE_PRECISION = (2 / 180) * pi
PHI = 0.5 * (-1.0 + (5.0)**0.5)

#The recognizer class implements the matching of the input gesture to available templates
#and outputs the corressponding figure name. 
class recognizer(object):

    def __init__(self):
        # format the example gestures
        self.unistrokes = []
        for template in UNISTROKES:
            self.unistrokes.append(recognizer(template[1]))
            self.unistrokes[-1].name = template[0]
     
    def __init__(self, points, should_format=True):
        self.points = points
        if should_format:
            self.resample()
            self.rotate_by(-self.indicative_angle())
            self.scale_to(SQUARE_SIZE)
            self.translate_to(ORIGIN)

    
    def resample(self,points):

        points = self.points
        #calculating the length that should be between given points. 
        I = self.path_length() / (RESAMPLE_SIZE - 1)
        D = 0
        new_points = [points[0]]
        i = 1
        while i < len(points):
            previous, current = points[i - 1:i + 1]
            d = self.distance(previous, current)
            if ((D + d) >= I):
                q = (previous[0] + ((I - D) / d) * (current[0] - previous[0]),
                     previous[1] + ((I - D) / d) * (current[1] - previous[1]))
                new_points.append(q)
                points.insert(i, q)
                D = 0
            else:
                D += d
            i += 1
        #This is to fix any round off error, incase it occurs. 
        if len(new_points) == RESAMPLE_SIZE - 1:
            new_points.append(new_points[-1])
        self.points = new_points

    def path_length(self):
        #This function works on calculating the path by summing distances between points. 
        d = 0
        for i in range(1, len(self.points)):
            d += self.distance(self.points[i - 1], self.points[i])
        return d

    def indicative_angle(self):
        #This returns the angle to rotate the figure at.
        c = self.centroid()
        return atan2(c[1] - self.points[0][1], c[0] - self.points[0][0])

    def centroid(self):
        n = len(self.points)
        return (
            sum([p[0] / n for p in self.points]),
            sum([p[1] / n for p in self.points])
        )

    def rotate_by(self, angle):
        #This function calculates the new points after a figure is rotated by certain angle. 
        c = self.centroid()
        new_points = []
        for p in self.points:
            dx, dy = p[0] - c[0], p[1] - c[1]
            new_points.append((
                dx * cos(angle) - dy * sin(angle) + c[0],
                dx * sin(angle) + dy * cos(angle) + c[1]
            ))
        self.points = new_points

    def scale_to(self, size):
        #scales the points in order to fit it into square with side length size.
        B = self.bounding_box()
        new_points = []
        for p in self.points:
            new_points.append((
                p[0] * size / B[0],
                p[1] * size / B[1]
            ))
        self.points = new_points

    def bounding_box(self):
        minX, maxX = inf, -inf
        minY, maxY = inf, -inf
        for point in self.points:
            minX, maxX = min(minX, point[0]), max(maxX, point[0])
            minY, maxY = min(minY, point[1]), max(maxY, point[1])
        return (maxX - minX, maxY - minY)

    def translate_to(self, target):
        #Translates the whole figure such that the centriod of the figure is at origin.
        c = self.centroid()
        new_points = []
        for p in self.points:
            new_points.append((
                p[0] + target[0] - c[0],
                p[1] + target[1] - c[1]
            ))
        self.points = new_points

    def distance_at_best_angle(self, T):
        #Finds the best distance between nodes using the angle of rotation. 
        a = -ANGLE_RANGE
        b = ANGLE_RANGE
        x1 = PHI * a + (1 - PHI) * b
        x2 = PHI * b + (1 - PHI) * a
        f1 = self.distance_at_angle(T, x1)
        f2 = self.distance_at_angle(T, x2)
        while abs(b - a) > ANGLE_PRECISION:
            if f1 < f2:
                b = x2
                x2 = x1
                f2 = f1
                x1 = PHI * a + (1 * PHI) * b
                f1 = self.distance_at_angle(T, x1)
            else:
                a = x1
                x1 = x2
                f1 = f2
                x2 = PHI * b + (1 - PHI) * a
                f2 = self.distance_at_angle(T, x2)
        return min(f1, f2)

    def distance_at_angle(self, T, angle):
        #This calulates the distances between points after having them rotated at a certain angle. 
        rotated_stroke = recognizer(self.points, False)
        rotated_stroke.rotate_by(angle)
        return rotated_stroke.path_distance(T)

    def distance(p1, p2):
        return ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5

    def path_distance(self, points):
        #Calculates the average distance betwen two corresponding paths. 
        n = len(points)
        return sum([self.distance(self.points[i], points[i]) / n for i in range(n)])

    def get_gesture(self, points):
        #Takes the input gesture from the user from canvas, and searches for appropriate template from the 
        #templates class and also implements the $1 Algorithm. 
        stroke = recognizer(points)
        points = self.resample(list(points))
        points = self.rotate_by(points)
        points = self.scale_to(points)
        points = self.translate_to(points)
        #Does the job of searching for the drawn gesture from the templates. 
        min_distance = inf
        gesture_name = ''
        for template_stroke in self.unistrokes:
            distance = stroke.distance_at_best_angle(template_stroke.points)
            if distance < min_distance:
                # update the current best gesture
                min_distance = distance
                gesture_name = template_stroke.name
        score = 1 - min_distance / (0.5 * sqrt(self.square_size **
                         2 + self.square_size ** 2))
        return gesture_name, score
 
##############################################################################################################


# Logic to read gesture data set, calls for offline Recognition test and output of the recognition results to log file.
main_folder = "xml_logs"
data = []
# iterate through all sub folders
for i in range(2, 12):
    if i<10:
        userFolder = f"s0{i}"
    else:
        userFolder = f"s{i}"
    
    path = os.path.join(main_folder, userFolder).replace("\\", "/")
    for file in os.listdir(path):
        if file.endswith(".xml"):
            filePath = os.path.join(path, file).replace("\\", "/")
            # This step parse the xml file to get the root element
            tree = etree.parse(filePath)
            root = tree.getroot()

            # Each Gesture element and its attributes along with itereated points will be saved in a dictionary per user           
            gesture_data = {
                "name": root.attrib.get("Name"),
                "subject": root.attrib.get("Subject"),
                "points": [],
            }
            for point in root:
                gesture_data["points"].append((point.attrib.get("X"), point.attrib.get("Y")))
            # add the gesture data to the list
            data.append(gesture_data)

# Creating an empty CSV file with coloumn names to store data. 
with open("recognition_output.csv", mode="w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["User", "Gesture Type", "Number of Training Examples", "Training Set Contents", "RecoResult GestureType",
            "RecoResult Score", "CorrectIncorrect[1/0]",])

users_index = set()
for d in data:
    users = d["subject"]
    if users and users not in users_index:
        users_index.add(int(users))

users_opted = {next(iter(users_index))}
#print(f'User => {user_opted}')
for user in users_opted:
    match = 0

    allTotalScores_OfUsers = []
    totalScore_OfUser = 0
    accuracyScoresOfUsers = []

    recognitionScore = 0
    recognitionScoresList = []

    #bestMatchScore = {}
    #sum_qty = 0
    
    print(f"User {user}")
    # Choose a random sample of templates from templates set list of unique gesture types
    gestureTypes = list(set(gesture["name"][:-2] for gesture in data))
    # logic to get a random sample of one gesture from each gesture type
    sample = [(gesture["name"][:-2], [[int(x), int(y)] for x, y in gesture["points"]])
        for gestureType in gestureTypes
        for gesture in random.sample([g for g in data if g["name"][:-2] == gestureType], 1)
    ]

    newgestureTypesList = list(set(gesture["name"][:-2] for gesture in data))
    # logic to get a new random sample of one gesture from each gesture type
    newSample = [(gesture["name"], [[int(x), int(y)] for x, y in gesture["points"]])
        for gestureType in newgestureTypesList
        for gesture in random.sample([g for g in data if g["name"][:-2] == gestureType], 1)
    ]

    gestureTemplateNames = [name[0] for name in newSample]
    gestureTemplateNames.sort()

    sample.sort(key=lambda name: name[0])
    sampleCopy = sample.copy()


    sample = map(lambda x: template(*x), sample)
    recognizer = recognizer()
    for template in sample:
        recognizer.addTemplate(template)
    for i in range(10):
        
        # list of unique gesture types
        gestureTypesList = list(set(gesture["name"][:-2] for gesture in data))

        # For each gesture type
        for gestureType in gestureTypesList:
            # Get all gestures list that match this gesture type
            gestures = [
                gesture for gesture in data if gesture["name"][:-2] == gestureType
            ]
            # print(gestures)
            if gestures:
                # Choose a random gesture
                randomGesture = random.choice(gestures)
                gesturePoints = randomGesture["points"]
                if gesturePoints:
                    points = [[int(coordinate) for coordinate in point] for point in gesturePoints]
                    # recognize call
                    matchedTemplate, score = recognizer.recognize(points)

                    if matchedTemplate.name == randomGesture["name"][:-2]:
                        recognitionScore += 1
                        totalScore_OfUser += 1
                        #bestMatchScore[random_gesture.get("name")] = score
                        match = 1
                    else:
                        totalScore_OfUser += 1
                        match = 0

                    with open("recognition_output.csv", mode="a", newline="") as f:
                        w = csv.writer(f)
                        w.writerow([user, randomGesture["name"], len(sampleCopy), gestureTemplateNames, matchedTemplate.name, round(score, 4), match,])

    recognitionScoresList.append(recognitionScore / 100)
    print(f"Reco score of the user {user}: {recognitionScore/100}")

    allTotalScores_OfUsers.append(totalScore_OfUser / 100)
    print(f"Total score for user {user}: {totalScore_OfUser/100}")
    
    # sorted_bestMatchScore = dict(sorted(bestMatchScore.items(), key=lambda x: x[1], reverse=True))
    # print(f"N Best Scores for User {user} : {sorted_bestMatchScore}")
    accuracyPerUser = (recognitionScore / 100) / (totalScore_OfUser / 100)
    accuracyScoresOfUsers.append(accuracyPerUser)

print(f"Total Average Accuracy: {round(sum(recognitionScoresList)/sum(allTotalScores_OfUsers),4)}")

with open("recognition_output.csv", mode="a", newline="") as f:
    w = csv.writer(f)
    w.writerow(["Total Average Accuracy", sum(accuracyScoresOfUsers) / len(accuracyScoresOfUsers)])

##############################################################################################################

#Main class from where the execution starts
#class myCanvas(tk.Tk):

#    def __init__(self, *args, **kwargs):
#        tk.Tk.__init__(self, *args, **kwargs)

#        #code in order to print the score and figure on canvas. 
#        self.title("$1 Recognizer")
#        self.detected_shape = tk.StringVar()
#        tk.Label(self, text="Matched Shape:").grid(
#            row=0, column=0, sticky="W", padx=5, pady=5)
#        tk.Label(self, text="Score:").grid(
#            row=1, column=0, sticky="W", padx=5, pady=5)
#        tk.Label(self, textvariable=self.detected_shape).grid(
#            row=0, column=1, sticky="W", padx=5, pady=5)
#        tk.Label(self, textvariable=self.detected_score).grid(
#            row=1, column=1, sticky="W", padx=5, pady=5)

#        # Canvas for drawing
#        self.canvas = tk.Canvas(self, width=600, height=600, bg="black")
#        self.canvas.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
#        self.canvas.bind("<B1-Motion>", self.on_motion)
#        self.canvas.bind("<ButtonRelease-1>", self.on_left_up)
#        self.canvas.bind("<Button-1>", self.on_left_down)
#        self.canvas.bind('<Double-Button-1>', self.on_left_double)
#        self.path_points = []

#    def on_left_down(self, event):
#        global gx, gy
#        gx, gy = event.x, event.y
#        color = 'red'
#        x1, y1 = (event.x - 3), (event.y - 3)
#        x2, y2 = (event.x + 3), (event.y + 3)
#        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

#    def on_motion(self, event):
#        global gx, gy
#        x, y = event.x, event.y
#        self.canvas.create_line(gx, gy, x, y, fill='red', width=5)
#        self.path_points.append((x, y))
#        gx, gy = event.x, event.y

#    #This gesture after drawing will make a call to the recognizer which will in turn identify the figure 
#    #and perform the scaling and rotation. 
#    def on_left_up(self, event):
#        matched_template, score = recognizer.recognize(self.path_points)
#        self.detected_shape.set(matched_template.name)
#        self.detected_score.set("{0:.2f}".format(score * 100))
#        self.path_points = []

#    def on_left_double(self, event):
#        self.canvas.delete("all")

#if __name__ == '__main__':
#    app = myCanvas()
#    app.mainloop()