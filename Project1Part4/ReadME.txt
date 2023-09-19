--------------------- Project 1 Part 4 : Collecting data from people ------------------------

How to run:

    Run "Project1Part4.py" to open up a drawable canvas. 


-- Application usage and Implementation details:

	a). We have used Visual Studio as our IDE as we are coding in Python.

	b). In this part, the main focus is on collecting gesture samples data from 6 users, per user will be prompted to add 10 samples for each of the 16 gestures. 

	c). In the code, the next_drawing() at line# 134, function makes calls to writeXML method to create XML file and updates the canvas for next gesture, sample to be drawn after clicking on 'Next' button.

	d). The writeXML() function at line# 79 takes the datapoints, gesture name, the sample user number and the sample number as input and writes these data into the xml file by creating respective directories 	and filenames for each sample gesture and convert it to byte code and save the files.

	e.) We have added two buttons, 'Clear' to remove the gesture from canvas if user wish to change the gesture drawn for a respective sample gesture, 'Next, to create XML file one at a time and proceed to 	draw an other sample gesture.   

	f). We have collected samples for 6 users (s1-s6) folders which is collected in the 'xml_logs_dataset' folder. Each folder will have 160 XML files (16 gestures x 10 samples) of sample gesture data. So 	total 960 sample gesture dataset zip file. We also added the user consent forms in the 'xml_logs_dataset' folder. 


-- We have added a demo video (video_demo.mkv) of the explanation of the code and application running. 
	video_demo1.mkv consists of demo for 1 sample of all the 16 gestures.

Team Members:
Sai Mohan Sujay Kanchumarthi - 4602-1313 - Skanchumarthi@ufl.edu
Priti Gumaste - 4953-5219 - pgumaste@ufl.edu
