import numpy as np
import matplotlib.pyplot as plt


def plot(val, name, x_label, y_label, file):
    plt.figure(figsize=(16, 9))
    plt.plot(val)
    plt.title(name)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(f"{file}.png")
    plt.show()


psi = np.fromfile('wf.dat', dtype=np.cdouble)
print(psi)

NX, NY, NZ = 128, 128, 128
dx, dy, dz = 1, 1, 1

Psi_x, Psi_y, Psi_z = [], [], []

Psi_norm_x, Psi_norm_y, Psi_norm_z, Psi_pow_x, Psi_pow_y, Psi_pow_z = [], [], [], [], [], []

for ix in range(NX):
    Psi_x.append(psi[int( (NZ/2)*dz + NZ*(NY/2)*dy + NZ*NY*ix )])
    Psi_y.append(psi[int( (NZ/2)*dz + NZ*ix + NZ*NY*(NX/2)*dx )])
    Psi_z.append(psi[int( ix + NZ*(NY/2)*dy + NZ*NY*(NX/2)*dx )])

    Psi_norm_x.append(np.sqrt(np.power(np.real(Psi_x[ix]), 2) + np.power(np.imag(Psi_x[ix]), 2)))
    Psi_norm_y.append(np.sqrt(np.power(np.real(Psi_y[ix]), 2) + np.power(np.imag(Psi_y[ix]), 2)))
    Psi_norm_z.append(np.sqrt(np.power(np.real(Psi_z[ix]), 2) + np.power(np.imag(Psi_z[ix]), 2)))

    Psi_pow_x.append(np.power(np.real(Psi_x[ix]), 2) + np.power(np.imag(Psi_x[ix]), 2))
    Psi_pow_y.append(np.power(np.real(Psi_y[ix]), 2) + np.power(np.imag(Psi_y[ix]), 2))
    Psi_pow_z.append(np.power(np.real(Psi_z[ix]), 2) + np.power(np.imag(Psi_z[ix]), 2))

plot(Psi_norm_x, "|psi|(x, NY/2, NZ/2)", "x", "|psi|", "psi_x")
plot(Psi_norm_y, "|psi|(NX/2, y, NZ/2)", "z", "|psi|", "psi_y")
plot(Psi_norm_z, "|psi|(NX/2, NY/2, z)", "y", "|psi|",  "psi_z")

plot(Psi_pow_x, "|psi|^2(x, NY/2, NZ/2)", "x", "|psi|^2", "psi2_x")
plot(Psi_pow_y, "|psi|^2(NX/2, y, NZ/2)", "y", "|psi|^2", "psi2_y")
plot(Psi_pow_z, "|psi|^2(NX/2, NY/2, z)", "z", "|psi|^2", "psi2_z")