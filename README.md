# 3D_printing from MRI: A Guide

This guide will walk you through the process of transforming surface files from Freesurfer into the 'STL' format, suitable for 3D printing.

## Step 1 - Transform into VTK format:

Begin by installing Freesurfer, and then utilizing its command-line tool, "mris_convert".

For instance, if you wish to use the left and right pial files from Freesurfer, execute these commands:

```
mris_convert lh.pial lh.pial.vtk
mris_convert rh.pial rh.pial.vtk
```

## Step 2 - Merge the Left and Right Hemisphere

You'll need to have a Python environment equipped with vtk. Install it using pip: pip install vtk.

Then, use the following command to combine the VTK files for the left and right hemispheres:

```
python combine_vtk.py lh.pial.vtk rh.pial.vtk brain.pial.vtk
```

## Step 3 - Transform VTK into STL Format:

Finally, convert the merged VTK file into the STL format by running this command:

```
python convert_to_STL.py brain.pial.vtk brain.pial.stl
```
Once you've completed these steps, your file should be ready for 3D printing.


## To add information about the 2 printers sent my Abbie Weeks and also all the training material that will be received for the same
