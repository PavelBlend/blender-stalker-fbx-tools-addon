import bpy


class StalkerFbxToolsPanel(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'scene'
    bl_label = 'STALKER Fbx Tools'

    def draw(self, context):
        lay = self.layout
        scn = context.scene
        lay.prop(scn.stalker_fbx_tools, 'input_dir')
        lay.prop(scn.stalker_fbx_tools, 'output_dir')
        lay.operator('stalker_fbx.convert_object_to_fbx')
