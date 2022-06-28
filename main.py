import os

# Define Values
scene = 'scene.blend'
cameras = ['Camera1', 'Camera2']
start_frame = '27'
end_frame = '32'


for x in cameras:
    print(r'"C:\Program Files\Blender Foundation\Blender 3.2\blender" -b %PATH% --python camera1.py -o %cd%\render_files\camera1\frame_# -E BLENDER_EEVEE -s %SFRAME% -e %EFRAME% -a')

    



# path = 'project_files/' + scene
# os.putenv("PATH", path)
# os.putenv("SFRAME", start_frame)
# os.putenv("EFRAME", end_frame)
# os.system("render.bat")







""" path = 'project_files/' + scene
os.putenv("PATH", path)

os.system("data\cameras.bat")


fileName = 'data/cameras.txt'

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        print(words) """


"""
import bpy
bpy.context.scene.camera = bpy.data.objects["Camera1"]
"""