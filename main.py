import subprocess
import shutil

# Define Values
file = 'scene.blend'
cameras = ['Camera1','Camera2']
start_frame = '1'
end_frame = '60'
x_res = '1280'
y_res = '720'
fps = '24'
format = "'PNG'"
step = '1'
render_engine = 'EEVEE'
samples = '1'
denoising = 'True'
time_limit = '0'
encoding_format = 'PRORES_4444'



# Static Values
blender_loc = r'"C:\Program Files\Blender Foundation\Blender 3.0\blender.exe"'
path = 'project_files/' + file
scripts = []
ffmpeg_scripts = []


# Script Compiler
if render_engine == 'CYCLES':
    for x in cameras:
        with open(f'build/{x}.py', 'w') as f:
            f.write(f'import bpy; bpy.context.scene.camera = bpy.data.objects["{x}"]; bpy.context.scene.render.resolution_x = {x_res}; bpy.context.scene.render.resolution_y = {y_res}; bpy.context.scene.render.fps = {fps}; bpy.context.scene.render.image_settings.file_format = {format}; bpy.context.scene.frame_step = {step}; bpy.context.scene.cycles.samples = {samples}; bpy.context.scene.cycles.use_denoising = {denoising}; bpy.context.scene.cycles.time_limit = {time_limit}')
elif render_engine == 'EEVEE':
    for x in cameras:
        with open(f'build/{x}.py', 'w') as f:
            f.write(f'import bpy; bpy.context.scene.camera = bpy.data.objects["{x}"]; bpy.context.scene.render.resolution_x = {x_res}; bpy.context.scene.render.resolution_y = {y_res}; bpy.context.scene.render.fps = {fps}; bpy.context.scene.render.image_settings.file_format = {format}; bpy.context.scene.frame_step = {step}; bpy.context.scene.eevee.taa_render_samples = {samples}')


if render_engine == 'CYCLES':
    for x in cameras:
        scripts.append(f'{path} --python "%cd%//build//{x}.py" -o "%cd%//render_files//{x}//frame_#" -E CYCLES -s {start_frame} -e {end_frame} -a')
elif render_engine == 'EEVEE':
    for x in cameras:
        scripts.append(f'{path} --python "%cd%//build//{x}.py" -o "%cd%//render_files//{x}//frame_#" -E BLENDER_EEVEE -s {start_frame} -e {end_frame} -a')



if encoding_format == 'PRORES_4444':
    for x in cameras:
        ffmpeg_scripts.append(f'ffmpeg -f image2 -r {fps} -i "%cd%\\render_files\\{x}\\frame_%%d.png" -c:v prores_ks -profile:v 4 -vendor apl0 -bits_per_mb 8000 -pix_fmt yuva444p10le "%cd%\\render_files\\{x}\\{x}_PRORES_4444.mov"')
        encoding = True
elif encoding_format == 'MP4':
    print('soon tm')
    encoding = True
else:
    encoding = False


with open('build/rendering.bat', 'w') as f:
    f.write(f'{blender_loc} -b ')
    f.write('  '.join(scripts))
    if encoding == True:
        f.write('\n' + '''
set str=%cd%
set str=%str:~0,-5%''' + '\n')
        f.write('\n'.join(ffmpeg_scripts))
        f.write('\n' + '''
echo all done!
PAUSE
SETLOCAL
SET "keepfile=ffmpeg.exe"

FOR %%a IN ("%cd%//build//*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"

GOTO :EOF''')

subprocess.call([r'build\rendering.bat'])


