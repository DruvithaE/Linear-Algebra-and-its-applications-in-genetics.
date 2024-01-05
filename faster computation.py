import numpy as np

def calculate_pqr(p0, q0, r0, n):
    pn = 1 - (1/2)**n * q0 - (1/2)**(n-1) * r0
    qn = (1/2)**n * q0 + (1/2)**(n-1) * r0
    rn = 0
    return pn, qn, rn

def calculate_Xn(p0, q0, r0, n):
    P = np.array([[1, 1/2, 0], [0, 1/2, 1], [0, 0, 0]])
    X0 = np.array([p0, q0, r0])

    C = np.array([[1, 1, 1/2], [0, -1, -1], [0, 0, 1/2]])
    D = np.array([[1, 0, 0], [0, 1/2, 0], [0, 0, 0]])
    
    C_inv = np.linalg.inv(C)
    Pn = C @ np.linalg.matrix_power(D, n) @ C_inv
    
    Xn = Pn @ X0
    return Xn

# Example usage
p0 = 0.5
q0 = 0.3
r0 = 0.2
n = 3

p, q, r = calculate_pqr(p0, q0, r0, n)
print(f"p_n: {p}")
print(f"q_n: {q}")
print(f"r_n: {r}")

X = calculate_Xn(p0, q0, r0, n)
print(f"X^(n): {X}")