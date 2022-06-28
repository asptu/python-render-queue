@echo off
set loopcount=2
:loop

%LOCATION% -b %PATH% -o %cd%\render_files\camera1\frame_# -E BLENDER_EEVEE -s %SFRAME% -e %EFRAME% -a

set /a loopcount=loopcount-1
if %loopcount%==0 goto exitloop
goto loop
:exitloop
pause