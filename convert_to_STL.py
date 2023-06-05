import vtk
import argparse

def convert_vtk_to_stl(input_file, output_file):
    # Read the VTK file
    reader = vtk.vtkDataSetReader()
    reader.SetFileName(input_file)
    reader.Update()

    # Convert the dataset to polydata
    geometry_filter = vtk.vtkGeometryFilter()
    geometry_filter.SetInputConnection(reader.GetOutputPort())
    geometry_filter.Update()

    # Write the polydata as an STL file
    stl_writer = vtk.vtkSTLWriter()
    stl_writer.SetFileName(output_file)
    stl_writer.SetInputConnection(geometry_filter.GetOutputPort())
    stl_writer.Write()

    print("Conversion complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert VTK file to STL format.")
    parser.add_argument("input_file", help="Input VTK file")
    parser.add_argument("output_file", help="Output STL file")
    args = parser.parse_args()

    convert_vtk_to_stl(args.input_file, args.output_file)

