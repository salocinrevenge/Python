def acharMenor(anterior,lista):
    if len(lista)==0:
        return anterior+1
    elif not lista[0]-anterior==1:
        return anterior+1
    else:
        return acharMenor(anterior+1,lista[1:len(lista)])

def main():
    print(acharMenor(-1,list(map(int, input().split()))))

main()