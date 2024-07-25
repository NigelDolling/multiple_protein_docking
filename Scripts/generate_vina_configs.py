"""
generate_vina_configs.py

This script generates configuration files for AutoDock Vina docking by reading receptor 
names and their corresponding centers of mass from a text file, and iterating over 
each ligand file in a specified folder.

Last Updated: Monday 25th July, 2024 | 4:47 PM

Prepared by: Nigel Dolling @ NMIMR
"""

import os
import re

# Define the path to the folder containing receptor files and the file with centers of mass
receptor_folder = "/mnt/lustre/users/fagamah/nigel/art_docking_4/Target"
center_of_mass_file = "centre_of_mass.txt"

def read_centers_of_mass(file_path):
    """
    Reads the file containing receptor names and centers of mass.

    Parameters:
        file_path (str): Path to the file containing centers of mass.

    Returns:
        dict: A dictionary with receptor names as keys and center of mass coordinates as values.
    """
    try:
        with open(file_path, 'r') as f:
            receptor_centers = f.readlines()
    except FileNotFoundError:
        print(f"Error: {center_of_mass_file} not found in {receptor_folder}")
        exit(1)

    receptor_dict = {}
    for line in receptor_centers:
        match = re.match(r"(.+):\s+\[(.+)\]", line)
        if match:
            receptor_name = match.group(1)
            center_of_mass = match.group(2)
            receptor_dict[receptor_name] = center_of_mass.split()
        else:
            print(f"Warning: Line '{line.strip()}' is not in the expected format")
    return receptor_dict

def list_ligand_files(folder_path):
    """
    Lists all ligand files in the specified folder.

    Parameters:
        folder_path (str): Path to the folder containing ligand files.

    Returns:
        list: A list of ligand file names.
    """
    try:
        ligand_files = os.listdir(folder_path)
    except FileNotFoundError:
        print(f"Error: Ligand folder {folder_path} not found")
        exit(1)
    return [f for f in ligand_files if f.endswith(".pdbqt")]

def generate_vina_configs(receptor_dict, ligand_files, receptor_folder, ligand_folder):
    """
    Generates Vina configuration files for each receptor and ligand combination.

    Parameters:
        receptor_dict (dict): Dictionary with receptor names and center of mass coordinates.
        ligand_files (list): List of ligand file names.
        receptor_folder (str): Path to the folder containing receptor files.
        ligand_folder (str): Path to the folder containing ligand files.
    """
    for ligand in ligand_files:
        ligand_name = ligand[:-6]
        for receptor, center in receptor_dict.items():
            if len(center) != 3:
                print(f"Warning: Center of mass for receptor '{receptor}' is not a valid 3D coordinate")
                continue

            vina_name = f"{receptor}_{ligand_name}.vina"
            try:
                with open(f"/mnt/lustre/users/fagamah/nigel/art_docking_3/Vina/{vina_name}", "w") as vw:
                    vw.write(f"receptor={os.path.join(receptor_folder, receptor)}.pdbqt\n")
                    vw.write(f"ligand=/mnt/lustre/users/fagamah/nigel/art_docking_3/Ligand/{ligand_name}.pdbqt\n")
                    vw.write(f"out=/mnt/lustre/users/fagamah/nigel/art_docking_3/Out/{vina_name}all.pdbqt\n")
                    vw.write(f"log=/mnt/lustre/users/fagamah/nigel/art_docking_3/Log/{vina_name}all.log\n")
                    vw.write(f"center_x={center[0]}\n")
                    vw.write(f"center_y={center[1]}\n")
                    vw.write(f"center_z={center[2]}\n")
                    vw.write("size_x=100\n")
                    vw.write("size_y=100\n")
                    vw.write("size_z=100\n")
                    vw.write("energy_range=4\n")
                    vw.write("cpu=8\n")
                    vw.write("exhaustiveness=320\n")
            except IOError:
                print(f"Error: Could not write to file {vina_name}")

if __name__ == "__main__":
    receptor_dict = read_centers_of_mass(os.path.join(receptor_folder, center_of_mass_file))
    ligand_files = list_ligand_files('../Ligand')
    generate_vina_configs(receptor_dict, ligand_files, receptor_folder, '../Ligand')
