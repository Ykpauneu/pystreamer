from pysamp import call_native_function, register_callback
from samp import INVALID_PLAYER_ID, INVALID_VEHICLE_ID  # type: ignore
from typing import Optional


def register_callbacks() -> None:
    register_callback("OnDynamicObjectMoved", "i")
    register_callback("OnPlayerEditDynamicObject", "iiiffffff")
    register_callback("OnPlayerSelectDynamicObject", "iiifff")
    register_callback("OnPlayerShootDynamicObject", "iiifff")
    register_callback("OnPlayerPickUpDynamicPickup", "ii")
    register_callback("OnPlayerEnterDynamicCP", "ii")
    register_callback("OnPlayerLeaveDynamicCP", "ii")
    register_callback("OnPlayerEnterDynamicRaceCP", "ii")
    register_callback("OnPlayerLeaveDynamicRaceCP", "ii")
    register_callback("OnPlayerEnterDynamicArea", "ii")
    register_callback("OnPlayerLeaveDynamicArea", "ii")
    register_callback("OnPlayerGiveDamageDynamicActor", "iifii")
    register_callback("OnDynamicActorStreamIn", "ii")
    register_callback("OnDynamicActorStreamOut", "ii")
    register_callback("Streamer_OnItemStreamIn", "iii")
    register_callback("Streamer_OnItemStreamOut", "iii")
    register_callback("Streamer_OnPluginError", "s")


def get_tick_rate():
    return call_native_function("Streamer_GetTickRate")


def set_tick_rate(rate):
    return call_native_function("Streamer_SetTickRate", rate)


def get_player_tick_rate(player_id: int):
    return call_native_function("Streamer_GetPlayerTickRate", player_id)


def set_player_tick_rate(player_id: int, rate):
    return call_native_function("Streamer_SetPlayerTickRate", player_id, rate)


def toggle_chunk_stream(toggle: bool):
    return call_native_function("Streamer_ToggleChunkStream", toggle)


def is_toggle_chunk_stream() -> bool:
    return call_native_function("Streamer_IsToggleChunkStream")


def get_chunk_tick_rate(type, player_id: int = -1):
    return call_native_function("Streamer_GetChunkTickRate", type, player_id)


def set_chunk_tick_rate(type, rate, player_id: int = -1):
    return call_native_function(
        "Streamer_SetChunkTickRate", type, rate, player_id
    )


def get_chunk_size(type):
    return call_native_function("Streamer_GetChunkSize", type)


def set_chunk_size(type, size):
    return call_native_function("Streamer_SetChunkSize", type, size)


def get_max_item(type):
    return call_native_function("Streamer_GetMaxItems", type)


def set_max_items(type, items):
    return call_native_function("Streamer_SetMaxItems", type, items)


def get_visible_items(type, player_id: int = -1):
    return call_native_function("Streamer_GetVisibleItems", type, player_id)


def set_visible_items(type, items, player_id: int = -1):
    return call_native_function(
        "Streamer_SetVisibleItems", type, items, player_id
    )


def set_radius_multiplier(type, multiplier: float, player_id: int = -1):
    return call_native_function(
        "Streamer_SetRadiusMultiplier", type, float(multiplier), player_id
    )


def get_type_priority(types: list, maxtypes: int = 8):
    return call_native_function("Streamer_GetTypePriority", types, maxtypes)


def set_type_priority(types: list, maxtypes: int = 8):
    return call_native_function("Streamer_SetTypePriority", types, maxtypes)


def set_cell_distance(distance: float):
    return call_native_function("Streamer_SetCellDistance", float(distance))


def set_cell_size(size: float):
    return call_native_function("Streamer_SetCellSize", float(size))


def toggle_item_static(type, id, toggle):
    return call_native_function("Streamer_ToggleItemStatic", type, id, toggle)


def is_toggle_item_static(type, id) -> bool:
    return call_native_function("Streamer_IsToggleItemStatic", type, id)


def toggle_item_inv_areas(type, id, toggle):
    return call_native_function(
        "Streamer_ToggleItemInvAreas", type, id, toggle
    )


def is_toggle_item_inv_areas(type, id) -> bool:
    return call_native_function("Streamer_IsToggleItemInvAreas", type, id)


def toggle_item_callbacks(type, id, toggle):
    return call_native_function(
        "Streamer_ToggleItemCallbacks", type, id, toggle
    )


def is_toggle_item_callbacks(type, id) -> bool:
    return call_native_function("Streamer_IsToggleItemCallbacks", type, id)


def toggle_error_callback(toggle):
    return call_native_function("Streamer_ToggleErrorCallback", toggle)


def is_toggle_error_callback() -> bool:
    return call_native_function("Streamer_IsToggleErrorCallback")


def amx_unload_destroy_items(toggle):
    return call_native_function("Streamer_AmxUnloadDestroyItems", toggle)


def process_active_items():
    return call_native_function("Streamer_ProcessActiveItems")


def toggle_idle_update(player_id: int, toggle: bool):
    return call_native_function("Streamer_ToggleIdleUpdate", player_id, toggle)


def is_toggle_idle_update(player_id: int) -> bool:
    return call_native_function("Streamer_IsToggleIdleUpdate", player_id)


