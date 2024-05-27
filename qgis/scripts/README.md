# QGIS Python scripts used in the automation

This repository contains Python scripts for use in QGIS. Follow the instructions below to add and use these scripts in QGIS.

## Adding Python scripts to QGIS using the GUI

### Step 1: Open the QGIS Processing Toolbox
1. Open the QGIS Processing Toolbox by going to `Processing > Toolbox` on the menu bar or clicking `CTRL+ALT+T`.

### Step 2: Add the script
1. On the toolbox menu bar, click on the Python icon and select `Add Script to Toolbox...`
2. This will open a file dialog.
3. Browse the file dialog and select the script you want to add.
4. This script will now be added to the Processing toolbox of the currently active User Profile.
5. NOTE: If you want the script to be available to other User Profiles, you need to add it to them too.

### Step 3: Use the Script in the QGIS Processing Toolbox

1. In the Processing Toolbox, expand the `Scripts` group.
2. Find the script you added. It will be listed under the group based on its metadata or filename. In this case, the scripts should be under a `YJP_Attribution` group.
3. Double-click the script to open the script dialog.
4. Fill in the required parameters and run the script.

### Optional step: Editing the script

1. On the Processing Toolbox, right click on the script and click `Edit Script` to open the script in the QGIS Python editor.
2. Similarly, you can also directly edit the script in any text or code editor of your choice.


## IMPORTANT
Scripts and models that are added to the Processing Toolbox become part of the QGIS Processing Framework and can be used in other models and scripts. They can also be batch processed.