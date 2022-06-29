"C:\Program Files\Blender Foundation\Blender 3.0\blender.exe" -b project_files/scene.blend --python "%cd%//build//Camera1.py" -o "%cd%//render_files//Camera1//frame_#" -E BLENDER_EEVEE -s 5 -e 5 -a  project_files/scene.blend --python "%cd%//build//Camera2.py" -o "%cd%//render_files//Camera2//frame_#" -E BLENDER_EEVEE -s 5 -e 5 -a  project_files/scene.blend --python "%cd%//build//Camera3.py" -o "%cd%//render_files//Camera3//frame_#" -E BLENDER_EEVEE -s 5 -e 5 -a  project_files/scene.blend --python "%cd%//build//Camera4.py" -o "%cd%//render_files//Camera4//frame_#" -E BLENDER_EEVEE -s 5 -e 5 -a
echo all done!

PAUSE

cd /d %cd%
for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)