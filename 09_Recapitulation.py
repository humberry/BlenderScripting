#09_Recapitulation.py
import bpy

#set 3d cursor location
bpy.context.scene.cursor_location = (1.0, 0.5, -1.0)

#create a cube
bpy.ops.mesh.primitive_cube_add()

#create a lamp
bpy.ops.object.lamp_add(type='SUN')

#create a camera
bpy.ops.object.camera_add()

#show number of objects
object_count = len(bpy.context.scene.objects)
print("Number of objects in your current scene is " + str(object_count))
print()

#show object type, name, location and dimensions
for i in range(0, object_count):
    print("bpy.context.scene.objects[" + str(i) + "].type = " + str(bpy.context.scene.objects[i].type))
    print("bpy.context.scene.objects[" + str(i) + "].name = " + str(bpy.context.scene.objects[i].name))
    print("bpy.context.scene.objects[" + str(i) + "].location = " + str(bpy.context.scene.objects[i].location))
    print("bpy.context.scene.objects[" + str(i) + "].dimensions = " + str(bpy.context.scene.objects[i].dimensions))
    print()

#select all and delete it
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()