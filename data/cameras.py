import bpy

cameras = []

for obj in bpy.data.objects:
        if obj.type == 'CAMERA':
            cameras.append(obj.name)

print(cameras)
with open('data/cameras.txt', 'w') as f:
    f.write('\n'.join(cameras))


