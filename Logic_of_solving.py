import numpy as np

class CircuitSolver:
    def __init__(self, filename):
        self.filename = filename
        self.nodes = set()
        self.resistors = []
        self.current_sources = []
        self.voltage_sources = []
        self.ground_node = 0


    def read_file(self):
        with open(self.filename, 'r') as file:
            for line in file:
                parts = line.split()
                if parts[0] == 'r':
                    node1, node2, value = int(parts[1]), int(parts[2]), float(parts[3])
                    self.resistors.append((node1, node2, value))
                    self.nodes.update([node1, node2])
                elif parts[0] == 'i':
                    node1, node2, value = int(parts[1]), int(parts[2]), float(parts[3])
                    self.current_sources.append((node1, node2, value))
                    self.nodes.update([node1, node2])
                elif parts[0] == 'v':
                    node1, node2, value = int(parts[1]), int(parts[2]), float(parts[3])
                    self.voltage_sources.append((node1, node2, value))
                    self.nodes.update([node1, node2])
        
        if self.ground_node in self.nodes:
            self.nodes.remove(self.ground_node)
        self.nodes = sorted(list(self.nodes))

    def build_mna_matrix(self):
        num_nodes = len(self.nodes)
        num_voltage_sources = len(self.voltage_sources)
        A = np.zeros((num_nodes + num_voltage_sources, num_nodes + num_voltage_sources))
        B = np.zeros(num_nodes + num_voltage_sources)
        node_index = {node: idx for idx, node in enumerate(self.nodes)}

        # Add resistors to the MNA matrix
        for node1, node2, resistance in self.resistors:
            G = 1 / resistance
            i1 = node_index.get(node1, None)
            i2 = node_index.get(node2, None)
            if i1 is not None:
                A[i1, i1] += G
            if i2 is not None:
                A[i2, i2] += G
            if i1 is not None and i2 is not None:
                A[i1, i2] -= G
                A[i2, i1] -= G

        # Add current sources to the MNA matrix
        for node1, node2, current in self.current_sources:
            if node1 != self.ground_node:
                B[node_index[node1]] -= current
            if node2 != self.ground_node:
                B[node_index[node2]] += current

        # Add voltage sources to the MNA matrix
        for idx, (node1, node2, voltage) in enumerate(self.voltage_sources):
            supernode_idx = num_nodes + idx
            if node1 != self.ground_node:
                A[node_index[node1], supernode_idx] = 1
                A[supernode_idx, node_index[node1]] = 1
            if node2 != self.ground_node:
                A[node_index[node2], supernode_idx] = -1
                A[supernode_idx, node_index[node2]] = -1
            B[supernode_idx] = voltage

        return A, B

    def solve(self):
        A, B = self.build_mna_matrix()
        print("MNA Matrix (A):")
        print(A)
        print("Right-hand side (B):")
        print(B)
        try:
            solution = np.linalg.solve(A, B)
            return solution
        except np.linalg.LinAlgError as e:
            print(f"Error solving the system: {e}")
            return None

def main():
    filename = 'datafile.txt'
    solver = CircuitSolver(filename)
    solver.read_file()
    solution = solver.solve()

    if solution is not None:
        print("Node Voltages:")
        for i, node in enumerate(solver.nodes):
            print(f"V({node}) = {solution[i]} V")

if __name__ == "__main__":
    main()
