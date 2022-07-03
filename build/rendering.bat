"C:\Program Files\Blender Foundation\Blender 3.0\blender.exe" -b project_files/scene.blend --python "%cd%//build//Camera1.py" -o "%cd%//render_files//Camera1//frame_#" -E BLENDER_EEVEE -s 1 -e 60 -a  project_files/scene.blend --python "%cd%//build//Camera2.py" -o "%cd%//render_files//Camera2//frame_#" -E BLENDER_EEVEE -s 1 -e 60 -a

set str=%cd%
set str=%str:~0,-5%
ffmpeg -f image2 -r 24 -i "%cd%\render_files\Camera1\frame_%%d.png" -c:v prores_ks -profile:v 4 -vendor apl0 -bits_per_mb 8000 -pix_fmt yuva444p10le "%cd%\render_files\Camera1\Camera1_PRORES_4444.mov"
ffmpeg -f image2 -r 24 -i "%cd%\render_files\Camera2\frame_%%d.png" -c:v prores_ks -profile:v 4 -vendor apl0 -bits_per_mb 8000 -pix_fmt yuva444p10le "%cd%\render_files\Camera2\Camera2_PRORES_4444.mov"

echo all done!
PAUSE
SETLOCAL
SET "keepfile=ffmpeg.exe"

FOR %%a IN ("%cd%//build//*") DO IF /i NOT "%%~nxa"=="%keepfile%" DEL "%%a"

GOTO :EOF