def toggle_camera_update(player_id: int, toggle):
    return call_native_function(
        "Streamer_ToggleCameraUpdate", player_id, toggle
    )


def is_toggle_camera_update(player_id: int) -> bool:
    return call_native_function("Streamer_IsToggleCameraUpdate", player_id)


def toggle_item_updadte(player_id: int, type, toggle):
    return call_native_function(
        "Streamer_ToggleItemUpdate", player_id, type, toggle
    )


def is_toggle_item_updadte(player_id: int, type) -> bool:
    return call_native_function("Streamer_IsToggleItemUpdate", player_id, type)


def update(player_id: int, type: int = -1):
    return call_native_function("Streamer_Update", player_id, type)


def update_ex(
    player_id: int,
    x: float,
    y: float,
    z: float,
    world_id: int = -1,
    interior_id: int = -1,
    type: int = -1,
    compensated_time: int = -1,
    freeze_player: bool = True,
):
    return call_native_function(
        "Streamer_UpdateEx",
        player_id,
        float(x),
        float(y),
        float(z),
        world_id,
        interior_id,
        type,
        compensated_time,
        freeze_player,
    )


def set_float_data(type, id, data, value: float) -> bool:
    return call_native_function(
        "Streamer_SetFloatData", type, id, data, float(value)
    )


def get_int_data(type, id, data):
    return call_native_function("Streamer_GetIntData", type, id, data)


def set_int_data(type, id, data, value) -> bool:
    return call_native_function("Streamer_SetIntData", type, id, data, value)


def remove_int_data(type, id, data) -> bool:
    return call_native_function("Streamer_RemoveIntData", type, id, data)


def has_int_data(type, id, data) -> bool:
    return call_native_function("Streamer_HasIntData", type, id, data)


def get_array_data(type, id, data, dest: list) -> bool:
    return call_native_function(
        "Streamer_GetArrayData", type, id, dest, len(dest)
    )


def set_array_data(type, id, data, scr: list) -> bool:
    return call_native_function(
        "Streamer_SetArrayData", type, id, data, scr, len(scr)
    )


def is_in_array_data(type, id, data, value) -> bool:
    return call_native_function(
        "Streamer_IsInArrayData", type, id, data, value
    )


def append_array_data(type, id, data, value) -> bool:
    return call_native_function(
        "Streamer_AppendArrayData", type, id, data, value
    )


def remove_array_data(type, id, data, value) -> bool:
    return call_native_function(
        "Streamer_RemoveArrayData", type, id, data, value
    )


def has_array_data(type, id, data) -> bool:
    return call_native_function("Streamer_HasArrayData", type, id, data)


def get_array_data_length(type, id, data):
    return call_native_function("Streamer_GetArrayDataLength", type, id, data)


def get_upper_bound(type):
    return call_native_function("Streamer_GetUpperBound", type)


def toggle_item(player_id: int, type, id, toggle: bool):
    return call_native_function(
        "Streamer_ToggleItem", player_id, type, id, toggle
    )


def is_toggle_item(player_id: int, type, id) -> bool:
    return call_native_function("Streamer_IsToggleItem", player_id, type, id)


def toggle_all_items(player_id: int, type, toggle, *exceptions):
    return call_native_function(
        "Streamer_ToggleAllItems",
        player_id,
        type,
        toggle,
        tuple(exceptions),
        len(exceptions),
    )


def get_item_internal_id(player_id: int, type, streamer_id: int):
    return call_native_function(
        "Streamer_GetItemInternalID", player_id, type, streamer_id
    )


def get_item_streamer_id(player_id: int, type, internal_id: int):
    return call_native_function(
        "Streamer_GetItemStreamerID", player_id, type, internal_id
    )


def is_item_visible(player_id: int, type, id) -> bool:
    return call_native_function("Streamer_IsItemVisible", player_id, type, id)


def destroy_all_visible_items(player_id: int, type, server_wide: bool = True):
    return call_native_function(
        "Streamer_DestroyAllVisibleItems", player_id, type, server_wide
    )


def count_visible_items(player_id: int, type, server_wide: bool = True):
    return call_native_function(
        "Streamer_CountVisibleItems", player_id, type, server_wide
    )


def destroy_all_items(type, server_wide: bool = True):
    return call_native_function("Streamer_DestroyAllItems", type, server_wide)


def count_items(type, server_wide: bool = True):
    return call_native_function("Streamer_CountItems", type, server_wide)


def get_nearby_items(
    x: float,
    y: float,
    z: float,
    items: list,
    range: float = 300.0,
    world_id: int = -1,
):
    return call_native_function(
        "Streamer_GetNearbyItems",
        float(x),
        float(y),
        float(z),
        type,
        items,
        len(items),
        range,
        world_id,
    )


def get_all_visible_items(player_id: int, type, items: list):
    return call_native_function(
        "Streamer_GetAllVisibleItems", player_id, type, len(items)
    )


def get_item_pos(type, id, x: float, y: float, z: float):
    return call_native_function(
        "Streamer_GetItemPos", type, id, float(x), float(y), float(z)
    )


def set_item_pos(type, id, x: float, y: float, z: float):
    return call_native_function(
        "Streamer_SetItemPos", type, id, float(x), float(y), float(z)
    )


