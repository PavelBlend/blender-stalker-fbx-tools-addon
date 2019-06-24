import bpy

from . import props
from . import ops
from . import ui


def register():
    bpy.utils.register_class(props.StalkerFbxToolsProps)
    props.StalkerFbxToolsProps.b_type.stalker_fbx_tools = \
        bpy.props.PointerProperty(type=props.StalkerFbxToolsProps)
    bpy.utils.register_class(ops.StalkerFbxToolsOperator)
    bpy.utils.register_class(ui.StalkerFbxToolsPanel)


def unregister():
    bpy.utils.unregister_class(ui.StalkerFbxToolsPanel)
    del props.StalkerFbxToolsProps.b_type.stalker_fbx_tools
    bpy.utils.unregister_class(props.StalkerFbxToolsProps)
    bpy.utils.unregister_class(ops.StalkerFbxToolsOperator)
