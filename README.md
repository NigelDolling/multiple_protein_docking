# Multiple Protein Docking with a Single Ligand

This repository provides a comprehensive guide and scripts to perform multiple protein docking with a single ligand on an HPC cluster. The aim is to help researchers and students understand and execute the process efficiently.

## Table of Contents

1. [Introduction](#introduction)
2. [Folder Structure](#folder-structure)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## Introduction

In computational biology, docking studies help predict the interaction between a ligand and a protein. This project automates the process of docking a single ligand with multiple protein targets using AutoDock Vina and an HPC cluster.

## Folder Structure

- **Generate_job**: Scripts to generate job files for the HPC cluster.
- **Ligand**: Contains ligand files for docking.
- **Log**: Directory for log files generated during docking.
- **Out**: Output directory for docking results.
- **Scripts**: Helper scripts for various tasks.
- **Submit_job**: Scripts to submit jobs to the HPC cluster.
- **Target**: Contains protein target files.
- **Vina**: Configuration files and executables for AutoDock Vina.

## Requirements

- Python 3.5 or higher
- AutoDock Vina
- HPC cluster access
- Git


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/multiple_protein_docking.git
   cd multiple_protein_docking

## Usage
1. Prepare the ligand and protein target files:

i. Place ligand files in the Ligand directory.
ii. Place protein target files in the Target directory.

2. Generate the centre of masses for proteins:
   ```bash
   python com_calculator.py
   
3. Generate job files:

   ```bash
   python Generate_job/generate_jobs.py

4. Submit jobs to the HPC cluster:

   ```bash
   qsub Submit_job/submit_jobs.sh

5. Monitor log files and retrieve results:

Logs will be available in the Log directory.
Results will be stored in the Out directory.

## Contributing
Contributions are welcome! Please read the CONTRIBUTING.md file for guidelines on how to contribute to this project.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For any questions or suggestions, please open an issue or contact ndolling5@gmail.com
