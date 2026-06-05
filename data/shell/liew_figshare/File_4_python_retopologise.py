shell = bpy.context.active_object
number_of_apertures = len(bpy.context.active_object.data.splines)
number_of_points_for_each_aperture = len(bpy.context.active_object.data.splines[0].points)
bpy.context.scene.objects.active  = shell
shell.select = True
for each_point in list(range(0,number_of_points_for_each_aperture)):
    bpy.context.active_object.data.splines[(number_of_apertures-1)].points[each_point].select = True

bpy.ops.object.editmode_toggle()