# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# clip.py
# Created on: 2017-10-19 14:17:59.00000
#   (generated by ArcGIS/ModelBuilder)
# Description:
# ---------------------------------------------------------------------------


...# input data is in NAD 1983 UTM Zone 11N coordinate system
input_features = r"C:/data/Redlands.shp"

# output data
output_feature_class = r"C:/data/Redlands_Project.shp"

# create a spatial reference object for the output coordinate system
out_coordinate_system = arcpy.SpatialReference('Transverse_Mercator')

# run the tool
arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)





>>> import os
... import glob
... from arcpy import env
... env.workspace = "G:/7gaodetraffic/2clip/"
... # Open one of the files,
... folder_path = 'G:/7gaodetraffic/2clip/'
... road= glob.glob(r'G:/7gaodetraffic/2clip/*.shp')
... i=1
... for i in range(0,200):
...     input_features = road[i]
...     output_features = "G:/7gaodetraffic/3project/"+ os.path.basename(road[i])
...     # create a spatial reference object for the output coordinate system
...     out_coordinate_system = arcpy.SpatialReference('WGS_1984_UTM_Zone_50N')
...     # run the tool
...     arcpy.Project_management(input_features, output_features, out_coordinate_system)
...     print output_features
...