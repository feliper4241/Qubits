from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Função para criar o circuito de verificação de paridade
def parity_checker(input_bits):
    n = len(input_bits)
    qc = QuantumCircuit(n + 1, 1)

    # Preparar os qubits de entrada
    for i, bit in enumerate(input_bits):
        if bit == '1':
            qc.x(i)  # Aplica X se o bit for 1

    # Porta CNOT entre cada bit e o último qubit (parity)
    for i in range(n):
        qc.cx(i, n)

    # Medida do qubit de paridade
    qc.measure(n, 0)

    # Execução do circuito
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend=simulator, shots=1024).result()
    counts = result.get_counts()

    print("Paridade (0 = par, 1 = ímpar):", counts)
    plot_histogram(counts)
    plt.show()

# Exemplo de uso:
parity_checker("1101")
