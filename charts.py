import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Tamanho": [100, 1000, 2500, 5000, 7500, 10000],
    "Tempo_codificação_STRING": [
        0.001083,
        0.000905,
        0.000000,
        0.001004,
        0.001624,
        0.002002,
    ],
    "Tempo_codificação_BITWISE": [
        0.001177,
        0.000998,
        0.001025,
        0.002398,
        0.003084,
        0.005004,
    ],
    "Memória_codificação_STRING": [
        0.007812,
        0.003906,
        0.011719,
        0.023438,
        0.039062,
        0.062500,
    ],
    "Memória_codificação_BITWISE": [
        0.007812,
        0.011719,
        0.046875,
        0.195312,
        0.281250,
        0.410156,
    ],
    "Tamanho_codificado_STRING": [200, 2000, 5000, 10000, 15000, 20000],
    "Tamanho_codificado_BITWISE": [25, 250, 625, 1250, 1875, 2500],
    "Tempo_decodificação_STRING": [
        0.000000,
        0.001002,
        0.001396,
        0.001495,
        0.001883,
        0.004061,
    ],
    "Tempo_decodificação_BITWISE": [
        0.000000,
        0.001002,
        0.001660,
        0.002999,
        0.006595,
        0.007127,
    ],
    "Memória_decodificação_STRING": [
        0.000000,
        0.000000,
        0.003906,
        0.003906,
        0.003906,
        0.066406,
    ],
    "Memória_decodificação_BITWISE": [
        0.000000,
        0.105469,
        0.394531,
        0.546875,
        0.820312,
        1.058594,
    ],
}

df = pd.DataFrame(data)

# Plotting
fig, axes = plt.subplots(3, 2, figsize=(14, 12))
fig.suptitle(
    "Comparação de Codificação e Decodificação: Métodos STRING vs BITWISE", fontsize=16
)

# Tempo de Codificação
axes[0, 0].plot(
    df["Tamanho"], df["Tempo_codificação_STRING"], marker="o", label="STRING"
)
axes[0, 0].plot(
    df["Tamanho"], df["Tempo_codificação_BITWISE"], marker="o", label="BITWISE"
)
axes[0, 0].set_title("Tempo de Codificação (s)")
axes[0, 0].set_xlabel("Tamanho do Arquivo")
axes[0, 0].set_ylabel("Tempo (s)")
axes[0, 0].legend()

# Memória para Codificação
axes[0, 1].plot(
    df["Tamanho"], df["Memória_codificação_STRING"], marker="o", label="STRING"
)
axes[0, 1].plot(
    df["Tamanho"], df["Memória_codificação_BITWISE"], marker="o", label="BITWISE"
)
axes[0, 1].set_title("Memória para Codificação (MB)")
axes[0, 1].set_xlabel("Tamanho do Arquivo")
axes[0, 1].set_ylabel("Memória (MB)")
axes[0, 1].legend()

# Tamanho do Arquivo Codificado
axes[1, 0].plot(
    df["Tamanho"], df["Tamanho_codificado_STRING"], marker="o", label="STRING"
)
axes[1, 0].plot(
    df["Tamanho"], df["Tamanho_codificado_BITWISE"], marker="o", label="BITWISE"
)
axes[1, 0].set_title("Tamanho do Arquivo Codificado (bytes)")
axes[1, 0].set_xlabel("Tamanho do Arquivo")
axes[1, 0].set_ylabel("Tamanho Codificado (bytes)")
axes[1, 0].legend()

# Tempo de Decodificação
axes[1, 1].plot(
    df["Tamanho"], df["Tempo_decodificação_STRING"], marker="o", label="STRING"
)
axes[1, 1].plot(
    df["Tamanho"], df["Tempo_decodificação_BITWISE"], marker="o", label="BITWISE"
)
axes[1, 1].set_title("Tempo de Decodificação (s)")
axes[1, 1].set_xlabel("Tamanho do Arquivo")
axes[1, 1].set_ylabel("Tempo (s)")
axes[1, 1].legend()

# Memória para Decodificação
axes[2, 0].plot(
    df["Tamanho"], df["Memória_decodificação_STRING"], marker="o", label="STRING"
)
axes[2, 0].plot(
    df["Tamanho"], df["Memória_decodificação_BITWISE"], marker="o", label="BITWISE"
)
axes[2, 0].set_title("Memória para Decodificação (MB)")
axes[2, 0].set_xlabel("Tamanho do Arquivo")
axes[2, 0].set_ylabel("Memória (MB)")
axes[2, 0].legend()

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
