#!/usr/bin/env python

import os
import time
import profile_gen
import re



def sort_human(l):
  convert = lambda text: float(text) if text.isdigit() else text
  alphanum = lambda key: [ convert(c) for c in re.split('([-+]?[0-9]*\.?[0-9]*)', key) ]
  l.sort( key=alphanum )
  return l



if __name__ == '__main__':
	temp_arr = profile_gen.default_fanprofile()
	temp = os.popen('ls -d /sys/class/drm/card*/device/hwmon/hwmon*/').read()
	temp = temp.split('\n')
	debugfile = []
	for i in range(0,len(temp)):
		if len(temp[i]) > 2:
			debugfile.append(temp[i])

	debugfile = sort_human(debugfile)

	temp_handles = []
	for i in range(0, len(debugfile)):
		temp_handles.append(open(debugfile[i]+'/temp1_input', 'r'))


	temp = [40]*len(debugfile)
	calculated_fan = [0]*len(debugfile)
	while (1):
		for i in range(0, len(debugfile)):
			temp[i] = int(temp_handles[i].read())/1000
			temp_handles[i].seek(0)
			calculated_fan[i] = temp_arr[temp[i]]
			os.system('wolfamdctrl -i '+str(i)+' --set-fanspeed '+str(calculated_fan[i]))
#		print temp
#		print calculated_fan
		time.sleep(5)


	##### Clean up
	for i in range(0, len(debugfile)):
                temp_handles[i].close()
