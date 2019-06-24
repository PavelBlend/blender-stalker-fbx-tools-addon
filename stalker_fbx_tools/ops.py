import os

import bpy

import io_scene_xray


class StalkerFbxToolsOperator(bpy.types.Operator):
    bl_idname = 'stalker_fbx.convert_object_to_fbx'
    bl_label = 'Convert *.object to *.fbx'
    bl_options = {'REGISTER', 'UNDO'}

    shaped_bones = io_scene_xray.plugin_prefs.PropObjectBonesCustomShapes()
    fmt_version = io_scene_xray.plugin_prefs.PropSDKVersion()

    @io_scene_xray.utils.execute_with_logger
    @io_scene_xray.utils.set_cursor_state
    def execute(self, context):
        scn = context.scene

        old_objects = []
        for obj in bpy.data.objects:
            old_objects.append(obj.name)

        old_meshes = []
        for mesh in bpy.data.meshes:
            old_meshes(mesh.name)

        old_mats = []
        for mat in bpy.data.materials:
            old_mats(mat.name)

        old_texs = []
        for tex in bpy.data.textures:
            old_texs(tex.name)

        old_imgs = []
        for img in bpy.data.images:
            old_imgs(img.name)

        old_arms = []
        for arm in bpy.data.armatures:
            old_arms(arm.name)

        textures_folder = io_scene_xray.plugin_prefs.get_preferences().textures_folder_auto
        objects_folder = io_scene_xray.plugin_prefs.get_preferences().objects_folder

        context = io_scene_xray.obj.imp.utils.ImportContext(
            textures=textures_folder,
            soc_sgroups=self.fmt_version == 'soc',
            import_motions=False,
            split_by_materials=False,
            operator=self,
            use_motion_prefix_name=False,
            objects=objects_folder
        )
        context.before_import_file()
        bpy.ops.object.select_all(action='DESELECT')
        for root, dirs, files in os.walk(scn.stalker_fbx_tools.input_dir):
            for file in files:
                if file.endswith('.object'):
                    path = os.path.join(root, file)
                    io_scene_xray.obj.imp.import_file(path, context)
                    for obj in scn.objects:
                        if obj.name in old_objects:
                            continue
                        obj.select = True
                    if obj.name.endswith('.object'):
                        obj.name = obj.name[0 : -len('.object')]
                    dir_path = os.path.join(
                        scn.stalker_fbx_tools.output_dir,
                        obj.xray.export_path
                    )
                    if not os.path.exists(dir_path):
                        os.makedirs(dir_path)
                    bpy.ops.export_scene.fbx(
                        filepath=os.path.join(dir_path, obj.name) + '.fbx',
                        use_selection=True,
                        add_leaf_bones=False
                    )

                    for obj in bpy.data.objects:
                        if obj.name in old_objects:
                            continue
                        bpy.data.objects.remove(obj)

                    for mesh in bpy.data.meshes:
                        if mesh.name in old_meshes:
                            continue
                        bpy.data.meshes.remove(mesh)

                    for mat in bpy.data.materials:
                        if mat.name in old_mats:
                            continue
                        bpy.data.materials.remove(mat)

                    for tex in bpy.data.textures:
                        if tex.name in old_texs:
                            continue
                        bpy.data.textures.remove(tex)

                    for img in bpy.data.images:
                        if img.name in old_imgs:
                            continue
                        bpy.data.images.remove(img)

                    for arm in bpy.data.armatures:
                        if arm.name in old_arms:
                            continue
                        bpy.data.armatures.remove(arm)

        return {'FINISHED'}
