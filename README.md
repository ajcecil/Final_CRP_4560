# Project Directory Overview
## [Accessing data sets in this repo](documentation/DATA.md)


## [Accessing Drone2Map data layers in this repo](documentation/DRONE2MAP.md)



## [Accessing Images in this repo](documentation/IMAGES.md)

### Test Images Folder (test_images)
This folder contains a subset of the images for pits 1 and 2 to be used when testing the script, either during the writing process or later when creating the map may not be the most important thing to do.

Containg only 48 images this folder is able to run through the OpenDroneMaps tools within 5-10 minutes as opposed to the complete image sets which can take an hour or more to process in OpenDroneMaps


## Pits Folder (pits)
This folder contains the 3D scans of pits as '.glb' files, due to the number of polygons in each 3D object not all pits that were scanned are included in this folder. The pits included in this folder have been edited with a 3D editing software to limit the model to the pit area, some pits only had the pit face scanned, not all models have the same amount of detail or surface area captured.

While ArcGIS pro has multiple 3D object formats which can be imported '.glb' 3D objects have a file structure which is able to display both the surface/shape data and the material and shading data allowing for a much lighterweight process to introduce 3D objects into ArcGIS.


## ArcGIS Pro Project Folder (pro_project)
#### Folder too large for github, can be found on boxdrive folder: https://iastate.app.box.com/folder/298784822202
This folder contains the arcgis pro project used in any of the scripts and is where the different layers are set up to be displayed.

## Scripts Folder (scripts)
This folder contains  all of the python scripts written for or used in this project.
### 3D_object.py
This is the main script for this project. This script calls on other scripts in the directory as well as other documents and directories in order to place layers within the ArcGIS Pro project.

#### 3D_Object.py Script Usage


### ODM.py
The OpenDroneMap (ODM) script was written after looking into the process of generating maps with pyodm, the library released by ODM, due to the need for multiple processes to occur when using pyodm it seemed easier to build functions to complete some of the complex tasks as a default. The primary benefit of this App is the defualt function in ODM.main() being to loop through a list of folders, this function has no minimum so running it with one folder will not effect the results. A second benefit of the ODM App is the automation of starting and stopping of a docker container on the machine. To run the docker container all that is needed from the user is opening docker desktop and inputing their docker information in ODM


### tk_flow.py
#### this script can be found in its most up to date version at: https://github.com/ajcecil/tk_flow
This script was produced to generate flowcharts, originally inspired by the flowcharts needed for CRP 4570/5570, Geogames for Civic engagement. The other flowchart tools did not have the features which could optimize production and formating changes to quickly alter format of the entire document. This script was also useful for the production of the flowchart for the poster.

#### method_flowchart.py
This script uses tk_flow to produce the flowchart

## Other Folder (z_other)
This folder contains any other files relavent to this project which do not fit into any of the alternative folder categories.
