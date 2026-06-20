import matplotlib.pyplot as plt

# Tus datos reales actualizados
dimensiones = ['Pequeña', 'Mediana', 'Grande']
tiempos = [0.0161, 0.0885, 0.1469]
costos = [22746, 43023, 62322]

# --- GRÁFICO 1: TIEMPO COMPUTACIONAL ---
plt.figure(figsize=(5, 3.8))
plt.plot(dimensiones, tiempos, marker='o', linestyle='-', color='#1f77b4', linewidth=2, markersize=8)
plt.title('Dimensión de la Red vs Tiempo de Ejecución', fontsize=11, fontweight='bold')
plt.xlabel('Tamaño de Instancia', fontsize=10)
plt.ylabel('Tiempo Promedio (segundos)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('grafico_tiempo.png', dpi=300)
plt.close()

# --- GRÁFICO 2: EVOLUCIÓN DE COSTOS ---
plt.figure(figsize=(5, 3.8))
plt.bar(dimensiones, costos, color='#ff7f0e', alpha=0.85, width=0.4)
plt.title('Dimensión de la Red vs Costo Total (Z)', fontsize=11, fontweight='bold')
plt.xlabel('Tamaño de Instancia', fontsize=10)
plt.ylabel('Costo Promedio ($)', fontsize=10)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('grafico_costos.png', dpi=300)
plt.close()

print("¡Listo! Ambos gráficos (tiempo y costos) fueron creados con éxito.")