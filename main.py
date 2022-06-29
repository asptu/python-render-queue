import subprocess

# Define Values
file = 'scene.blend'
cameras = ['Camera1', 'Camera2', 'Camera3', 'Camera4']
start_frame = '5'
end_frame = '5'
x_res = '400'
y_res = '400'
fps = '24'
format = "'PNG'"
step = '1'
render_engine = 'EEVEE'
samples = '1'
denoising = 'True'
time_limit = '5'
scene = 'Scene'


# Static Values
blender_loc = r'"C:\Program Files\Blender Foundation\Blender 3.0\blender.exe"'
path = 'project_files/' + file
scripts = []


# Script Compiler
if render_engine == 'CYCLES':
    for x in cameras:
        with open(f'build/{x}.py', 'w') as f:
            f.write(f'import bpy; bpy.context.scene.camera = bpy.data.objects["{x}"]; bpy.context.scene.render.resolution_x = {x_res}; bpy.context.scene.render.resolution_y = {y_res}; bpy.context.scene.render.fps = {fps}; bpy.context.scene.render.image_settings.file_format = {format}; bpy.context.scene.frame_step = {step}; bpy.context.scene.cycles.samples = {samples}; bpy.context.scene.cycles.use_denoising = {denoising}; bpy.context.scene.cycles.time_limit = {time_limit}; bpy.context.scene.name = "{scene}"')
elif render_engine == 'EEVEE':
    for x in cameras:
        with open(f'build/{x}.py', 'w') as f:
            f.write(f'import bpy; bpy.context.scene.camera = bpy.data.objects["{x}"]; bpy.context.scene.render.resolution_x = {x_res}; bpy.context.scene.render.resolution_y = {y_res}; bpy.context.scene.render.fps = {fps}; bpy.context.scene.render.image_settings.file_format = {format}; bpy.context.scene.frame_step = {step}; bpy.context.scene.eevee.taa_render_samples = {samples}; bpy.context.scene.name = "{scene}"')


if render_engine == 'CYCLES':
    for x in cameras:
        scripts.append(f'{path} --python "%cd%//build//{x}.py" -o "%cd%//render_files//{x}//frame_#" -E CYCLES -s {start_frame} -e {end_frame} -a')
elif render_engine == 'EEVEE':
    for x in cameras:
        scripts.append(f'{path} --python "%cd%//build//{x}.py" -o "%cd%//render_files//{x}//frame_#" -E BLENDER_EEVEE -s {start_frame} -e {end_frame} -a')


with open('build/rendering.bat', 'w') as f:
    f.write(f'{blender_loc} -b ')
    f.write('  '.join(scripts))
    f.write('\n' + 'echo all done!')

subprocess.call([r'build\rendering.bat'])


