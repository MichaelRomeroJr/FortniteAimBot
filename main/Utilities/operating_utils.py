from PIL import ImageGrab
import numpy as np

import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle

def monitor_to_image():
	"""
		Read monitor as Pillow Image then convert to Numpy Array
		bbox specifies specific region (bbox= x,y,width,height)
	"""
	
	#img = ImageGrab.grab(bbox=(175,133,1750,950)) #Sample a smaller area of the monitor as Pil.Image
	img = ImageGrab.grab(bbox=(0,0,1920,1080)) #Grab entire monitor as Pil.image
	img_np = np.array(img) 
	
	return img_np


def get_boundingbox_coords(tensor):
	"""
		Input: tensor
		Output: Coordinates of object detected in tensor
	"""

	c1 = tuple(tensor[1:3].int()) #Top Left Coordinates
	c2 = tuple(tensor[3:5].int()) #Bottom Right Coordinates

	#+175 to x-coord & +135 to y-coord when taking sample of image
	x1 = int(c1[0].item()) #+175
	y1 = int(c1[1].item()) #+133
	x2 = int(c2[0].item()) #+175
	y2 = int(c2[1].item()) #+133
	 
	width = x2 -  x1
	height = y2 - y1 

	return width, height, x1, y1


class ImageLabel(tk.Label): 
	"""
		Class w/ tKinter to draw bounding boxes w/ GUI
	"""
   
	def load(self, im, width, height):        
		if isinstance(im, str):
			im = Image.open(im)
			im = im.resize((width,height)) #Resize target box to size of rectangle
		frames = []
		try:
			for i in count(1):
				frames.append(ImageTk.PhotoImage(im.copy()))
				im.seek(i)
		except EOFError:
			pass
		self.frames = cycle(frames)
		try:
			self.delay = im.info['duration']
		except:
			self.delay = 1 #self.delay = 100
		if len(frames) == 1:
			self.config(image=next(self.frames))
		else:
			self.next_frame()
	def unload(self):
		self.config(image=None)
		self.frames = None
	def next_frame(self):
		if self.frames:
			self.config(image=next(self.frames))
			self.after(self.delay, self.next_frame)


def create_overlay(width, height, x, y, object_detected):
	"""
		Use ImageLabel class to display rectangle over-lay on monitory 
	"""

	root = tk.Tk()
	lbl = ImageLabel(root, text=object_detected, compound='bottom', font=("Arial", 25))    
	lbl.pack()
	
	imgpath = Image.new('RGB', (width, height), color = 'red') #Create Red Rectangle to overlay over target

	lbl.load(imgpath, width, height)
	
	lbl.master.overrideredirect(True)
	GeometryString = "+" + str(x) + "+" + str(y)
	lbl.master.geometry(GeometryString) #label.master.geometry("+250+250")

	lbl.master.lift()
	lbl.master.wm_attributes("-topmost", True)
	lbl.master.wm_attributes("-disabled", True)
	lbl.master.wm_attributes("-transparentcolor", "white")

	lbl.pack()
	
	root.after(25, root.destroy)  
	#root.after(1000, root.destroy)
	
	lbl.mainloop()
	
	return


def draw_boundingbox(tensor, object_detected):
	"""
		Draw bounding box 
	"""

	width, height, x, y = get_boundingbox_coords(tensor=tensor) #Get Coordinates for rectangle to draw on screen
	create_overlay(width, height, x, y, object_detected=object_detected) #Draw rectangle on screen with the ability to click through it

	return x, y, width, height
