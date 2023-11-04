def limpiar_pib(line: str):
    n = 0
    com = False
    for i, x in enumerate(line):
        if x=='"':
            com = not com
        if com: continue
        if x==",":
            n+=1
            if n==2:
                r = line[:i]
            if n==11:
                return r+line[i:]
        

def limipiar_regiones_pib():
    with open("PIB_regiones.csv", "r", encoding="utf-8") as file:
        lines = file.readlines()

    lines = [limpiar_pib(line) for line in lines]

    with open("regiones.csv", "w", encoding="utf-8") as file:
        file.writelines(lines)

if __name__=='__main__':
    limipiar_regiones_pib()