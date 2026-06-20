import gurobipy as gp
from gurobipy import GRB
import json
import os
import time

def resolver_instancia(ruta_json):
    with open(ruta_json, 'r') as f:
        data = json.load(f)
        
    I_len, J_len, K_len = data["I"], data["J"], data["K"]
    S, H, R, P, F = data["S"], data["H"], data["R"], data["P"], data["F"]
    C, D = data["C"], data["D"]

    env = gp.Env(empty=True)
    env.setParam('OutputFlag', 0)
    env.start()
    model = gp.Model("RedLogistica", env=env)

    #variables de decision
    x = model.addVars(I_len, J_len, vtype=GRB.CONTINUOUS, name="x")
    y = model.addVars(J_len, K_len, vtype=GRB.CONTINUOUS, name="y")
    z = model.addVars(J_len, vtype=GRB.BINARY, name="z")

    #restricciones
    model.addConstrs((gp.quicksum(x[i,j] for j in range(J_len)) <= S[i] for i in range(I_len)), name="CapPlantas")
    model.addConstrs((gp.quicksum(x[i,j] for i in range(I_len)) == gp.quicksum(y[j,k] for k in range(K_len)) for j in range(J_len)), name="ConsFlujo")
    model.addConstrs((gp.quicksum(y[j,k] for k in range(K_len)) <= H[j] * z[j] for j in range(J_len)), name="CapCD")
    model.addConstrs((gp.quicksum(y[j,k] for j in range(J_len)) == R[k] for k in range(K_len)), name="SatisfaDemanda")
    model.addConstr(gp.quicksum(z[j] for j in range(J_len)) <= P, name="MaxCentros")

    #Funcion objetivo
    model.setObjective(
        gp.quicksum(F[j]*z[j] for j in range(J_len)) +
        gp.quicksum(C[i][j]*x[i,j] for i in range(I_len) for j in range(J_len)) +
        gp.quicksum(D[j][k]*y[j,k] for j in range(J_len) for k in range(K_len)),
        GRB.MINIMIZE
    )

    #Optimizar midiendo tiempo computacional
    t_inicio = time.time()
    model.optimize()
    t_total = time.time() - t_inicio

    #Recopilar las métricas para el análisis del informe
    if model.status == GRB.OPTIMAL:
        centros_abiertos = sum(1 for j in range(J_len) if z[j].X > 0.5)
        return {
            "Costo_Total": model.ObjVal,
            "Tiempo_s": round(t_total, 4),
            "Variables": model.NumVars,
            "Restricciones": model.NumConstrs, 
            "CD_Abiertos": centros_abiertos,
            "P_Maximo": P,
            "Iteraciones": model.IterCount,
            "Nodos": model.NodeCount
        }
    return None

# Recorrer la carpeta mis_instancias y resolver todo de una
resultados_finales = []
print(f"{'Instancia':<25} | {'Costo Total':<12} | {'Tiempo (s)':<10} | {'Vars':<6} | {'Restr':<6} | {'CD Open/P':<10}")
print("-" * 80)

for archivo in sorted(os.listdir('mis_instancias')):
    if archivo.endswith('.json'):
        res = resolver_instancia(os.path.join('mis_instancias', archivo))
        if res:
            nombre = archivo.replace(".json", "")
            print(f"{nombre:<25} | {res['Costo_Total']:<12.1f} | {res['Tiempo_s']:<10} | {res['Variables']:<6} | {res['Restricciones']:<6} | {res['CD_Abiertos']}/{res['P_Maximo']}")