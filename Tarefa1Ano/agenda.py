import csv
import argparse


def substituir(arg1, arg2_none):
    """
    Essa função retorna o valor do segundo parametro caso ele exista, se não retorna o primeiro objeto
    :param arg1: Qualquer objeto
    :param arg2_none: Qualquer objeto, ou "None"
    :return: objeto 2 se existir. Caso contrário objeto 1
    """
    if arg2_none:
        return arg2_none
    else:
        return arg1


def criar_evento(agenda, nomeEvento, descricaoEvento, dataEvento, horaEvento):
    """
    cria o evento com base nos parametros dados
    :param agenda: um dicionario de dicionário que representa a agenda
    :param nomeEvento: nome do evento
    :param descricaoEvento: descrição do evento
    :param dataEvento: data do evento
    :param horaEvento: hora do evento
    :return: retorna a agenda (um dicionário) atualizada
    """
    if not agenda:  # caso a agenda esteja vazia, crie o primeiro evento com tag 1
        agenda["1"] = {"nome": nomeEvento, "descricao": descricaoEvento, "data": dataEvento, "hora": horaEvento,
                       "estado": "ativo"}
    else:
        agenda[str(len(agenda) + 1)] = {"nome": nomeEvento, "descricao": descricaoEvento, "data": dataEvento, "hora": horaEvento,
                       "estado": "ativo"}
    print("Evento criado")
    return agenda


def editar_evento(agenda, args):
    """
    Essa função edita a agenda com base nos parametros dados
    :param agenda: a agenda com os eventos a serem editados
    :param args: args contendo paramentros facultativos nome,descrição,data e hora
    :return: agenda editada
    """
    try:  # executar usando funcao substituir criada caso o evento exista
        agenda[str(args.evento)]["nome"] = substituir(agenda[str(args.evento)]["nome"], args.nome)
        agenda[str(args.evento)]["descricao"] = substituir(agenda[str(args.evento)]["descricao"], args.descricao)
        agenda[str(args.evento)]["data"] = substituir(agenda[str(args.evento)]["data"], args.data)
        agenda[str(args.evento)]["hora"] = substituir(agenda[str(args.evento)]["hora"], args.hora)
        print("Evento editado")
    except:
        print("Esse evento não existe!")
    return agenda


def deletar_evento(agenda, nEvento):
    """
    Altera o evento dado para desativado
    :param agenda: agenda a editar
    :param nEvento: numero do evento a ser deletado
    :return: agenda atualizada
    """
    # passar uma nova tupla com os mesmos valores que os antigos mas com o ultimo valor "removido"
    agenda[str(nEvento)]["estado"]="removido"
    print(f"Evento {nEvento} deletado")
    return agenda


def listar_evento_dia(agenda, dia):
    """
    Essa função lista todos os eventos do dia indicado, seguindo o padrão exigido nos exemplos
    :param agenda: agenda com os eventos (um dicionário)
    :param dia: dia exigido para mostrar os eventos
    :return: None, a função apenas printa (imprime) textos na tela
    """
    nenhum = True
    intro = True
    for evento in agenda:
        if agenda[str(evento)]["data"] == dia and agenda[str(evento)]["estado"] == "ativo":  # apenas eventos sem a tag 'removido'
            nenhum = False
            if intro:
                print(f"Eventos do dia {dia}")
                intro = False
            print("-----------------------------------------------")
            print(f"Evento {evento} - {agenda[str(evento)]['nome']}")
            print(f"Descrição: {agenda[str(evento)]['descricao']}")
            print(f"Data: {agenda[str(evento)]['data']}")
            print(f"Hora: {agenda[str(evento)]['hora']}")
    if nenhum:
        print(f"Não existem eventos para o dia {dia}!")
    else:
        print("-----------------------------------------------")


def criar_agenda(caminho):
    """
    Cria a agenda vazia no caminho especificado
    :param caminho: string contando o caminho da agenda a partir da pasta de origem
    :return: None
    """
    with open(caminho, 'w') as arquivo:
        arquivo.write("\n")
    print("Agenda criada")


def carregar_agenda(caminho):
    """
    carrega a agenda a partir de um arquivo .csv dado.
    :param caminho: caminho do arquivo (incluindo sua extensao)
    :return: retorna a agenda (um dicionário de dicionarios)
    """
    agenda = dict()
    with open(caminho, 'r') as arquivo:
        # receber a agenda sem virgulas e sem as ultimas quebras de linhas
        texto = csv.reader(arquivo, delimiter=',')
        for linha in texto:
            if len(linha) == 0:  # agenda ainda vazia
                return agenda
            agenda[linha[0]] = {"nome": linha[1],"descricao": linha[2],"data": linha[3],"hora": linha[4],"estado": linha[5]}

        return agenda


def executar_acao(agenda, args):
    """
    Executa outras açoes a partir da segunda instrução do segundo argumento
    :param agenda: a agenda para se realizar a ação (um dicionário)
    :param args: argumentos recebidos de main para passar para as funçoes
    :return: agenda alterada pelas funçoes (ou a mesma agenda inicial)
    """
    if args.a[1] == "criar":
        return criar_evento(agenda, args.nome, args.descricao, args.data, args.hora)
    elif args.a[1] == "alterar":
        return editar_evento(agenda, args)
    elif args.a[1] == "remover":
        return deletar_evento(agenda, args.evento)
    elif args.a[1] == "listar":
        listar_evento_dia(agenda, args.data)
        return agenda


def guardar_agenda(caminho, agenda):
    """
    Salva a agenda no arquivo indicado em extensão .csv
    :param caminho: string contendo o caminho indicado
    :param agenda: agenda a ser armazenda (um dicionario)
    :return: None
    """
    with open(caminho, 'w') as arquivo:
        if agenda:
            for evento in agenda:
                arquivo.write(
                    f"{evento},{agenda[evento]['nome']},{agenda[evento]['descricao']},{agenda[evento]['data']},{agenda[evento]['hora']},{agenda[evento]['estado']}\n")
            arquivo.write(f"\n")


def main():
    """
    função principal (menu)
    :return: None
    """
    # criar argumentos (é possivel criar uma função pra isso?(de maneira facil ou simples ou comum))
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", "-a", help="caminho do arquivo e acao a ser realizada separados por espaco", type=str,
                        nargs=2)
    parser.add_argument("--nome", "-nome", help="nome do evento em questao", type=str)
    parser.add_argument("--descricao", "-descricao", help="descricao do evento", type=str)
    parser.add_argument("--data", "-data", help="data do evento", type=str)
    parser.add_argument("--hora", "-hora", help="hora do evento", type=str)
    parser.add_argument("--evento", "-evento", help="numero do evento a ser modificado", type=int)
    args = parser.parse_args()

    # cria a agenda se o comando passado for inicializar
    if args.a[1] == "inicializar":
        criar_agenda(args.a[0])
    # receber agenda
    agenda = carregar_agenda(args.a[0])
    # executar acao desejada
    agenda = executar_acao(agenda, args)

    # salvar agenda em arquivo csv
    guardar_agenda(args.a[0], agenda)


main()
