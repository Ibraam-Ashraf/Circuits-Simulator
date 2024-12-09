# Circuit Solver

## Overview

This project is a Python-based **Circuit Solver** that analyzes electrical circuits using **Modified Nodal Analysis (MNA)**. It reads a circuit description from a file, builds the MNA matrix, and computes the node voltages and branch currents in the circuit.

---

## Features

- Reads circuit data from a text file.
- Supports resistors, voltage sources, and current sources.
- Constructs the Modified Nodal Analysis (MNA) matrix.
- Solves the circuit equations using `numpy.linalg.solve`.
- Outputs node voltages and matrix details.

---

## Requirements

- Python 3.6+
- `numpy` library

Install the required dependency using:
```bash
pip install numpy
