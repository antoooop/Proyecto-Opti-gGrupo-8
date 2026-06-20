import random
import json
import os

# fijamos la semilla para que siempre tire los mismos numeros exactos ---
random.seed(42)

def generar_instancia_valida(tipo, id_instancia, p_num, cd_num, zd_num):
    '''
    crea una instancia logistica asegurando por contrato que sea factible
    tanto en plantas como en la combinacion de los P centros mas chicos.
    '''
    # 1. demandas de cada zona (R_k)
    demandas = [random.randint(50, 200) for _ in range(zd_num)]
    total_pedidos = sum(demandas)
    
    # 2. capacidad de las plantas (S_i) con holgura del 30%
    cap_base_planta = int((total_pedidos * 1.3) / p_num)
    cap_plantas = [random.randint(cap_base_planta, cap_base_planta + 40) for _ in range(p_num)]
    
    # VALIDACION EXPLICITA 1: Oferta total de plantas debe ser mayor que la demanda
    if sum(cap_plantas) <= total_pedidos:
        return None # si falla la validacion, no sirve

    # 3. limite maximo de centros operativos (P)
    p_limite = random.randint(max(2, cd_num // 3), cd_num - 1)
    
    # 4. capacidades de los centros (H_j)
    cap_base_cd = int((total_pedidos * 1.4) / p_limite)
    cap_cds = [random.randint(cap_base_cd, cap_base_cd + 80) for _ in range(cd_num)]
    
    # VALIDACION EXPLICITA 2: ¿Los P centros con menor capacidad pueden cubrir la demanda?
    # ordenamos de menor a mayor y sumamos los P primeros. Si ellos cubren, cualquier combo sirve.
    cds_ordenados = sorted(cap_cds)
    if sum(cds_ordenados[:p_limite]) < total_pedidos:
        return None # infactible logisticamente si nos toca el peor combo, se descarta

    # 5. costos y transporte
    costos_p_cd = [[round(random.uniform(2.5, 12.0), 2) for _ in range(cd_num)] for _ in range(p_num)]
    costos_cd_z = [[round(random.uniform(1.8, 9.5), 2) for _ in range(zd_num)] for _ in range(cd_num)]
    costos_fijos = [random.randint(1500, 6000) for _ in range(cd_num)]

    # si paso todas las validaciones explicitas, armamos el json
    datos = {
        "I": p_num, "J": cd_num, "K": zd_num,
        "S": cap_plantas, "H": cap_cds, "R": demandas,
        "P": p_limite, "F": costos_fijos,
        "C": costos_p_cd, "D": costos_cd_z
    }
    
    return datos

def main():
    rangos = {
        "Pequena": {"P": (3, 10), "CD": (6, 12), "ZD": (8, 15)},
        "Mediana": {"P": (11, 20), "CD": (12, 24), "ZD": (16, 30)},
        "Grande":  {"P": (21, 35), "CD": (25, 40), "ZD": (31, 45)}
    }

    if not os.path.exists('mis_instancias'): 
        os.makedirs('mis_instancias')

    for t, r in rangos.items():
        intentos = 0
        instancias_creadas = 0
        while instancias_creadas < 5:
            intentos += 1
            p_n = random.randint(r["P"][0], r["P"][1])
            cd_n = random.randint(r["CD"][0], r["CD"][1])
            zd_n = random.randint(r["ZD"][0], r["ZD"][1])
            
            instancia = generar_instancia_valida(t, instancias_creadas + 1, p_n, cd_n, zd_n)
            
            if instancia is not None:
                instancias_creadas += 1
                with open(f"mis_instancias/instancia_{t}_{instancias_creadas}.json", 'w') as f:
                    json.dump(instancia, f, indent=4)
        print(f"categoria {t} terminada usando {intentos} intentos por filtros de factibilidad.")

if __name__ == "__main__":
    main()