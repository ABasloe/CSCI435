# CSCI435

Libraries used:
- Python's xml ElementTree and Tree modules
- the Python PIL imaging library

Compile and Run:
- First make sure to change the "base_path" variable to wherever you donwload the files onto your computer, the rest should be fine unchanged.
- The pictures are hardcoded into the program so there is no need for user interaction simply compile the program using any python combatible IDE or from your terminal and run. The outputted pictures will then be put in the folder you have the original program.

Synopsis:
The program works by looping through a list of tuples and then looking at each tuple, taking the first part (the png) and the second part (the xml file). The program parses through the xml file, finds the leaf nodes or the GUI items and then for each leaf found, parses the exact boundary coordinates and creates a yellow boxes around the found bounds onto the png file. After each image is done it is printed out to the computer and the next one begins. 

I chose to use tuples as they are the most useful for seperating small groups of pairs of things so I could put all the images and files together while deliniating them easily. I chose to leave out the base_path so that others could change it easily when running the program and so I could use it for both the xml and png path. The rest is mostly just implementing the libraries i selected, especially the ElementTree xml which makes things fairly straight forward like finding all the leaf nodes using the length of the nodes. 
