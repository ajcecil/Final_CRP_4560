## Scripts Folder
This folder contains  all of the python scripts written for or used in this project.
### 3D_object.py
This is the main script for this project. This script calls on other scripts in the directory as well as other documents and directories in order to place layers within the ArcGIS Pro project.

#### 3D_Object.py Script Usage
This script should be ready to use once all data is downlaoded as listed structured in.

3D_Objects.py calls all of its own functions and imports the necessary packages and functions to run anything it contains. It was built to be run without openening the arcGIS Pro project and should place layers and adjust their symbology so when the project is opened the layers are in the top level map.

### ODM.py
ODM.py requires nodeODM installed instructions for which can be found at https://docs.opendronemap.org/installation/
ODM.py also requires the installation of [pyodm](https://pyodm.readthedocs.io/en/latest/)


The OpenDroneMap (ODM) script was written after looking into the process of generating maps with pyodm, the library released by ODM, due to the need for multiple processes to occur when using pyodm it seemed easier to build functions to complete some of the complex tasks as a default. The primary benefit of this App is the defualt function in ODM.main() being to loop through a list of folders, this function has no minimum so running it with one folder will not effect the results. A second benefit of the ODM App is the automation of starting and stopping of a docker container on the machine. To run the docker container all that is needed from the user is opening docker desktop and inputing their docker information in ODM


### tk_flow.py
#### this script can be found in its most up to date version at: https://github.com/ajcecil/tk_flow
This script was produced to generate flowcharts, originally inspired by the flowcharts needed for CRP 4570/5570, Geogames for Civic engagement. The other flowchart tools did not have the features which could optimize production and formating changes to quickly alter format of the entire document. This script was also useful for the production of the flowchart for the poster.

#### method_flowchart.py
This script uses tk_flow to produce the flowchart
