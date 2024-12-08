# CircuitSolver

This README provides an overview of the **CircuitSolver** project, including installation instructions, usage examples, and contribution guidelines.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview
**CircuitSolver** is a Python-based tool for solving electrical circuits using **Modified Nodal Analysis (MNA)**. The program reads circuit definitions from a file, constructs the MNA matrix, and computes node voltages.

## Features
- **Reads Circuit Definitions**: Supports resistors, current sources, and voltage sources.
- **MNA Matrix Construction**: Automatically builds the Modified Nodal Analysis matrix from the circuit data.
- **Voltage Calculation**: Solves for node voltages in the circuit using NumPy's linear algebra capabilities.
- **Ground Node Handling**: Automatically accounts for a designated ground node.

## Installation
To run CircuitSolver, ensure you have **Python 3** installed along with the necessary dependencies. Follow these steps to set up the project:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/CircuitSolver.git
   cd CircuitSolver
