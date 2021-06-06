# -*- coding: utf-8 -*-
from Vision import detection

import time
import datetime

if __name__ == "__main__":
	# What you'd like to detect from Coco dataset
	objects_to_detect = ['person']  # defualt None draw everything detected

	runtime=1

	# run for 30 seconds
	end_time = datetime.datetime.now() + datetime.timedelta(minutes=runtime)

	while (datetime.datetime.now() < end_time):	
		s = time.time()

		detection.Run(objects=objects_to_detect)

		f =time.time()
		#print(f"Frame runtime: {f - s}")
		#print()

