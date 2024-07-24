class Edicao():
    def menu(self):
        try:
            arquivo = open('Dados.txt', 'r+')
            texto = arquivo.read()
            print(texto)
            arquivo.close()

        except FileNotFoundError as erro:
            print('Criando Arquivo')
            arquivo = open('Dados.txt', 'a')
            arquivo.close()

        user = int(input('ADICIONAR DADOS [1]\nEXIBIR TUDO     [2]\nAPAGAR TUDO     [3]\nSAIR            [4]\n:'))

        if user == 1:
            arquivo.close()
            escrever = open('Dados.txt', 'a')
            print(f'{"Em Mi":^40}')

            periodo = str(input('ANO DOS DADOS: '))
            m2_inicial = float(input(f'{"AGREGADOS M2":^40}\nINICIAL :'))
            m2_final = float(input(f'{"AGREGADOS M2":^40}\nFINAL :'))
            ipca_inicio = float(input(f'{"IPCA":^40}\nINICIAL :'))
            ipca_final = float(input(f'{"IPCA":^40}\nfinal :'))

            escrever.write(f'\n{periodo}\n{m2_inicial}\n{m2_final}\n{ipca_inicio}\n{ipca_final}\n')

        elif user == 2:
            arquivo.close()
            ler = open('Dados.txt', 'r')
            dados = ler.read()
            print(str(dados))

        elif user == 3:
            def apagar_texto_arquivo(nome_arquivo):
                try:
                    # Abre o arquivo em modo de escrita ('w' - write mode)
                    with open(nome_arquivo, 'w') as arquivo:
                        arquivo.write('')  # Sobrescreve o conteúdo com uma string vazia
                    print(f"Conteúdo do arquivo '{nome_arquivo}' foi apagado com sucesso.")
                except IOError:
                    print(f"Erro ao tentar abrir ou escrever no arquivo '{nome_arquivo}'.")

            # Exemplo de uso:
            nome_do_arquivo = 'Dados.txt'
            apagar_texto_arquivo(nome_do_arquivo)

        elif user == 4:
            print('Saindo')
            exit()

from Yd_Real import Principal
voltar = Principal()
voltar.yild()
#x = Edicao()
#x.menu()
