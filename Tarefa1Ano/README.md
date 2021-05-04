O arquivo csv:

	A agenda é armazenada em arquivo .csv, utilizando "," como separador e nenhum tipo de cabeçalho para indicar cada uma das estruturas

	O arquivo csv tem a seguinte estrutura:

		--Cada linha simboliza um evento na agenda, sendo o numero do evento também o numero da linha

		-- Cada coluna representa uma característica do evento, sendo cada uma respectivamente:Numero do evento, nome do evento, descrição do evento, data do evento e hora do evento.

	Cada um desses valores será dado pelo próprio usuário, então cabe apenas a ele decidir o padrão (12/14, DD/MM/AAAA ou MM/DD/AAAA ou ainda dia-mês-ano) e a língua a ser escrito.


A agenda:

	A estrutura de dados escolida foi um dicionário de tuplas, sendo a chave do evento no dicionário, o seu número na forma de string. O primeiro valor da tupla é o seu nome, o segundo a sua descrição sem limites de extensão, o terceiro a data e o quarto a hora. O quinto valor da tupla será explicado mais adiante. Todos os valores são strings com o padrão decidido pelo próprio usuário no momento da criação do evento ou de sua edição (12/14, DD/MM/AAAA ou MM/DD/AAAA ou ainda dia-mês-ano), assim como a linguagem decidida.

	Cada evento possui um identificador extra: Uma string representando se ele ainda está ativo ou já foi removido. Essa característica foi pensada para que o usuário possa ver quais eventos foram removidos ou recuperar um evento deletado por engano, simplesmente alterando manualmente o arquivo csv. Isso causa uma queda de desempenho para agendas muito extensas, então para agendas com muitos valores deletados seria uma boa ideia criar uma nova agenda.


Os comandos:

	A cada execução do programa o usuário deve passar o parametro -a <caminho> <ação> identificando o local e nome que o arquivo foi ou será guardado e a ação (inicializar, criar,alterar,remover,listar) a ser executada.

	Cada ação exige ou permite uma combinação de parametros, mas de modo geral são eles: -nome (criar,alterar*) -descricao (criar,alterar*) -data (criar,alterar*,listar) -hora (criar,alterar*) -evento (alterar,remover).
Entre parênteses estão os comandos que exigem esse parametro e os que possuem ele como adicional (com asterisco).

Use bem a sua agenda =D.

Caso possua alguma crítica ou sugestão entre em contado comigo atraés do meu email.