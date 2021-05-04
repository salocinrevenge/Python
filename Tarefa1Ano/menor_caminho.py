def receberLab():
    lab=[]
    while True:
        try:
            linha = input()
            fileira = []
            for char in linha:
                if not char == "/n":
                    fileira.append(char)
            lab.append(fileira)
        except:
            break

    return lab

def display(lab):
    for linha in lab:
        for char in linha:
            char=str(char)
            print(char[len(char)-1], end='')
        print()

def vazarAgua(lab,posx,posy,char):
    dirs=((0,1),(1,0),(0,-1),(-1,0))
    for dir in dirs:
        try:
            if lab[posy+dir[1]][posx+dir[0]] == "E":
                return (posy+dir[1],posx+dir[0])
            if lab[posy+dir[1]][posx+dir[0]] == " ":
                lab[posy+dir[1]][posx+dir[0]]=char
        except:
            continue
    return None


def escorrerAgua(lab,distancia):
    if distancia==0:
        for y,linha in enumerate(lab):
            for x,char in enumerate(linha):
                if char=="S":
                    tmp=vazarAgua(lab,x,y,distancia+1)
                    if tmp:
                        return tmp,distancia
                    break #só pode receber uma entrada e uma saida (pra o programa ficar mais rapido)
            else:
                continue
            break
        return escorrerAgua(lab, distancia + 1)
    else:
        for y, linha in enumerate(lab):
            for x, char in enumerate(linha):
                if char == distancia:
                    tmp = vazarAgua(lab, x, y, distancia + 1)
                    if tmp:
                        return tmp,distancia
        return escorrerAgua(lab,distancia+1)

def navegar(lab,x,y,dis):
    if lab[y][x]=="S":
        return
    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
    for dir in dirs:
        try:
            if lab[y + dir[1]][x + dir[0]] == "S":
                if not lab[y][x] == "E":
                    lab[y][x] = "*"
                return navegar(lab, x + dir[0], y + dir[1], dis - 1)
            if lab[y + dir[1]][x + dir[0]] == dis-1:
                if not lab[y][x]=="E":
                    lab[y][x]="*"
                return navegar(lab,x + dir[0],y + dir[1],dis-1)
        except:
            print("algo deu ruim :?")
            continue

def removerAgua(lab):
    for x,linha in enumerate(lab):
        for y,char in enumerate(linha):
            if type(char)==int:
                lab[x][y] = " "

def acharCaminho(lab):
    coords,dis=escorrerAgua(lab,0)
    navegar(lab,coords[1],coords[0],dis+1)
    removerAgua(lab)

def main():
    labirinto=receberLab()
    acharCaminho(labirinto)
    display(labirinto)

main()