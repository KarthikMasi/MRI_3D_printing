import vtk
import argparse

def concatenate_vtk_files(input_file1, input_file2, output_file):
    # Read the first VTK file
    reader1 = vtk.vtkDataSetReader()
    reader1.SetFileName(input_file1)
    reader1.Update()
    data1 = reader1.GetOutput()

    # Read the second VTK file
    reader2 = vtk.vtkDataSetReader()
    reader2.SetFileName(input_file2)
    reader2.Update()
    data2 = reader2.GetOutput()

    # Combine the datasets along the X-axis
    append_filter = vtk.vtkAppendPolyData()
    append_filter.AddInputData(data1)
    append_filter.AddInputData(data2)
    append_filter.Update()
    combined_data = append_filter.GetOutput()

    # Write the combined dataset to a VTK file
    writer = vtk.vtkDataSetWriter()
    writer.SetFileName(output_file)
    writer.SetInputData(combined_data)
    writer.Write()

    print("Concatenation complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Concatenate two VTK files.")
    parser.add_argument("input_file1", help="First input VTK file")
    parser.add_argument("input_file2", help="Second input VTK file")
    parser.add_argument("output_file", help="Output VTK file")
    args = parser.parse_args()

    concatenate_vtk_files(args.input_file1, args.input_file2, args.output_file)

