import modulo
import re

def identar(string, nIdentacao):
    """
    Essa função recebe uma string e adiciona 2 espaços para cada valor de nIdentacao (adiciona 2*nIdentacao espaços)
    :param string: string a ser identada
    :param nIdentacao: numero de pares de espaços a ser adicionada no começo da string
    :return: string contendo espaços relativos a nIdentacao e a string original
    """
    res=""
    for _ in range(nIdentacao):
        res+="  "
    return res+string

def removerMarcasURL(url):
    """
    Essa é uma função auxiliar, que remove os 6 primeiros e o ultimo caracteres da string dada
    :param url: string a remover a marcação (href="  ")
    :return: string sem marcação
    """
    return url[6:len(url)-1]

def encontrarLinksValidos(url,origem):
    """
    a partir de um url dado, utiliza funções definidas em modulo.py para receber os links nesse site
    :param url: link da pagina a encontrar outros links
    :param origem: url da página de origem (Usado para definir os limites de navegação)
    :return:retorna uma lista com todos os links encontrados
    """
    texto=modulo.obter_html(url)
    #identificar a estrutura por href="____"
    linksEncontrados = re.findall(r"href=\"[^#@\s]+\"", texto)
    links=[]
    for link in linksEncontrados:
        link=removerMarcasURL(link)
        link=modulo.resolver_url(link,url)
        if modulo.eh_url_valida(link,origem):
            links.append(link)
    return links



def navegar(url,profundidade,arvore,origem,visitados):
    """
    Essa é uma função recursiva que entra em liks não conhecidos e definidos pela função do modulo.py "eh_url_valida.py".
    Se o link ainda não foi visitado, a função o visitará
    Ao final, retorna uma arvore de links visitados (string)
    :param url: url do site atual
    :param profundidade: int numero contendo o numero de sites ja visitados anteriormente (numero de chamada da função)
    :param arvore: string contendo todos os links identados de sites visitados
    :param origem: site de origem. Primeiro site visitado. (Usado para definir os limites de navegação)
    :param visitados: conjunto (set) com links de todos os sites já visitados
    :return: string contendo todos os links identados de sites visitados (antes e depois dessa chamada)
    """
    visitados.add(url)
    arvore+=identar(url,profundidade)+"\n"
    links=encontrarLinksValidos(url,origem)
    for link in links:
        if link not in visitados:
            arvore=navegar(link,profundidade+1,arvore,origem,visitados)
    return arvore


def main():
    """
    Função principal com a coleta de dados e saida de dados processados
    :return: None
    """
    url = input()
    print(navegar(url,0,"",url,set()),end="")

main()
