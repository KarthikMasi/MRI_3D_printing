import vtk
import argparse

def add_hole_to_vtk_model(input_file, output_file, hole_radius):
    # Read the VTK model
    reader = vtk.vtkPolyDataReader()
    reader.SetFileName(input_file)
    reader.Update()
    vtk_model = reader.GetOutput()

    # Compute the bounds of the VTK model
    bounds = vtk_model.GetBounds()
    min_z = bounds[4]

    # Set the hole center at the bottom of the model
    hole_center = [0.0, 0.0, min_z]

    # Create a cylinder representing the hole
    cylinder = vtk.vtkCylinder()
    cylinder.SetCenter(hole_center[0], hole_center[1], hole_center[2] - hole_radius)
    cylinder.SetRadius(hole_radius)
    cylinder.SetAxis(0.0, 0.0, 1.0)

    # Create a boolean operation to remove the bottom surface from the hole cylinder
    boolean_operation = vtk.vtkBooleanOperationPolyDataFilter()
    boolean_operation.SetOperationToDifference()
    boolean_operation.SetInputData(0, vtk_model)
    boolean_operation.SetInputConnection(1, cylinder.GetOutputPort())
    boolean_operation.Update()
    modified_model = boolean_operation.GetOutput()

    # Write the modified VTK model to a file
    writer = vtk.vtkPolyDataWriter()
    writer.SetFileName(output_file)
    writer.SetInputData(modified_model)
    writer.Write()

    print("Hole added to the bottom of the VTK model.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a hole to a VTK model at the bottom.")
    parser.add_argument("input_file", help="Input VTK model file")
    parser.add_argument("output_file", help="Output VTK model file")
    parser.add_argument("hole_radius", type=float, help="Hole radius")
    args = parser.parse_args()

    add_hole_to_vtk_model(args.input_file, args.output_file, args.hole_radius)

