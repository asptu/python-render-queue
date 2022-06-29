import subprocess


# Define Values
scene = 'scene.blend'
cameras = ['Camera1', 'Camera2', 'Camera3', 'Camera4']
start_frame = '5'
end_frame = '7'


# Static Values
blenderLoc = r'"C:\Program Files\Blender Foundation\Blender 3.2\blender.exe"'
path = 'project_files/' + scene
scripts = []


# Script Compiler
for x in cameras:
    with open(f'build/{x}.py', 'w') as f:
        f.write(f'import bpy; bpy.context.scene.camera = bpy.data.objects["{x}"]')


for x in cameras:
    scripts.append(f'{path} --python %cd%//build//{x}.py -o %cd%//render_files//{x}//frame_# -E BLENDER_EEVEE -s {start_frame} -e {end_frame} -a')

with open('build/rendering.bat', 'w') as f:
    f.write(f'{blenderLoc} -b ')
    f.write('  '.join(scripts))

subprocess.call([r'C:\Users\a\Documents\Blener_RenderQ_Python\build\rendering.bat'])


