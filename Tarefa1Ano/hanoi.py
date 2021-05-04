total=0

def resolverHanoi(num,inicio,meio,fim):
    global total
    if num ==1:
        #print(f"mova o disco {num} de {inicio} para {fim}")
        total+=1
    else:
        resolverHanoi(num-1,inicio,fim,meio)
        #print(f"mova o disco {num} de {inicio} para {fim}")
        total+=1
        resolverHanoi(num-1,meio,inicio,fim)

def main():
    resolverHanoi(int(input()),"A","B","C")
    print(total)

main()