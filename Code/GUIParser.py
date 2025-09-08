import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

#list of tuples, each tuple is a pair of png and xml
#hardcode in files, put them in pairs, for each pair, read the xml leaf nodes, write yellow boxes
#onto the png, print out png

base_path = "C:/Users/apb71/OneDrive/Desktop/Code/CSCI 435/Assignment 0/Programming-Assignment-Data/"
#starting path for where all my images are on my computer

file_pairs = [('com.apalon.ringtones.png', 'com.apalon.ringtones.xml'), ('com.dropbox.android.png', 'com.dropbox.android.xml'), 
              ('com.giphy.messenger-1.png', 'com.giphy.messenger-1.xml'),
              ('com.giphy.messenger-2.png', 'com.giphy.messenger-2.xml'), ('com.google.android.apps.transalte.png', 'com.google.android.apps.transalte.xml'), 
              ('com.pandora.android.png', 'com.pandora.android.xml'),
              ('com.yelp.android.png', 'com.yelp.android.xml')]
'''
hardcoded list of tuples with each picture and its reflecting xml file. If needed the program could just be shifted so the user entered 
the name of the file and then the related xml file and each time it would be placed into the tuple list.
'''

def parse_bounds(bounds_str):
    x1, y1, x2, y2 = map(int, bounds_str.replace("][", ",").replace("[", "").replace("]", "").split(","))
    return (x1, y1, x2, y2)
#to parse the bounds from the xml file we have to remove the brackets and the quotes around them so that we can then set them to custom variables

for png, xml in file_pairs: #for every image and xml file in a tuple, do:
    print("FILE:") 
    xml_path = base_path + xml #add the exact xml file to the computer path to create the full location
    tree = ET.parse(xml_path) #use the python xlm package to parse the xml file into a usable tree
    root = tree.getroot() #locate the root of the tree
    png_path = base_path + png #do the same thing for the png with making the full locatable path
    image = Image.open(png_path).convert("RGB") #use the PIL package to create an image that can be written on
    draw = ImageDraw.Draw(image) #open the created image to write on
    
    
    for node in root.iter("node"):
        if len(node) == 0 and "bounds" in node.attrib: #len(node) == 0 finds all leaves as they have 0 children and 
                                                        #confirms that it is also an object with bounds
            bounds = parse_bounds(node.attrib["bounds"])
            x1, y1, x2, y2 = bounds #make 4 variables from the pounds we got above
            
            draw.rectangle([x1, y1, x2, y2], outline="yellow", width=5) #take the variables of the bounds and create a 5 pixel wide yellow box around them
                
            out_file = png.replace(".png", "_annotated.png") #create new files with an annotated version of the name
            image.save(out_file) #save the new created image

