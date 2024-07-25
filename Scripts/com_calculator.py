"""
Calculate Center of Mass for PDB Files

This script calculates the center of mass for each PDB file in a specified directory
and writes the results to an output file.

Prepared by: Nigel Dolling @ NMIMR
Last Updated: Monday 25th July, 2024 | 4:42 PM
"""

import os
from Bio.PDB import PDBParser, Selection
import numpy as np

# Path for PDB files
PDB_FILES_DIRECTORY = '/path/to/your/Target'

# Output file for center of mass information
OUTPUT_FILE_PATH = '/path/to/your/Target/centre_of_mass.txt'  # Replace with the desired output file path

def calculate_center_of_mass(atom_list):
    """
    Calculate the center of mass of a list of atoms.

    Parameters:
    atom_list (list): List of atoms.

    Returns:
    np.ndarray: Center of mass coordinates.
    """
    total_mass = sum(atom.mass for atom in atom_list)
    center = np.array([0.0, 0.0, 0.0])
    for atom in atom_list:
        center += atom.mass * atom.get_coord()
    return center / total_mass

def main():
    """
    Main function to calculate the center of mass for each PDB file
    in the specified directory and write the results to an output file.
    """
    pdb_files = os.listdir(PDB_FILES_DIRECTORY)
    with open(OUTPUT_FILE_PATH, 'w') as output_file:
        for pdb_file in pdb_files:
            # Create the full path to the PDB file
            full_path = os.path.join(PDB_FILES_DIRECTORY, pdb_file)

            # Parse the PDB file
            pdb_parser = PDBParser()
            structure = pdb_parser.get_structure('protein', full_path)

            # Calculate the center of mass for the entire structure
            all_atoms = Selection.unfold_entities(structure, 'A')
            center_of_mass = calculate_center_of_mass(all_atoms)

            # Write center of mass information to the output file
            output_file.write(f"Center of Mass for {pdb_file}: {center_of_mass}\n")

    print(f"Center of mass information written to: {OUTPUT_FILE_PATH}")

if __name__ == "__main__":
    main()
