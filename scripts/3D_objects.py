'''
Author: Alex Cecil
email: ajcecil@iastate.edu
Date Created: 2024-12-12
Last Modified: 2024-15-12
Purpose: This script creates maps from drone imagery, imports the created imagery into a map, creates a scene for 3D object and imports 3D object into the scene and map.
Requirements: To use this script ODM and Docker need to be on the machine when using the ODM based functions, the instructions for both installations can be found at: https://docs.opendronemap.org/installation/. Any 3D files used need to be in a Binary GL Transmission Format (.glb) or a GL Transmission Format (.glTF)
'''

import arcpy as ap
import os
import ODM
import pandas as pd
import matplotlib.pyplot as plt
#region = Dictionary and variable Establishment
# Relative Directory Dictionary

rel_dir_dic = {
    'project directory' : 'pro_project/3D_UAS_Mapping/3D_UAS_Mapping.aprx',
    'geodatabase' :'pro_project/3D_UAS_Mapping/3D_UAS_Mapping.gdb',
    'pit locations' : 'data/pit_locations.csv',
    'pit locations corrected' : 'data/pit_locations_corrected.csv',
    'pit locations layer': 'kansas_soil_pit_locations',
    'arc environment' : 'pro_project',
    'test images' : 'images/test_images',
    'pits 1 and 2' : 'images/pits_1_and_2_Images',
    'pits 3 and 4' : 'images/pits_3_and_4_Images',
    'pits 5 and 6' : 'images/pits_5_and_6_Images',
    'pits 7 and 8' : 'images/pits_7_and_8_Images',
    'pits 9 and 10' : 'images/pits_9_and_10_Images',
    'pits 11 and 12' : 'images/pits_11_and_12_Images',
    'Processed UAS data' : 'maps/processed_maps',
    'Drone2Map DSM Layer' :'drone2map/Drone2Map_DSM_Layers.lyrx'
}

# Check directory script is in
script_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(script_dir)
print(f'script dir: {script_dir}')
print(f'parent dir: {parent_dir}')
joined = os.path.normpath(os.path.join(parent_dir,rel_dir_dic['project directory']))
print(f'Test: {joined}')
# Absolute Directory Dictionary
# This dictionary was created after having reoccuring issues with arcpy struggling to reference items through the relative directories.
dir_dic = {
    'project directory' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['project directory'])),
    'geodatabase' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['geodatabase'])),
    'pit locations' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['pit locations'])),
    'pit locations corrected' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['pit locations corrected'])),
    'pit locations layer': os.path.normpath(os.path.join(parent_dir, rel_dir_dic['geodatabase'], rel_dir_dic['pit locations layer'])),
    'arc environment' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['arc environment'])),
    'test images' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['test images'])),
    'pits 1 and 2' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['pits 1 and 2'])),
    'pits 3 and 4' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['pits 3 and 4'])),
    'pits 5 and 6' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['pits 5 and 6'])),
    'pits 7 and 8' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['pits 7 and 8'])),
    'pits 9 and 10' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['pits 9 and 10'])),
    'pits 11 and 12' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['pits 11 and 12'])),
    'Processed UAS data' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['Processed UAS data'])),
    'Drone2Map DSM Layer' : os.path.normpath(os.path.join(parent_dir, rel_dir_dic['Drone2Map DSM Layer']))
}


# coordinate system(s) dictionary
# For the scene coordinate systems there was not much info on which is idea but those selected seem to cover the areas and qualifications needed.

coor_dic = {
    'cs_' : 'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],VERTCS["WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PARAMETER["Vertical_Shift",0.0],PARAMETER["Direction",1.0],UNIT["Meter",1.0]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision', # Coordinate system for XYTable to points, or other coorinate based applications
    'main map xy' : '6343', #WKID for map XY projection, NAD 1983 (2011) UTM Zone 14N
    'main map z' : '5703', #WKID for map Z projection, NAVD88 height (m)
    'main scene xy' : '104602', #WKID for scene XY projection, NAD 1983 3D
    'main scene z' : '115807', #WKID for scene Z projection, Unkown height systems (meters) 
}


#endregion

#set map and scene as variables
print(dir_dic['project directory'])
project = ap.mp.ArcGISProject(dir_dic['project directory'])
maps = project.listMaps()
main_map = maps[0]
main_scene = maps[1]


#region - Pit Location import
# Import location data of pits from csv file, data in csv file was collected via handheld gps
pit_data = pd.read_csv(dir_dic['pit locations'])
# Adjust pit depths to convert from cm to m and from positive to negative to indicate depth under surface
pit_depth = (pit_data['Depth'] * -0.01)
pit_data['Depth'] = pit_depth
pit_data.to_csv(dir_dic['pit locations corrected'], index = False)

#endregion
#region - Point Layer and add to Map
# Create layer from csv

#To allow for multiple runs of this script
ap.env.overwriteOutput = True

ap.management.XYTableToPoint(
    in_table = dir_dic['pit locations corrected'],
    out_feature_class = dir_dic['pit locations layer'],
    x_field = 'lon',
    y_field = 'lat',
    z_field='Depth',
    coordinate_system = coor_dic['Points to Table']
)

#Add new point layer to Map and Scene
main_map.addDataFromPath(dir_dic['pit locations layer'])
main_scene.addDataFromPath(dir_dic['pit locations layer'])
print("Features added to maps")
#endregion