def set_item_off_set(type, id, x: float, y: float, z: float):
    return call_native_function(
        "Streamer_SetItemOffset", type, id, float(x), float(y), float(z)
    )


def create_dynamic_object(
    model_id: int,
    x: float,
    y: float,
    z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    stream_distance: float = 300.0,
    draw_distance: float = 0.0,
    area_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicObject",
        model_id,
        float(x),
        float(y),
        float(z),
        float(rotation_x),
        float(rotation_y),
        float(rotation_z),
        world_id,
        interior_id,
        player_id,
        float(stream_distance),
        float(draw_distance),
        area_id,
        priority,
    )


def destroy_dynamic_object(object_id: int):
    return call_native_function("DestroyDynamicObject", object_id)


def is_valid_dynamic_object(object_id: int) -> bool:
    return call_native_function("IsValidDynamicObject", object_id)


def set_dynamic_object_pos(object_id: int, x: float, y: float, z: float):
    return call_native_function(
        "SetDynamicObjectPos", object_id, float(x), float(y), float(z)
    )


def set_dynamic_object_rot(
    object_id: int, rotation_x: float, rotation_y: float, rotation_z: float
):
    return call_native_function(
        "SetDynamicObjectRot",
        object_id,
        float(rotation_x),
        float(rotation_y),
        float(rotation_z)
    )


def get_dynamic_object_no_camera_col(object_id: int):
    return call_native_function("GetDynamicObjectNoCameraCol", object_id)


def set_dynamic_object_no_camera_col(object_id: int):
    return call_native_function("SetDynamicObjectNoCameraCol", object_id)


def move_dynamic_object(
    object_id: int,
    x: float,
    y: float,
    z: float,
    speed: float,
    rotation_x: float = -1000.0,
    rotation_y: float = -1000.0,
    rotation_z: float = -1000.0,
):
    return call_native_function(
        "MoveDynamicObject",
        object_id,
        float(x),
        float(y),
        float(z),
        float(speed),
        float(rotation_x),
        float(rotation_y),
        float(rotation_z),
    )


def stop_dynamic_object(object_id: int):
    return call_native_function("StopDynamicObject", object_id)


def is_dynamic_object_moving(object_id: int) -> bool:
    return call_native_function("IsDynamicObjectMoving", object_id)


def attach_camera_to_dynamic_object(player_id: int, object_id: int):
    return call_native_function(
        "AttachCameraToDynamicObject", player_id, object_id
    )


def attach_dynamic_object_to_object(
    object_id: int,
    attach_to_id: int,
    offset_x: float,
    offset_y: float,
    offset_z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
    syncrotation: bool = True,
):
    return call_native_function(
        "AttachDynamicObjectToObject",
        object_id,
        attach_to_id,
        float(offset_x),
        float(offset_y),
        float(offset_z),
        float(rotation_x),
        float(rotation_y),
        float(rotation_z),
        syncrotation,
    )


def attach_dynamic_object_to_player(
    object_id: int,
    player_id: int,
    offset_x: float,
    offset_y: float,
    offset_z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
):
    return call_native_function(
        "AttachDynamicObjectToPlayer",
        object_id,
        player_id,
        float(offset_x),
        float(offset_y),
        float(offset_z),
        float(rotation_x),
        float(rotation_y),
        float(rotation_z),
    )


def attach_dynamic_object_to_vehicle(
    object_id: int,
    vehicle_id: int,
    offset_x: float,
    offset_y: float,
    offset_z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
):
    return call_native_function(
        "AttachDynamicObjectToVehicle",
        object_id,
        vehicle_id,
        float(offset_x),
        float(offset_y),
        float(offset_z),
        float(rotation_x),
        float(rotation_y),
        float(rotation_z),
    )


def edit_dynamic_object(player_id: int, object_id: int):
    return call_native_function("EditDynamicObject", player_id, object_id)


def is_dynamic_object_material_used(object_id: int, material_index) -> bool:
    return call_native_function(
        "IsDynamicObjectMaterialUsed", object_id, material_index
    )


def remove_dynamic_object_material(object_id: int, material_index):
    return call_native_function(
        "RemoveDynamicObjectMaterial", object_id, material_index
    )


def set_dynamic_object_material(
    object_id: int,
    material_index: int,
    model_id: int,
    txd_name: str,
    texturename: str,
    material_color: int = 0x00000000,
):
    return call_native_function(
        "SetDynamicObjectMaterial",
        object_id,
        material_index,
        model_id,
        txd_name,
        texturename,
        material_color,
    )


def is_dynamic_object_material_text_used(
    object_id: int, material_index: int
) -> bool:
    return call_native_function(
        "IsDynamicObjectMaterialTextUsed", object_id, material_index
    )


def remove_dynamic_object_material_text(object_id: int, material_index: int):
    return call_native_function(
        "RemoveDynamicObjectMaterialText", object_id, material_index
    )


