import os

# Variable Values
scene = 'scene.blend'
cameras = ['Camera1', 'Camera2']
start_frame = '5'
end_frame = '6'


# Static Values
blenderLoc = r'"C:\Program Files\Blender Foundation\Blender 3.0\blender.exe"'
path = 'project_files/' + scene
camerasNum = len(cameras)




for i in cameras:
    print(cameras)


    
#os.putenv("CAMERAS", cameras)
#os.putenv("NUM", camerasNum)
# os.putenv("LOCATION", blenderLoc)
# os.putenv("PATH", path)
# os.putenv("SFRAME", start_frame)
# os.putenv("EFRAME", end_frame)
# os.system("test2.bat")







""" path = 'project_files/' + scene
os.putenv("PATH", path)

os.system("data\cameras.bat")


fileName = 'data/cameras.txt'

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        print(words)



for x in cameras:
    print(x)

import bpy
bpy.context.scene.camera = bpy.data.objects["Camera1"]
"""