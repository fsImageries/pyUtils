import os


# ------------------------- Maya information -------------------------- #
# --------------------------------------------------------------------- #

project_folders = [
    "assets", "autosave",
    "cache/nCache/fluid",
    "cache/particles",
    "clips", "data", "images", "movies",
    "renderData/depth",
    "renderData/fur",
    "renderData/fur/furAttrMap",
    "renderData/fur/furEqualMap",
    "renderData/fur/furFiles",
    "renderData/fur/furImages",
    "renderData/fur/furShadowMap",
    "renderData/iprImages",
    "renderData/shaders",
    "sceneAssembly"
    "scenes/edits",
    "scripts", "sound",
    "sourceimages/3dPaintTextures",
    "Time Editor/Clip Exports"
]


workspace_definition = """
//Maya 2020 Project Definition

workspace -fr "fluidCache" "cache/nCache/fluid";
workspace -fr "images" "images";
workspace -fr "offlineEdit" "scenes/edits";
workspace -fr "furShadowMap" "renderData/fur/furShadowMap";
workspace -fr "iprImages" "renderData/iprImages";
workspace -fr "FBX" "data";
workspace -fr "SVG" "data";
workspace -fr "renderData" "renderData";
workspace -fr "scripts" "scripts";
workspace -fr "fileCache" "cache/nCache";
workspace -fr "eps" "data";
workspace -fr "DAE_FBX" "data";
workspace -fr "shaders" "renderData/shaders";
workspace -fr "3dPaintTextures" "sourceimages/3dPaintTextures";
workspace -fr "translatorData" "data";
workspace -fr "mel" "scripts";
workspace -fr "furFiles" "renderData/fur/furFiles";
workspace -fr "OBJ" "data";
workspace -fr "particles" "cache/particles";
workspace -fr "scene" "scenes";
workspace -fr "FBX export" "data";
workspace -fr "furEqualMap" "renderData/fur/furEqualMap";
workspace -fr "sourceImages" "sourceimages";
workspace -fr "furImages" "renderData/fur/furImages";
workspace -fr "clips" "clips";
workspace -fr "DAE_FBX export" "data";
workspace -fr "depth" "renderData/depth";
workspace -fr "sceneAssembly" "sceneAssembly";
workspace -fr "teClipExports" "Time Editor/Clip Exports";
workspace -fr "movie" "movies";
workspace -fr "audio" "sound";
workspace -fr "autoSave" "autosave";
workspace -fr "mayaAscii" "scenes";
workspace -fr "move" "data";
workspace -fr "sound" "sound";
workspace -fr "diskCache" "data";
workspace -fr "illustrator" "data";
workspace -fr "mayaBinary" "scenes";
workspace -fr "templates" "assets";
workspace -fr "OBJexport" "data";
workspace -fr "furAttrMap" "renderData/fur/furAttrMap";
workspace -fr "timeEditor" "Time Editor";
"""


# ------------------- aimocap mahelper information -------------------- #
# --------------------------------------------------------------------- #


HOST = "localhost"
PORT = 6550
HEADER_SIZE = 10

