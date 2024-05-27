# QGIS Models used in the automation

This repository contains QGIS models that will be used in the automation. Follow the instructions below to add and use these models in QGIS.

## Adding models to QGIS using the GUI

### Step 1: Open the QGIS Processing Toolbox
1. Open the QGIS Processing Toolbox by going to `Processing > Toolbox` on the menu bar or clicking `CTRL+ALT+T`.

### Step 2: Add the model
1. On the toolbox menu bar, click on the Model icon (first icon that has 3 gears) and select `Add Model to Toolbox...`
2. This will open a file dialog.
3. Browse the file dialog and select the model you want to add.
4. This model will now be added to the Processing toolbox of the currently active User Profile.
5. NOTE: If you want the model to be available to other User Profiles, you need to add it to them too.

### Step 3: Use the Model in the QGIS Processing Toolbox

1. In the Processing Toolbox, expand the `Models` group.
2. Find the model you added. It will be listed under the group based on its metadata or filename. In this case, the models should be under a `YJP_Attribution` group.
3. Double-click the model to open the model dialog.
4. Fill in the required parameters and run the model.

### Optional step: Editing the model

1. On the Processing Toolbox, right click on the model and click `Edit Model` to open the QGIS Model Designer.


## IMPORTANT
Scripts and models that are added to the Processing Toolbox become part of the QGIS Processing Framework and can be used in other models and scripts. They can also be batch processed.