def set_dynamic_object_material_text(
    object_id: int,
    material_index: int,
    text: str,
    material_size: int = 90,
    font_face: str = "Arial",
    font_size: int = 24,
    bold: bool = True,
    font_color: int = 0xFFFFFFFF,
    back_color: int = 0x00000000,
    text_alignment: int = 0,
):
    return call_native_function(
        "SetDynamicObjectMaterialText",
        object_id,
        material_index,
        text,
        material_size,
        font_face,
        font_size,
        bold,
        font_color,
        back_color,
        text_alignment,
    )


def get_player_camera_target_dyn_object(player_id: int):
    return call_native_function("GetPlayerCameraTargetDynObject", player_id)


def create_dynamic_pickup(
    model_id: int,
    type: int,
    x: float,
    y: float,
    z: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    stream_distance: float = 200.0,
    area_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicPickup",
        model_id,
        type,
        float(x),
        float(y),
        float(z),
        world_id,
        interior_id,
        player_id,
        float(stream_distance),
        area_id,
        priority,
    )


def destroy_dynamic_pickup(pickup_id: int):
    return call_native_function("DestroyDynamicPickup", pickup_id)


def is_valid_dynamic_pickup(pickup_id: int) -> bool:
    return call_native_function("IsValidDynamicPickup", pickup_id)


def create_dynamic_cp(
    x: float,
    y: float,
    z: float,
    size: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    stream_distance: float = 200.0,
    area_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicCP",
        float(x),
        float(y),
        float(z),
        float(size),
        world_id,
        interior_id,
        player_id,
        float(stream_distance),
        area_id,
        priority,
    )


def destroy_dynamic_cp(checkpoint_id: int):
    return call_native_function("DestroyDynamicCP", checkpoint_id)


def is_valid_dynamic_cp(checkpoint_id: int) -> bool:
    return call_native_function("IsValidDynamicCP", checkpoint_id)


def is_player_in_dynamic_cp(player_id: int, checkpoint_id: int) -> bool:
    return call_native_function(
        "IsPlayerInDynamicCP", player_id, checkpoint_id
    )


def get_player_visible_dynamic_cp(player_id: int):
    return call_native_function("GetPlayerVisibleDynamicCP", player_id)


def create_dynamic_race_cp(
    type,
    x: float,
    y: float,
    z: float,
    next_x: float,
    next_y: float,
    next_z: float,
    size: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    stream_distance: float = 200.0,
    area_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicRaceCP",
        type,
        float(x),
        float(y),
        float(z),
        float(next_x),
        float(next_y),
        float(next_z),
        float(size),
        world_id,
        interior_id,
        player_id,
        float(stream_distance),
        area_id,
        priority,
    )


def destroy_dynamic_race_cp(checkpoint_id: int):
    return call_native_function("DestroyDynamicRaceCP", checkpoint_id)


def is_valid_dynamic_race_cp(checkpoint_id: int) -> bool:
    return call_native_function("IsValidDynamicRaceCP", checkpoint_id)


def is_player_in_dynamic_race_cp(player_id: int, checkpoint_id: int) -> bool:
    return call_native_function(
        "IsPlayerInDynamicRaceCP", player_id, checkpoint_id
    )


def get_player_visible_dynamic_race_cp(player_id: int):
    return call_native_function("GetPlayerVisibleDynamicRaceCP", player_id)


def create_dynamic_map_icon(
    x: float,
    y: float,
    z: float,
    type: int,
    color: int,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    stream_distance: float = 200.0,
    style: int = 0,
    area_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicMapIcon",
        float(x),
        float(y),
        float(z),
        type,
        color,
        world_id,
        interior_id,
        player_id,
        float(stream_distance),
        style,
        area_id,
        priority,
    )


def destroy_dynamic_map_icon(icon_id: int):
    return call_native_function("DestroyDynamicMapIcon", icon_id)


def is_valid_dynamic_map_icon(icon_id: int) -> bool:
    return call_native_function("IsValidDynamicMapIcon", icon_id)


def create_dynamic_3d_text_label(
    text: str,
    color: int,
    x: float,
    y: float,
    z: float,
    draw_distance: float,
    attached_player: int = INVALID_PLAYER_ID,
    attached_vehicle: int = INVALID_VEHICLE_ID,
    testlos: bool = False,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    stream_distance: float = 200.0,
    area_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamic3DTextLabel",
        text,
        color,
        float(x),
        float(y),
        float(z),
        float(draw_distance),
        attached_player,
        attached_vehicle,
        testlos,
        world_id,
        interior_id,
        player_id,
        float(stream_distance),
        area_id,
        priority,
    )


def destroy_dynamic_3d_text_label(id: int):
    return call_native_function("DestroyDynamic3DTextLabel", id)


def is_valid_dynamic_3d_text_label(id: int) -> bool:
    return call_native_function("IsValidDynamic3DTextLabel", id)


def get_dynamic_3d_text_label_text(id: int, text: str) -> str:
    return call_native_function(
        "GetDynamic3DTextLabelText", id, text, len(text)
    )


def update_dynamic_3d_text_label_text(id: int, color: int, text: str):
    return call_native_function(
        "UpdateDynamic3DTextLabelText", id, color, text
    )


def create_dynamic_circle(
    x: float,
    y: float,
    size: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicCircle",
        float(x),
        float(y),
        float(size),
        world_id,
        interior_id,
        player_id,
        priority,
    )


