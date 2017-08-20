# ---------------------------------------------------------------------------
# build_b1_ne_50m_admin_0_subunits.py
# Created on: Sat Aug 19 2017 11:46:19 PM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Set the necessary product code
gp.SetProduct("ArcInfo")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")


# Local variables...
ne_50m_admin_0_map_subunits_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_map_subunits.shp"
ne_10m_admin_0_map_subunits_test_shp__2_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_map_subunits.shp"
ne_10m_admin_0_map_subunits_test_shp__3_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_map_subunits.shp"
ne_10m_admin_0_map_subunits_test_shp__4_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_map_subunits.shp"
ne_10m_admin_0_map_subunits_test_shp__5_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_map_subunits.shp"
ne_10m_admin_0_map_subunits_test_shp__6_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_map_subunits.shp"
ne_10m_admin_0_map_subunits_test_shp__7_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_map_subunits.shp"
ne_admin_0_details_level_4_subunits_dbf = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\housekeeping\\ne_admin_0_details_level_4_subunits.dbf"
ne_50m_admin_0_scale_rank_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_scale_rank.shp"
Output_Feature_Class = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_map_subunits.shp"
ne_10m_admin_0_map_subunits_shp__2_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_map_subunits.shp"

# Process: Dissolve...
gp.Dissolve_management(ne_50m_admin_0_scale_rank_shp, ne_50m_admin_0_map_subunits_shp, "sr_su_a3", "scalerank MIN", "MULTI_PART", "DISSOLVE_LINES")

# Process: Add Field (2)...
gp.AddField_management(ne_50m_admin_0_map_subunits_shp, "scalerank", "SHORT", "", "", "", "", "NON_NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field...
gp.CalculateField_management(ne_10m_admin_0_map_subunits_test_shp__4_, "scalerank", "[MIN_scaler]", "VB", "")

# Process: Add Field...
gp.AddField_management(ne_10m_admin_0_map_subunits_test_shp__5_, "featurecla", "TEXT", "", "", "30", "", "NON_NULLABLE", "NON_REQUIRED", "")

# Process: Calculate Field (2)...
gp.CalculateField_management(ne_10m_admin_0_map_subunits_test_shp__3_, "featurecla", "\"Admin-0 map subunit\"", "VB", "")

# Process: Delete Field...
gp.DeleteField_management(ne_10m_admin_0_map_subunits_test_shp__6_, "MIN_scaler")

# Process: Repair Geometry...
gp.RepairGeometry_management(ne_10m_admin_0_map_subunits_test_shp__7_, "DELETE_NULL")

# Process: Join Field...
gp.JoinField_management(Output_Feature_Class, "sr_su_a3", ne_admin_0_details_level_4_subunits_dbf, "SU_A3", "")

# Process: Delete Field (2)...
gp.DeleteField_management(ne_10m_admin_0_map_subunits_test_shp__2_, "sr_su_a3;MIN_scaler")

