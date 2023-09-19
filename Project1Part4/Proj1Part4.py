'''
                                            HCIRA - Project 1 Part 4
                                                    Group 23
                                                      Names: 
                                        Sai Mohan Sujay Kanchumarthi 
                                                 Priti Gumaste 
'''


import os
import time
from tkinter import *
from xml.dom import minidom
import xml.etree.ElementTree as ET
from datetime import datetime

# Importing tkinter module
# Class definition for the main window application
# class MyApp():

#     # Constructor of the class
#     def _init_(self, root):
#         self.root = root
        # Initializing the tkinter Tk class
        #Tk._init_(self, *args, **kwargs)

########## Canvas for drawing
root = Tk()
root.title("$1 Recognizer")

current_gestureCount = 1
current_sampleCount = 1
totalGestures = 16
totalSampleSize = 10
current_user = ""

########### All the gesture names that the user will be drawing on canvas ##########
gesture_names = {
    1: "triangle",
    2: "x",
    3: "rectangle",
    4: "circle",
    5: "check",
    6: "caret",
    7: "zig-zag",
    8: "arrow",
    9: "left_sq_bracket",
    10: "right_sq_bracket",
    11: "v",
    12: "delete",
    13: "left_curly_brace",
    14: "right_curly_brace",
    15: "star",
    16: "pigtail"
}

# gestures_names = ['triangle', 'x', 'rectangle', 'circle', 'check', 'caret', 'zig-zag', 'arrow', 'left-square bracket', 'right-square bracket', 'v', 
#     'delete', 'left curly brace', 'right curly brace', 'star', 'pigtail']

# gesture_elem_attributes = ['Name', 'Subject', 'Speed', 'Number', 'NumPts', 'Millseconds', 'AppName', 'AppVer', 'Date', 'TimeOfDay']

# gesture_elem_attributes_values = ['triangle01', '1', 'medium', '1', '74', '1268', 'Gestures', '3.5.0.0', 'Thursday, March 02, 2023', '9:12:24 AM']

########### Logic enter to enter user name in Entry widget to assign name of the user folder ##########
user_name = StringVar()
def userNameSubmit():
    global current_user

    name = user_name.get()
    current_user = name
    # sbt_btn["state"] = "disabled"
    # sbt_btn.config(text = "Submitted")
    user_name.set("")


Label(root, text="User Name:").grid(row=0, column=0, sticky="W", padx=5, pady=5)
user_var = Entry(root, textvariable=user_name).grid(row=0, column=1, sticky="W", padx=5, pady=5)
sbt_btn = Button(root, text="submit", state="normal", command = userNameSubmit).grid(row=0, column=2)
#current_user = user_name.get()
#print(current_user)

########### This part sets the updates gesture name and the sample count name to the canvas ##########
Label(root, text="Gesture Type:").grid(row=1, column=0, sticky="W", padx=5, pady=5)
Label(root, text="Sample #:").grid(row=2, column=0, sticky="W", padx=5, pady=5)

gestureType_label = Label(root, text=f"{gesture_names[current_gestureCount]}")
gestureType_label.grid(row=1, column=1, sticky="W", padx=5, pady=5)

sampleCount_label = Label(root, text=f"{current_sampleCount}")
sampleCount_label.grid(row=2, column=1, sticky="W", padx=5, pady=5)

########### Takes the current system time inorder to print on the XML ##########
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

########### This method is used to create XML log data files with points captured as subelements and gesture detials 
###########as main element attributes
def writeXML(points, gesture, user, sampleCount):

    ########### logic to create main directory and individual folders for each user ##########
    cwd = os.getcwd()
    main_dir = '{}/xml_logs_dataset/'.format(cwd)
    #print(main_dir)
    user_dir = f'{user}'
    #print(user_dir)
    fileName = '{}{}.xml'.format(gesture, sampleCount)
    #print(fileName)
    try:
        os.mkdir(main_dir)
    except:
        pass

    # os.chdir(dir+fileName)
    path = os.path.join(main_dir, user_dir).replace("\\", "/")
    #print(path)
    try:
        os.mkdir(path)
    except:
        pass
    
    file_path = os.path.join(path, fileName).replace("\\", "/")
    #print(file_path)

    ########### logic to create and write an XML file with required elements and their attributes ##########
    ########### Gesture element ##########
    gesture_element = ET.Element("Gesture")
    gesture_element.set('Name', '{}{}'.format(gesture, sampleCount))
    gesture_element.set('Subject', '{}'.format(user))
    gesture_element.set('Number', '{}'.format(sampleCount))
    gesture_element.set('NumPts', '{}'.format(len(points)))
    ########### Point elements ##########
    for point in points:
        point_element = ET.SubElement(gesture_element, 'Point')
        point_element.set('X', str(point[0]))
        point_element.set('Y', str(point[1]))
        point_element.set('T', str(point[2]))
    ###########Encode to byte data ##########
    byte_xml = ET.tostring(gesture_element)
    xmlstr = minidom.parseString(byte_xml).toprettyxml(indent="   ")
    ########### Create XML file with sample gesture name file name in respective user directory created ##########
    with open(file_path, "wb") as f:
        f.write(xmlstr.encode('utf-8'))
    ########### clear canvas call to add new gesture ##########
    clear_canvas()
    
     # with open(dir+fileName, 'wb') as f:
    #     f.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n')
    #     f.write('<Gesture Name="{}{}" Subject="{}" Number="{}" NumPts="{}">\n'.format(gesture, sampleCount, user, sampleCount, len(points)))

    #     for point in points:
    #         f.write('   <Point X="{}" Y="{}" T="{}" />\n'.format(point[0], point[1], point[2]))

    #     f.write('</Gesture>')

