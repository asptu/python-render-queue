:: Render

"C:\Program Files\Blender Foundation\Blender 3.2\blender" -b %PATH% --python camera1.py -o %cd%\render_files\camera1\frame_# -E BLENDER_EEVEE -s %SFRAME% -e %EFRAME% -a

echo all done!

PAUSE