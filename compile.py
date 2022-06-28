import os

with open('explode.bat', 'w') as f:
    f.write('echo hi')

os.system("explode.bat")