def create_dynamic_cylinder(
    x: float,
    y: float,
    min_z: float,
    max_z: float,
    size: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicCylinder",
        float(x),
        float(y),
        float(min_z),
        float(max_z),
        float(size),
        world_id,
        interior_id,
        player_id,
        priority,
    )


def create_dynamic_sphere(
    x: float,
    y: float,
    z: float,
    size: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicSphere",
        float(x),
        float(y),
        float(z),
        float(size),
        world_id,
        interior_id,
        player_id,
        priority,
    )


def create_dynamic_rectangle(
    min_x: float,
    min_y: float,
    max_x: float,
    max_y: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicRectangle",
        float(min_x),
        float(min_y),
        float(max_x),
        float(max_y),
        world_id,
        interior_id,
        player_id,
        priority,
    )


def create_dynamic_cuboid(
    min_x: float,
    min_y: float,
    min_z: float,
    max_x: float,
    max_y: float,
    max_z: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicCuboid",
        float(min_x),
        float(min_y),
        float(min_z),
        float(max_x),
        float(max_y),
        float(max_z),
        world_id,
        interior_id,
        player_id,
        priority,
    )


def create_dynamic_cube(
    min_x: float,
    min_y: float,
    min_z: float,
    max_x: float,
    max_y: float,
    max_z: float,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicCube",
        float(min_x),
        float(min_y),
        float(min_z),
        float(max_x),
        float(max_y),
        float(max_z),
        world_id,
        interior_id,
        player_id,
        priority,
    )


def create_dynamic_polygon(
    points: list[float],
    min_z: float = -2139095040.0,
    max_z: float = 2139095040.0,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicPolygon",
        points,
        float(min_z),
        float(max_z),
        len(points),
        world_id,
        interior_id,
        player_id,
        priority,
    )


def destroy_dynamic_area(area_id: int):
    return call_native_function("DestroyDynamicArea", area_id)


def is_valid_dynamic_area(area_id: int) -> bool:
    return call_native_function("IsValidDynamicArea", area_id)


def get_dynamic_area_type(area_id: int):
    return call_native_function("GetDynamicAreaType", area_id)


def get_dynamic_polygon_points(area_id: int, points: list[float]):
    return call_native_function(
        "GetDynamicPolygonPoints", area_id, points, len(points)
    )


def get_dynamic_polygon_number_points(area_id: int):
    return call_native_function("GetDynamicPolygonNumberPoints", area_id)


def is_player_in_dynamic_area(
    player_id: int,
    area_id: int,
    recheck: bool = False
) -> bool:
    return call_native_function(
        "IsPlayerInDynamicArea", player_id, area_id, recheck
    )


def is_player_in_any_dynamic_area(
    player_id: int,
    recheck: bool = False
) -> bool:
    return call_native_function("IsPlayerInAnyDynamicArea", player_id, recheck)


def is_any_player_in_dynamic_area(
    area_id: int,
    recheck: bool = False
) -> bool:
    return call_native_function("IsAnyPlayerInDynamicArea", area_id, recheck)


def is_any_player_in_any_dynamic_area(recheck: bool = False):
    return call_native_function("IsAnyPlayerInAnyDynamicArea", recheck)


def get_player_dynamic_areas(player_id: int, areas: list):
    return call_native_function(
        "GetPlayerDynamicAreas", player_id, tuple(areas), len(areas)
    )


def get_player_number_dynamic_areas(player_id: int):
    return call_native_function("GetPlayerNumberDynamicAreas", player_id)


def is_point_in_dynamic_area(
    area_id: int,
    x: float,
    y: float,
    z: float
) -> bool:
    return call_native_function(
        "IsPointInDynamicArea",
        area_id,
        float(x),
        float(y),
        float(z)
    )


def is_point_in_any_dynamic_area(
    x: float,
    y: float,
    z: float
) -> bool:
    return call_native_function(
        "IsPointInAnyDynamicArea",
        float(x),
        float(y),
        float(z)
    )


def is_line_in_dynamic_area(
    area_id: int,
    x: float,
    y: float,
    z: float,
    x_1: float,
    y_1: float,
    z_1: float,
) -> bool:
    return call_native_function(
        "IsLineInDynamicArea",
        area_id,
        float(x),
        float(y),
        float(z),
        float(x_1),
        float(y_1),
        float(z_1)
    )


def is_line_in_any_dynamic_area(
    x: float, y: float, z: float, x_1: float, y_1: float, z_1: float
) -> bool:
    return call_native_function(
        "IsLineInAnyDynamicArea",
        float(x),
        float(y),
        float(z),
        float(x_1),
        float(y_1),
        float(z_1)
    )


def get_dynamic_areas_for_point(x: float, y: float, z: float, areas: list):
    return call_native_function(
        "GetDynamicAreasForPoint",
        float(x),
        float(y),
        float(z),
        tuple(areas),
        len(areas)
    )


def get_number_dynamic_areas_for_point(x: float, y: float, z: float):
    return call_native_function(
        "GetNumberDynamicAreasForPoint",
        float(x),
        float(y),
        float(z)
    )


