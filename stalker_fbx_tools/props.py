import bpy


class StalkerFbxToolsProps(bpy.types.PropertyGroup):
    b_type = bpy.types.Scene

    input_dir = bpy.props.StringProperty(name='Input Dir', default='', subtype='DIR_PATH')
    output_dir = bpy.props.StringProperty(name='Output Dir', default='', subtype='DIR_PATH')
