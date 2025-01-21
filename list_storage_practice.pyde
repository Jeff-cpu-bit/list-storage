#Jeffrey Hahner
#PVU249
#11362452
#CMPT 140 (1)
stripes = [] #empty list

def setup():#canvas start
    size(400, 400)  
    noStroke()

def draw():
    background(255)  # Clear the canvas with a white background
    stripe_height = 20  # Height of each stripe
    for y, color_value in stripes:#checks list for new additions and draws based off what is listed
        fill(color_value)
        rect(0, y, width, stripe_height)

def keyPressed():
    global stripes
    stripe_height = 20  #height of each stripe
    if key == BACKSPACE:
        if stripes:
             stripes.pop(-1) #removes newest stripe unless list if the list is not empty to avoid errors
        return  
    if key == 'r':
        new_color = color(255, 0, 0)  #red
    elif key == 'g':
        new_color = color(0, 255, 0)  #green
    elif key == 'b':
        new_color = color(0, 0, 255)  #blue
    else:
        return  
    
    new_y = len(stripes) * stripe_height  #chabhes the y value for where to draw strip depending on stripes in list
    stripes.append((new_y, new_color))  #add the y coordinate and color
