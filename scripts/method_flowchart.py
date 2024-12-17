'''
email: ajcecil@iastate.edu
Date Created: 2024-15-12
Last Modified: 2024-15-12
Purpose: This script creates a flowchart for my final project poster for CRP 4560.
Requirements: tk_flow is needed, I wrote the tk_flow app for to create flowcharts and published it to PyPI, can be installed using pip install tk_flow.
'''


from tk_flow import Flowchart
import tkinter as tk

#region - Positioning and Grid formating
width = 425
height = width*0.6
node_width = 350
node_height = node_width*0.6
col_space = 1
row_space = 2
point_space = row_space/2
point_space_c = col_space/2
yes_label = point_space * (9/16)
no_label = point_space_c * 1.25

r0 = 1
r1 = r0 + row_space
r2 = r1 + row_space
r3 = r2 + row_space
r4 = r3 + row_space
r5 = r4 + row_space
r6 = r5 + row_space
r7 = r6 + row_space
r8 = r7 + row_space
r9 = r8 + row_space
r10 = r9 + row_space
r11 = r10 + row_space
r12 = r11 + row_space
r13 = r12 + row_space
r14 = r13 + row_space
r15 = r14 + row_space
r16 = r15 + row_space
r17 = r16 + row_space
r18 = r17 + row_space
r19 = r18 + row_space
r20 = r19 + row_space
r21 = r20 + row_space

r0a = r0 + point_space
r1a = r1 + point_space
r2a = r2 + point_space
r3a = r3 + point_space
r4a = r4 + point_space
r4b = r4 + point_space * 1.25
r5a = r5 + point_space
r5b = r5 + yes_label
r6a = r6 + point_space
r6b = r6 + yes_label
r7a = r7 + point_space
r7b = r7 + yes_label
r8a = r8 + point_space
r8b = r8 + yes_label
r8c = r8 + point_space * 1.25
r9a = r9 + point_space
r9b = r9 + yes_label
r10a = r10 + point_space
r10b = r10 + yes_label
r11a = r11 + point_space
r11b = r11 + point_space * 1.25
r11c = r11 + point_space * 1.5
r12a = r12 + point_space
r13a = r13 + point_space
r13b = r13+ yes_label
r14a = r14 + point_space
r14b = r14 + yes_label
r15a = r15 + point_space
r16a = r16 + point_space
r16b = r16 + yes_label
r17a = r17 + point_space
r17b = r17 + yes_label
r18a = r18 + point_space
r18b = r18 + yes_label
r19a = r19 + point_space
r19b = r19 + yes_label


c1 = 1
c2 = c1 + col_space
c3 = c2 + col_space
c4 = c3 + col_space
c5 = c4 + col_space
c6 = c5 + col_space
c7 = c6 + col_space
c8 = c7 + col_space
c9 = c8 + col_space


c1a = c1 + point_space_c
c2a = c2 + point_space_c
c3a = c3 + point_space_c
c3b = c3 + no_label
c4a = c4 + point_space_c
c4b = c4 + point_space_c * 1.25
c4c = c4 + point_space_c * 0.75
c5a = c5 + point_space_c
c5b = c5 + no_label
c5c = c5 + point_space_c * 1.5
c6a = c6 + point_space_c
c7a = c7 + point_space_c
c7b = c7 + point_space_c * 1.5
c8a = c8 + point_space_c
c9a = c9 + point_space_c


#endregion
#region - variable assignment
# Shape variables
terminal = "oval"
process = "rectangle"
decision = "diamond"
preparation = "hexagon"
special = "rectangle2"
p = "point"
label = "label"
title = "title"
start = "terminal_start"
end = "terminal_end"
a = "arrow"

# Colors and Formating
    # Custom color and outline scheme
color = {
    terminal: "#189a18",
    process : "#ffcc33",
    special : "#f47935",
    decision : "#f2debe",
    preparation : "#cb9353",
    start : "#189a18",
    end : "#a01313"
}

