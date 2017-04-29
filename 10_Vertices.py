#10_Vertices.py
import bpy

#set 3d cursor location
bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)

#create a cube
bpy.ops.mesh.primitive_cube_add()

#show number of objects
object_count = len(bpy.context.scene.objects)
print("Number of objects in your current scene is " + str(object_count))
print()

#show object vertices
if object_count > 0:
    for i in range(0, len(bpy.context.scene.objects[0].data.vertices)):
        print("bpy.context.scene.objects[0].data.vertices[" + str(i) + "].co = " + str(bpy.context.scene.objects[0].data.vertices[i].co))

#lets try to change two vertices
vert0 = (-2.0, -2.0, -2.0)
vert1 = (-2.0, -2.0, 2.0)
if object_count > 0:
    bpy.context.scene.objects[0].data.vertices[0].co = vert0
    bpy.context.scene.objects[0].data.vertices[1].co = vert1
    print()
    for i in range(0, len(bpy.context.scene.objects[0].data.vertices)):
        print("bpy.context.scene.objects[0].data.vertices[" + str(i) + "].co = " + str(bpy.context.scene.objects[0].data.vertices[i].co))

#deselect all vertices
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.object.mode_set(mode='OBJECT')

#select four vertices
verts = [4,5,6,7]
for v in verts:
    bpy.context.object.data.vertices[v].select = True
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.delete(type='VERT')

#add two vertices
bpy.ops.object.mode_set(mode='OBJECT')
bpy.context.object.data.vertices.add(2)
bpy.context.object.data.vertices[-1].co = (0.5, 0.5, -0.5)
bpy.context.object.data.vertices[-2].co = (0.5, -0.5, -0.5)
bpy.ops.object.mode_set(mode='EDIT')

#to be continued