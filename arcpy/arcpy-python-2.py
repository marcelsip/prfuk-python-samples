# Skript pro vypis trid prvku a rastru z adresare
#------------------------------------------------

import arcpy
arcpy.env.workspace = "C:/Data/ArcCR3"
workspaces = arcpy.ListWorkspaces("*", "All")

for workspace in workspaces: 
	arcpy.env.workspace = workspace
	print "--------------------"
	print workspace
	print "--------------------"

	print "Tridy prvku:"
	fcs = arcpy.ListFeatureClasses("*","All")
	for fc in fcs:
		print fc

	print "Rastry:"
	rasters = arcpy.ListRasters("*","All")
	for raster in rasters:
		print raster