outline = {
    terminal : {"color": "black", "thickness":3},
    process : {"color": "black", "thickness": 3},
    special : {"color": "black", "thickness": 3},
    decision : {"color": "black", "thickness": 3},
    preparation : {"color": "black", "thickness": 3},
    start : {"color": "black", "thickness":3},
    end : {"color": "black", "thickness":3}
    
}

fonts = {
    "oval": {"font": "Courier", "size": 24, "color": "black", "weight": "normal", "underline" : False},
    "rectangle": {"font": "Times", "size": 36, "color": "black", "weight": "normal", "underline" : False},
    "rectangle2": {"font": "Courier", "size": 24, "color": "black", "weight": "bold", "underline" : False},
    "diamond": {"font": "Courier", "size": 24, "color": "black", "weight": "normal", "underline" : False},
    "hexagon": {"font": "Courier", "size": 24, "color": "black", "weight": "normal", "underline" : False},
    "label": {"font": "Courier", "size": 18, "color": "black", "weight": "bold", "underline" : False},
    "terminal_start": {"font": "Courier", "size": 36, "color": "black", "weight": "bold", "underline" : False},
    "terminal_end": {"font": "Courier", "size": 36, "color": "black", "weight": "bold", "underline" : False},
    "title": {"font": "Times", "size": 52, "color": "black", "weight": "bold", "underline" : False}
}

connector = {
    "color": "black",
    "thickness": 6
}

n, s, e, w, c = "n", "s", "e", "w", "c"

#endregion


#region Window Establishment
root = tk.Tk()

# Create Flowchart instance
f = Flowchart(
    root = root,
    grid_width=width,
    grid_height=height,
    fonts = fonts,
    colors=color,
    outlines=outline,
    connectors=connector,
    node_width = node_width,
    node_height = node_height 
    )

#endregion
#region - Title Node
title = f.node(c5, r0a, "UAS Images to ArcGIS Pro Map", title)

#endregion
#region - Flow
pit = f.node(c6, r1, "Scanned\nPits", process)
UAS_image = f.node(c5, r1, "Imagery\nfrom\nUAS", process)
ODM_function = f.node(c5, r2, "Open Drone\nMap (ODM)\nPython Tool", process)
f.connect(UAS_image, s, ODM_function, n, a)

ODM_to_processed_1 = f.node(c5, r2a )
f.connect(ODM_function, s, ODM_to_processed_1, c)
ODM_to_processed_2 = f.node(c4, r2a)
f.connect(ODM_to_processed_1, c, ODM_to_processed_2, c)
processed = f.node(c4, r3, "Processed\nImagery", process)
f.connect(ODM_to_processed_2, c, processed, n, a)


ODM_to_gcp = f.node(c6, r2a)
f.connect(ODM_to_processed_1, c, ODM_to_gcp, c)
gcp = f.node(c6, r3, "Ground\nControl\nPoints", process)
f.connect(ODM_to_gcp, c, gcp, n, a)


processed_to_pro = f.node(c4, r3a)
f.connect(processed, s, processed_to_pro, c)
arcGIS_Pro = f.node(c5, r4, "ArcGIS\nPro\nMap", process)
gcp_to_pro_1 = f.node(c6, r3a)
f.connect(gcp, s, gcp_to_pro_1, c)


f.connect(pit, s, gcp, n, a)
gcp_to_pro_2 = f.node(c5, r3a)
f.connect(processed_to_pro, c, gcp_to_pro_2, c)
f.connect(gcp_to_pro_1, c, gcp_to_pro_2, c)
f.connect(gcp_to_pro_2, c, arcGIS_Pro, n, a)


# setting corners for spacing of flowchart
corner_1 = f.node(c3, r0)
corner_2 = f.node(c3, r5)
corner_3 = f.node(c7, r5)
corner_4 = f.node(c7, r0)

root.mainloop()