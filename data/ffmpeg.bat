set str=%cd%
set str=%str:~0,-4%

ffmpeg -f image2 -r 24 -i "%str%render_files\Camera1\frame_%%d.png" -c:v prores_ks -profile:v 4 -vendor apl0 -bits_per_mb 8000 -pix_fmt yuva444p10le proRes444_output.mov

PAUSE