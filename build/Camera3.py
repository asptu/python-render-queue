import bpy; bpy.context.scene.camera = bpy.data.objects["Camera3"]; bpy.context.scene.render.resolution_x = 400; bpy.context.scene.render.resolution_y = 400; bpy.context.scene.render.fps = 24; bpy.context.scene.render.image_settings.file_format = 'PNG'; bpy.context.scene.frame_step = 1; bpy.context.scene.eevee.taa_render_samples = 1