#region - create maps from UAS Data using ODM
# Due to the size of a single map this takes a long time to run and is run in a for loop to iterate through all UAS imagery

UAS_imagery = [
    dir_dic['pits 1 and 2'],
    dir_dic['pits 3 and 4'],
    dir_dic['pits 5 and 6'],
    dir_dic['pits 7 and 8'],
    dir_dic['pits 9 and 10'],
    dir_dic['pits 11 and 12'],
]
def build_project_maps(images):
    try:
        ODM.UAS_map_builder(images, dir_dic['Processed UAS data']).main()
        
        # Add UAS Maps to Proproject
        for image_set in images:
            dsm_path = os.path.normpath(os.path.join(parent_dir,f'/maps/processed_Maps/{os.path.basename(image_set)}/All_ODM_Files/odm_dem/dsm.tif'))
            ortho_path = os.path.normpath(os.path.join(parent_dir,f'/maps/processed_Maps/{os.path.basename(image_set)}/All_ODM_Files/odm_orthophoto/odm_orthophoto.tif'))
            main_map.addDataFromPath(dsm_path)
            main_map.addDataFromPath(ortho_path)
    except:
        print('Failure in ODM, some maps maybe be missing.')
        
build_project_maps(UAS_imagery)
#endregion

#region - Adding 3D Objects to Map and Scene
# Setting up dictionary of pit names in pit locations dataframe to reference later
pit_names = {
    'pit 1' : 'Kansas Soil  Juging Pit 1',
    'pit 2' : 'Kansas Soil Judging Pit 2',
    'pit 3' : 'Kansas Soil Judging Pit 3',
    'pit 4' : 'Kansas Soil Judging Pit 4',
    'pit 5' : 'Kansas Soil Judging Pit 5',
    'pit 6' : 'Kansas Soil Judging Pit 6',
    'pit 9' : 'Kansas Soil Judging Pit 9',
    'pit 11' : 'Kansas Soil Judging Pit 11',
    'pit 12' : 'Kansas Soil Judgig Pit 12'
}

# Adding 3D object (practice pit #5) to map

lon = pit_data.loc[pit_data['name'] == pit_names['pit 5'], 'lon']
lat = pit_data.loc[pit_data['name'] == pit_names['pit 5'], 'lat']
depth = pit_data.loc[pit_data['name'] == pit_names['pit 5'], 'Depth']

ap.management.Import3DObjects(
    files_and_folders = os.path.normpath(os.path.join(parent_dir,'pits\Kansas_Pit_5.glb')),
    updated_features = 'Kansas_Pit_5',
    update = 'UPDATE_EXISTING_ADD_NEW',
    translate = f'{lon}, {lat}',
    elevation = depth,
    scale = 1,
    rotate = 0, # this assumes the model wont need to be rotated to align with map
    y_is_up = 'Y_IS_UP'
)
#endregion

#region - Adding Drone2Map Files to map
#set up empty group layer
DSM_group_layer = ap.mp.LayerFile(dir_dic['Drone2Map DSM Layer'])
DSM_group = main_map.addLayer(DSM_group_layer)[0]

#Example Raster Layer Style:
for layer in main_map.listLayers():
    if layer.name == 'Drone_Images_5_6_dsm.tif':
        model_layer = layer

#List of pit folders
pit_maps = [folder for folder in os.listdir(os.path.dirname(dir_dic['Drone2Map DSM Layer'])) if os.path.isdir(os.path.join(os.path.dirname(dir_dic['Drone2Map DSM Layer']),folder))] # list of pit map sets

for pit_series in pit_maps:

    DSM_path = os.path.normpath(os.path.join(parent_dir, f'drone2map/{pit_series}/Products/2D/DEM/DSM/{pit_series}_dsm.tif'))
    print(DSM_path)
    main_map.addDataFromPath(DSM_path)
    new_raster = f'{pit_series}_dsm.tif'
    print(new_raster)
    for layer in main_map.listLayers():
        if layer.isRasterLayer and layer.name == new_raster:
            working_raster = layer
    
    # Set symbology to match the other DSM layers in map
    ap.management.ApplySymbologyFromLayer(
    in_layer=working_raster,
    in_symbology_layer=model_layer,
    symbology_fields="CHART_RENDERER_PIE_SIZE_FIELD # #;COLOR_EXPRESSION_FIELD # #;EXCLUSION_CLAUSE_FIELD # #;NORMALIZATION_FIELD # #;PRIMITIVE_OVERRIDE_EXPRESSION_FIELD # #;ROTATION_XEXPRESSION_FIELD # #;ROTATION_YEXPRESSION_FIELD # #;ROTATION_ZEXPRESSION_FIELD # #;SIZE_EXPRESSION_FIELD # #;TRANSPARENCY_EXPRESSION_FIELD # #;TRANSPARENCY_NORMALIZATION_FIELD # #;VALUE_FIELD # #",
    update_symbology="DEFAULT"
    )
    main_map.addLayerToGroup(DSM_group, working_raster)
    main_map.removeLayer(working_raster)
    project.save()
# List raster layers in the map
for layer in main_map.listLayers():
    if layer.isRasterLayer:
        print(f'Raster Layer: {layer}')