def get_dynamic_areas_for_line(
    x: float,
    y: float,
    z: float,
    x_1: float,
    y_1: float,
    z_1: float,
    areas: list,
):
    return call_native_function(
        "GetDynamicAreasForLine",
        float(x),
        float(y),
        float(z),
        float(x_1),
        float(y_1),
        float(z_1),
        tuple(areas),
        len(areas)
    )


def get_number_dynamic_areas_for_line(
    x: float, y: float, z: float, x_1: float, y_1: float, z_1: float
):
    return call_native_function(
        "GetNumberDynamicAreasForLine",
        float(x),
        float(y),
        float(z),
        float(x_1),
        float(y_1),
        float(z_1)
    )


def attach_dynamic_area_to_object(
    area_id: int,
    object_id: int,
    type: int = 2,
    player_id: int = INVALID_PLAYER_ID,
    offset_x: float = 0.0,
    offset_y: float = 0.0,
    offset_z: float = 0.0,
):
    return call_native_function(
        "AttachDynamicAreaToObject",
        area_id,
        object_id,
        type,
        player_id,
        float(offset_x),
        float(offset_y),
        float(offset_z),
    )


def attach_dynamic_area_to_player(
    area_id: int,
    player_id: int,
    offset_x: float = 0.0,
    offset_y: float = 0.0,
    offset_z: float = 0.0,
):
    return call_native_function(
        "AttachDynamicAreaToPlayer",
        area_id,
        player_id,
        float(offset_x),
        float(offset_y),
        float(offset_z),
    )


def attach_dynamic_area_to_vehicle(
    area_id: int,
    vehicle_id: int,
    offset_x: float = 0.0,
    offset_y: float = 0.0,
    offset_z: float = 0.0,
):
    return call_native_function(
        "AttachDynamicAreaToVehicle",
        area_id,
        vehicle_id,
        float(offset_x),
        float(offset_y),
        float(offset_z),
    )


def toggle_dyn_area_spectate_mode(area_id: int, toggle: bool):
    return call_native_function("ToggleDynAreaSpectateMode", area_id, toggle)


def is_toggle_dyn_area_spectate_mode(area_id: int) -> bool:
    return call_native_function("IsToggleDynAreaSpectateMode", area_id)


def create_dynamic_actor(
    model_id: int,
    x: float,
    y: float,
    z: float,
    rotation: float,
    invulnerable: bool = True,
    health: float = 100.0,
    world_id: int = -1,
    interior_id: int = -1,
    player_id: int = -1,
    stream_distance: float = 200.0,
    area_id: int = -1,
    priority: int = 0,
):
    return call_native_function(
        "CreateDynamicActor",
        model_id,
        float(x),
        float(y),
        float(z),
        float(rotation),
        invulnerable,
        float(health),
        world_id,
        interior_id,
        player_id,
        float(stream_distance),
        area_id,
        priority,
    )


def destroy_dynamic_actor(actor_id: int):
    return call_native_function("DestroyDynamicActor", actor_id)


def is_valid_dynamic_actor(actor_id: int) -> bool:
    return call_native_function("IsValidDynamicActor", actor_id)


def is_dynamic_actor_streamed_in(actor_id: int, for_player_id: int) -> bool:
    return call_native_function(
        "IsDynamicActorStreamedIn", actor_id, for_player_id
    )


def get_dynamic_actor_virtual_world(actor_id: int):
    return call_native_function("GetDynamicActorVirtualWorld", actor_id)


def set_dynamic_actor_virtual_world(actor_id: int, virtual_world: int):
    return call_native_function(
        "SetDynamicActorVirtualWorld", actor_id, virtual_world
    )


def get_dynamic_actor_animation(
    actor_id: int,
    anim_lib: str,
    anim_name: str,
    delta: float,
    loop: int,
    lock_x: int,
    lock_y: int,
    freeze: int,
    time: int,
):
    return call_native_function(
        "GetDynamicActorAnimation",
        actor_id,
        anim_lib,
        anim_name,
        float(delta),
        loop,
        lock_x,
        lock_y,
        freeze,
        time,
        len(anim_lib),
        len(anim_name),
    )


def apply_dynamic_actor_animation(
    actor_id: int,
    anim_lib: str,
    anim_name: str,
    delta: float,
    loop: int,
    lock_x: int,
    lock_y: int,
    freeze: int,
    time: int,
):
    return call_native_function(
        "ApplyDynamicActorAnimation",
        actor_id,
        anim_lib,
        anim_name,
        float(delta),
        loop,
        lock_x,
        lock_y,
        freeze,
        time,
    )


def clear_dynamic_actor_animations(actor_id: int):
    return call_native_function("ClearDynamicActorAnimations", actor_id)


def set_dynamic_actor_facing_angle(actor_id: int, angle: float):
    return call_native_function(
        "SetDynamicActorFacingAngle", actor_id, float(angle)
    )


def set_dynamic_actor_pos(actor_id: int, x: float, y: float, z: float):
    return call_native_function(
        "SetDynamicActorPos", actor_id, float(x), float(y), float(z)
    )


def set_dynamic_actor_health(actor_id: int, health: float):
    return call_native_function(
        "SetDynamicActorHealth", actor_id, float(health)
    )


def set_dynamic_actor_invulnerable(actor_id: int, invulnerable: bool = True):
    return call_native_function(
        "SetDynamicActorInvulnerable", actor_id, invulnerable
    )