########### Method to make write XML call and update gesture label, sample count based on gesture input by the user ##########
def next_drawing():
    global current_gestureCount
    global current_sampleCount
    global gestureType_label
    global sampleCount_label

    ########### does the work of writing data to XML files. ##########
    currentDrawing = gesture_names[current_gestureCount]
    writeXML(path_points, currentDrawing, current_user, current_sampleCount)

    ########### this if loop keeps track if 10 samples are taken per gesture ##########
    #print(current_sampleCount)
    if  current_sampleCount <11: 
        current_sampleCount += 1
        #print(current_sampleCount)
        sampleCount_label.config(text = current_sampleCount)

    ########### this updates the gesture to the next one, once 10 samples are taken for the current gesture ##########
    if current_sampleCount == totalSampleSize+1:
        sampleCount_label.config(text = current_sampleCount)
        current_sampleCount = 1
        sampleCount_label.config(text = current_sampleCount)
        current_gestureCount += 1
        #print(current_gestureCount)
        gestureType_label.config(text = gesture_names[current_gestureCount])
    ########### if all sample examples for each gesture type were drawn, disable buttons ##########
    if current_gestureCount == totalGestures + 1:
        sampleCount_label.config(text = "Done!")
        gestureType_label.config(text = "Done!")

        next_button["state"] = "disabled"
        clear_button["state"] = "disabled"

########### Create Canvas ##########
canvas = Canvas(root, width=800, height=600, bg="black")
canvas.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
#canvas.pack(anchor="nw", fill="both", expand=1)

path_points = []

########### clear canvas method ##########
def clear_canvas():
    canvas.delete("all")

# def next_gesture():
#     gesture_element = ET.Element("Gesture")
#     gesture_element.set('Name', 'triangle01')
#     #gesture_element.set('Subject', '1')
#     #gesture_element.set('Number', '1')

#     for point in path_points:
#         point_element = ET.SubElement(gesture_element, 'Point')
#         point_element.set('X', str(point[0]))
#         point_element.set('Y', str(point[1]))
#         #point_element.set('T', '11435895')
    
#     byte_xml = ET.tostring(gesture_element)
#     xmlstr = minidom.parseString(byte_xml).toprettyxml(indent="   ")

#     with open("triangle01.xml", "wb") as f:
#         f.write(xmlstr.encode('utf-8'))

#     canvas.delete("all")
    # for attrib in gesture_elem_attributes:
    #     gesture_element.set(attrib, )


########### buttons to handle the clear screen and next gesture calls. ##########
clear_button = Button(root, text="Clear", command=clear_canvas, state="normal", width = 10 , height=2, bd='10', bg='blue', fg='black')
clear_button.grid(row=4, column=0, padx=5, pady=5)

next_button = Button(root, text="Next", command=next_drawing, state="normal", width = 10 , height=2, bd='10', bg='green', fg='black')
next_button.grid(row=4, column=1, padx=5, pady=5)
   
#clear_button.place(x=300, y=500)
#clear_button.place()

#this binds the mouse operation 'clicking the button' to the function of clearing the canvas.
#self.canvas.bind('<Button-1>', self.clear_canvas)
#clear_button.configure(command=lambda: self.clear_canvas(None))
#self.canvas.bind(clear_button, self.clear_canvas)


#self.canvas.bind("<ButtonRelease-1>", self.on_left_up)        
#self.canvas.bind('<Double-Button-1>', self.clear_canvas)

########### Method to handle left mouse button down event ##########
def on_left_down(event):
    global gx, gy
    gx, gy = event.x, event.y
    x1, y1 = (event.x - 3), (event.y - 3)
    x2, y2 = (event.x + 3), (event.y + 3)
    canvas.create_rectangle(x1, y1, x2, y2, fill='red', outline='red')
    current_time = int(round(time.time() * 1000))
    path_points.append([event.x, event.y, current_time])

########### Method to handle mouse motion event ##########
def on_motion(event):
    global gx, gy
    x, y = event.x, event.y
    canvas.create_line(gx, gy, x, y, fill='red', width=3)
    current_time = int(round(time.time() * 1000))
    path_points.append([x, y, current_time])
    gx, gy = event.x, event.y
########## Mouse events method binding ##########
canvas.bind("<Button-1>", on_left_down)
canvas.bind("<B1-Motion>", on_motion)

# Method recognizes the shape drawn on the canvas by calling the recognizer.
    # recognize function and sets the result as the detected shape and score to be displayed on the UI.
    # def on_left_up(self, event):
    #     templates = ["triangle", "x", "rectangle", "circle", "check", "caret", "zig_zag","arrow",
    #          "left_square_bracket", "right_square_bracket","v", "delete",
    #          "left_curly_brace", "right_curly_brace", "star", "pigtail"]
    #     for template in templates:
    #         self.template.set(template)
    #         Label(self, textvariable=self.template).grid(
    #         row=0, column=1, sticky="W", padx=5, pady=5)
    #         self.next_gesture(self, template)
    #     #self.path_points = []

    # method simply clears the canvas by deleting all elements.

    #self.next_gesture

    # def next_gesture(self, event, template):
    #     for i in range(11):
    #         self.sampleNum.set(i)
    #         Label(self, textvariable=self.sampleNum).grid(
    #         row=1, column=1, sticky="W", padx=5, pady=5)
    #             #self.sampleNum.set(i)
    #         self.path_points = []

    # def next_canvas():
    #     a=0

# The code runs the Tkinter application by instantiating an object of the MyApp class and starting the event loop
# with the mainloop method.
#if __name__ == '_main_':
    # root = tk.Tk()
    #app = MyApp(root)

root.mainloop()

