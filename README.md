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

## Step 4 - Adding drain hole in STL files:

Install meshlab on Ubuntu with

```
sudo apt-get install meshlab
```

Open the STL file in meshlab, click the "Select Faces in a rectangular region".

Hold 'alt' to select only visible region and add a small hole on the surface(preferrably on the bottom). Once your desired region is selected, press "delete".

This is so that the resin has a way to drain for hollow models. Without a hole for draining resin, software on the printer builds a solid model instead of a hollow one 
