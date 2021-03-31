import bpy
import bmesh
import mathutils

obj1 = bpy.data.objects["Plane"]
frame_range1 = [1,100]
scale1 = 2.00
name1 = "Cloth"
output_dir1 = "X:\USER\out"

def bake_morph_textures(obj, frame_range, scale, name, output_dir):

    scene_path = bpy.path.abspath("//")
    
    if "//" in output_dir:
        output_dir = output_dir.replace("//", scene_path)

    pixels_pos = list()
    pixels_nrm = list()
    width = 0
    
    for i in range(frame_range[1] - frame_range[0]):
        f          = i + frame_range[0]
        temp_obj   = new_object_from_frame(obj, f)
        new_pixels = get_vertex_data_from_frame(temp_obj, scale)
        width      = len(new_pixels)

        for pixel in new_pixels:
            pixels_pos += pixel[0]
            pixels_nrm += pixel[1]

    height = frame_range[1] - frame_range[0]

    write_output_image(pixels_pos, name + '_position', [width, height], output_dir)
    write_output_image(pixels_nrm, name + '_normal', [width, height], output_dir)

    frame_zero = get_export_object(obj, 0)
    create_morph_uv_set(frame_zero)
    export_mesh(frame_zero, output_dir, name)

    return frame_zero


def write_output_image(pixel_list, name, size, output_dir):
    image = bpy.data.images.new(name, width=size[0], height=size[1])
    image.pixels = pixel_list
    image.save_render(output_dir + name + ".png", scene=bpy.context.scene)


def new_object_from_frame(obj, f):
    context = bpy.context
    scene   = context.scene
    scene.frame_set(f)  

    dg        = context.view_layer.depsgraph
    eval_obj  = obj.evaluated_get(dg)
    duplicate = bpy.data.objects.new('clone', bpy.data.meshes.new_from_object(eval_obj))

    return duplicate

def get_export_object(obj, f):
    context = bpy.context
    scene   = context.scene
    scene.frame_set(f)  

    dg        = context.view_layer.depsgraph
    eval_obj  = obj.evaluated_get(dg)
    duplicate = bpy.data.objects.new('export', bpy.data.meshes.new_from_object(eval_obj))

    return duplicate

def get_vertex_data_from_frame(obj, position_scale):
    obj.data.calc_tangents()
    vertex_data = [None] * len(obj.data.vertices)

    for face in obj.data.polygons:
        for vert in [obj.data.loops[i] for i in face.loop_indices]:
            index    = vert.vertex_index
            normal   = unsign_vector(vert.normal.copy())
            position = unsign_vector(obj.data.vertices[index].co.copy() / position_scale)

            # Image object expects RGBA, append A
            normal.append(1.0)
            position.append(1.0)

            vertex_data[index] = [position, normal, 0]

    return vertex_data


def unsign_vector(vec, as_list=True):
    """ Rescale input vector from -1..1 to 0..1.
    """
    vec += mathutils.Vector((1.0, 1.0, 1.0))
    vec /= 2.0

    if as_list:
        return list(vec.to_tuple())
    else:
        return vec


def create_morph_uv_set(obj):
    bm = bmesh.new()
    bm.from_mesh(obj.data)

    #not sure why i make two but thats also what houdini does
    uv_layer = bm.loops.layers.uv.new("uv")
    uv_layer2 = bm.loops.layers.uv.new("uv2")
    
    pixel_size = 1.0 / len(bm.verts)

    i = 0
    for v in bm.verts:
        for l in v.link_loops:
            uv_data = l[uv_layer]
            uv_data.uv = mathutils.Vector((i * pixel_size, 0.0))
        i += 1
        
    exportobj = bm;
    bm.to_mesh(obj.data)

def export_mesh(obj, output_dir, name):
    context = bpy.context
    context.collection.objects.link(obj)
    context.view_layer.objects.active = obj
    
    #this is super ugly but works
    bpy.data.objects['export'].select_set(True)
    bpy.data.objects['Plane'].select_set(False)
    
    output_dir = output_dir + name + "_" + "mesh.fbx"

    bpy.ops.export_scene.fbx(use_selection=True, filepath=output_dir)
    
    
#actually run the whole thing
bake_morph_textures(obj1, frame_range1, scale1, name1, output_dir1)