def is_dynamic_actor_invulnerable(actor_id: int) -> bool:
    return call_native_function("IsDynamicActorInvulnerable", actor_id)


def get_player_target_dynamic_actor(player_id: int):
    return call_native_function("GetPlayerTargetDynamicActor", player_id)


def get_player_camera_target_dyn_actor(player_id: int):
    return call_native_function("GetPlayerCameraTargetDynActor", player_id)


def create_dynamic_object_ex(
    model_id: int,
    x: float,
    y: float,
    z: float,
    rotation_x: float,
    rotation_y: float,
    rotation_z: float,
    stream_distance: float = 300.0,
    draw_distance: float = 0.0,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    areas: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    if areas is None:
        areas = [-1]

    return call_native_function(
        "CreateDynamicObjectEx",
        model_id,
        float(x),
        float(y),
        float(z),
        float(rotation_x),
        float(rotation_y),
        float(rotation_z),
        float(stream_distance),
        float(draw_distance),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        tuple(areas),
        priority,
        len(worlds),
        len(interiors),
        len(players),
        len(areas),
    )


def create_dynamic_pickup_ex(
    model_id: int,
    type: int,
    x: float,
    y: float,
    z: float,
    stream_distance: float = 200.0,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    areas: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    if areas is None:
        areas = [-1]

    return call_native_function(
        "CreateDynamicPickupEx",
        model_id,
        type,
        float(x),
        float(y),
        float(z),
        float(stream_distance),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        tuple(areas),
        priority,
        len(worlds),
        len(interiors),
        len(players),
        len(areas),
    )


def create_dynamic_cp_ex(
    x: float,
    y: float,
    z: float,
    size: float,
    stream_distance: float = 200.0,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    areas: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    if areas is None:
        areas = [-1]

    return call_native_function(
        "CreateDynamicCPEx",
        float(x),
        float(y),
        float(z),
        float(size),
        float(stream_distance),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        tuple(areas),
        priority,
        len(worlds),
        len(interiors),
        len(players),
        len(areas),
    )


def create_dynamic_race_cp_ex(
    type,
    x: float,
    y: float,
    z: float,
    next_x: float,
    next_y: float,
    next_z: float,
    size: float,
    stream_distance: float = 200.0,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    areas: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    if areas is None:
        areas = [-1]

    return call_native_function(
        "CreateDynamicRaceCPEx",
        type,
        float(x),
        float(y),
        float(z),
        float(next_x),
        float(next_y),
        float(next_z),
        float(size),
        float(stream_distance),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        tuple(areas),
        priority,
        len(worlds),
        len(interiors),
        len(players),
        len(areas),
    )


def create_dynamic_map_icon_ex(
    x: float,
    y: float,
    z: float,
    type: int,
    color: int,
    style: int = 0,
    stream_distance: float = 200.0,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    areas: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    if areas is None:
        areas = [-1]

    return call_native_function(
        "CreateDynamicMapIconEx",
        float(x),
        float(y),
        float(z),
        type,
        color,
        style,
        float(stream_distance),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        tuple(areas),
        priority,
        len(worlds),
        len(interiors),
        len(players),
        len(areas),
    )


def create_dynamic_3d_text_label_ex(
    text: str,
    color: int,
    x: float,
    y: float,
    z: float,
    draw_distance: float,
    attached_player: int = INVALID_PLAYER_ID,
    attached_vehicle: int = INVALID_VEHICLE_ID,
    testlos: bool = False,
    stream_distance: float = 200.0,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    areas: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    if areas is None:
        areas = [-1]

    return call_native_function(
        "CreateDynamic3DTextLabelEx",
        text,
        color,
        float(x),
        float(y),
        float(z),
        float(draw_distance),
        attached_player,
        attached_vehicle,
        testlos,
        float(stream_distance),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        tuple(areas),
        priority,
        len(worlds),
        len(interiors),
        len(players),
        len(areas),
    )


def create_dynamic_circle_ex(
    x: float,
    y: float,
    size: float,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    return call_native_function(
        "CreateDynamicCircleEx",
        float(x),
        float(y),
        float(size),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        priority,
        len(worlds),
        len(interiors),
        len(players),
    )


def create_dynamic_cylinder_ex(
    x: float,
    y: float,
    min_z: float,
    max_z: float,
    size: float,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    return call_native_function(
        "CreateDynamicCylinderEx",
        float(x),
        float(y),
        float(min_z),
        float(max_z),
        float(size),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        priority,
        len(worlds),
        len(interiors),
        len(players),
    )


def create_dynamic_sphere_ex(
    x: float,
    y: float,
    z: float,
    size: float,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    return call_native_function(
        "CreateDynamicSphereEx",
        float(x),
        float(y),
        float(z),
        float(size),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        priority,
        len(worlds),
        len(interiors),
        len(players),
    )


def create_dynamic_rectangle_ex(
    min_x: float,
    min_y: float,
    max_x: float,
    max_y: float,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    return call_native_function(
        "CreateDynamicRectangleEx",
        float(min_x),
        float(min_y),
        float(max_x),
        float(max_y),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        priority,
        len(worlds),
        len(interiors),
        len(players),
    )


def create_dynamic_cuboid_ex(
    min_x: float,
    min_y: float,
    min_z: float,
    max_x: float,
    max_y: float,
    max_z: float,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    return call_native_function(
        "CreateDynamicCuboidEx",
        float(min_x),
        float(min_y),
        float(min_z),
        float(max_x),
        float(max_y),
        float(max_z),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        priority,
        len(worlds),
        len(interiors),
        len(players),
    )


def create_dynamic_cube_ex(
    min_x: float,
    min_y: float,
    min_z: float,
    max_x: float,
    max_y: float,
    max_z: float,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    return call_native_function(
        "CreateDynamicCubeEx",
        float(min_x),
        float(min_y),
        float(min_z),
        float(max_x),
        float(max_y),
        float(max_z),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        priority,
        len(worlds),
        len(interiors),
        len(players),
    )


def create_dynamic_polygon_ex(
    points: list[float],
    min_z: float = -2139095040.0,
    max_z: float = 2139095040.0,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    return call_native_function(
        "CreateDynamicPolygonEx",
        points,
        float(min_z),
        float(max_z),
        len(points),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        priority,
        len(worlds),
        len(interiors),
        len(players),
    )


def create_dynamic_actor_ex(
    model_id: int,
    x: float,
    y: float,
    z: float,
    rotation: float,
    invulnerable: bool = True,
    health: float = 100.0,
    stream_distance: float = 200.0,
    worlds: Optional[list[int]] = None,
    interiors: Optional[list[int]] = None,
    players: Optional[list[int]] = None,
    areas: Optional[list[int]] = None,
    priority: int = 0,
):
    if worlds is None:
        worlds = [-1]

    if interiors is None:
        interiors = [-1]

    if players is None:
        players = [-1]

    if areas is None:
        areas = [-1]

    return call_native_function(
        "CreateDynamicActorEx",
        model_id,
        float(x),
        float(y),
        float(z),
        float(rotation),
        invulnerable,
        float(health),
        float(stream_distance),
        tuple(worlds),
        tuple(interiors),
        tuple(players),
        tuple(areas),
        priority,
        len(areas),
        len(worlds),
        len(interiors),
        len(players),
    )


# Natives (Deprecated)


def destroy_all_dynamic_object():
    return call_native_function("DestroyAllDynamicObjects")


def count_dynamic_object():
    return call_native_function("CountDynamicObjects")


def destroy_all_dynamic_pickups():
    return call_native_function("DestroyAllDynamicPickups")


def count_dynamic_pickups():
    return call_native_function("CountDynamicPickups")


def destroy_all_dynamic_cps():
    return call_native_function("DestroyAllDynamicCPs")


def count_dynamic_cps():
    return call_native_function("CountDynamicCPs")


def destroy_all_dynamic_race_cps():
    return call_native_function("DestroyAllDynamicRaceCPs")


def count_dynamic_race_cps():
    return call_native_function("CountDynamicRaceCPs")


def destroy_all_dynamic_map_icons():
    return call_native_function("DestroyAllDynamicMapIcons")


def count_dynamic_map_icons():
    return call_native_function("CountDynamicMapIcons")


def destroy_all_dynamic_3d_text_labels():
    return call_native_function("DestroyAllDynamic3DTextLabels")


def count_dynamic_3d_text_labels():
    return call_native_function("CountDynamic3DTextLabels")


def destroy_all_dynamic_areas():
    return call_native_function("DestroyAllDynamicAreas")


def count_dynamic_areas():
    return call_native_function("CountDynamicAreas")


def toggle_player_dynamic_cp(player_id: int, checkpoint_id: int, toggle: bool):
    return call_native_function(
        "TogglePlayerDynamicCP", player_id, checkpoint_id, toggle
    )


def toggle_player_all_dynamic_cps(
    player_id: int, toggle: bool, exceptions: Optional[list[int]] = None
):
    if exceptions is None:
        exceptions = [-1]

    return call_native_function(
        "TogglePlayerAllDynamicCPs",
        player_id,
        toggle,
        tuple(exceptions),
        len(exceptions),
    )


def toggle_player_dynamic_race_cp(
    player_id: int, checkpoint_id: int, toggle: bool
):
    return call_native_function(
        "TogglePlayerDynamicRaceCP", player_id, checkpoint_id, toggle
    )


def toggle_player_all_dynamic_race_cps(
    player_id: int, toggle: bool, exceptions: Optional[list[int]] = None
):
    if exceptions is None:
        exceptions = [-1]

    return call_native_function(
        "TogglePlayerAllDynamicRaceCPs",
        player_id,
        toggle,
        tuple(exceptions),
        len(exceptions),
    )


def toggle_player_dynamic_area(player_id: int, area_id: int, toggle: bool):
    return call_native_function(
        "TogglePlayerDynamicArea", player_id, area_id, toggle
    )


def toggle_player_all_dynamic_areas(
    player_id: int, toggle: bool, exceptions: Optional[list[int]] = None
):
    if exceptions is None:
        exceptions = [-1]

    return call_native_function(
        "TogglePlayerAllDynamicAreas",
        player_id,
        toggle,
        tuple(exceptions),
        len(exceptions),
    )
