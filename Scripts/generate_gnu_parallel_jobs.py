"""
generate_gnu_parallel_jobs.py

This script generates a GNU parallel jobs file by listing all Vina configuration 
files in a specified directory and writing commands to execute Vina with these 
configuration files to the jobs file.

Last Updated: Monday 25th July, 2024 | 4:57 PM

Prepared by: Nigel Dolling @ NMIMR
"""

import os

def list_vina_files(folder_path):
    """
    Lists all Vina configuration files in the specified folder.

    Parameters:
        folder_path (str): Path to the folder containing Vina configuration files.

    Returns:
        list: A list of Vina configuration file names.
    """
    try:
        vina_files = os.listdir(folder_path)
    except FileNotFoundError:
        print(f"Error: Vina folder {folder_path} not found")
        exit(1)
    return vina_files

def generate_gnu_parallel_jobs(vina_files, output_file):
    """
    Generates a GNU parallel jobs file for running Vina with the configuration files.

    Parameters:
        vina_files (list): List of Vina configuration file names.
        output_file (str): Path to the output GNU parallel jobs file.
    """
    try:
        with open(output_file, "w") as gnu_w:
            for vina in vina_files:
                command = f"/path/to/your/Submit_job/vina --config /path/to/your/Vina/{vina}\n\n"
                gnu_w.write(command)
    except IOError:
        print(f"Error: Could not write to file {output_file}")

if __name__ == "__main__":
    vina_folder = '../Vina'
    output_file = "gnu_parallel.jobs"
    vina_files = list_vina_files(vina_folder)
    generate_gnu_parallel_jobs(vina_files, output_file)
