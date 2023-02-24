import bpy
import mathutils
import math

# define the orbit parameters
radius = 30000
speed = 0.03

# set the number of frames to orbit the object
num_frames = 100

# load scene 
scene = bpy.data.scenes["Scene"]

# load object
obj = bpy.context.scene.objects["NAC_DTM_A17SIVB."]

# add a new camera
cam = bpy.data.cameras.new(name='Camera-Orbit')
cam_ob = bpy.data.objects.new(name='Camera-Orbit', object_data=cam)
bpy.context.scene.collection.objects.link(cam_ob)
bpy.context.scene.camera = cam_ob

cam.lens= 1400 # focal length
cam.clip_end= 50000 # distance camera can see

# animate the camera along the curved path
camera_position = obj.location + mathutils.Vector((0, 0, radius))

# iterate over each frame and update the camera position
for i in range(num_frames):
    
    # calculate the current z-axis position of the camera
    z = obj.location[2] + radius * math.sin(speed * i)

    # calculate the new camera position
    camera_position = mathutils.Vector((obj.location[0], obj.location[1] + radius * math.cos(speed * i), z))
    
    # calculate the camera's direction vector
    direction = mathutils.Vector((0, 0, 0)) - camera_position
    
    # set the camera's location and rotation
    bpy.context.scene.camera.location = camera_position
    bpy.context.scene.camera.rotation_euler = direction.to_track_quat('-Z', 'Y').to_euler()
     
    # insert a keyframe for the camera's location and rotation
    bpy.context.scene.camera.keyframe_insert(data_path='location', frame=i)
    bpy.context.scene.camera.keyframe_insert(data_path='rotation_euler', frame=i)
