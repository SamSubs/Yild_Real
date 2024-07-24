class Principal():
    print(f'{"INFORMAÇÕES":^60}')
    print('\nM2 Brasil https://pt.tradingeconomics.com/brazil/money-supply-m2')
    print('Inflação Brasil https://pt.tradingeconomics.com/brazil/inflation-cpi')
    print(f'{"-" * 60}')

    def yild(self):
        try:
            while True:
                print(f'\n{"Yild Real":^40}')

                user = int(input('\nReal    [1]\nDolar   [2]\nOutros  [3]\nSair    [4]\n:'))

                if user == 1:
                    print('{:^40}'.format('Periodo de 12 Meses(1 Ano)'))
                    dividend = float(input('Valor do Dividendo R$ '))
                    Valor_Cota = float(input('Valor Cota R$ '))
                    #dividend = float(1.41)
                    #Valor_Cota = float(8.43)

                    dy_do_ativo = (dividend / Valor_Cota) * 100

                    print('\n{:^40}\n Yd ao Ano {:.2f}% Mes {:.2f}%'.format('Lucro Nominal', dy_do_ativo, dy_do_ativo / 12))
                    #Dados
                    # Agregado Monetario em Milhoes
                    M1 = [0, 0, 0]

                    # Agregado Monetario em Milhoes
                    M2 = [5.33, 6.11, 12]

                    # Agregado Monetario em Milhoes
                    M3 = [0, 0, 0]

                    # taxa De Inflação Periodo em %
                    TI = [3.94, 4.23, 12]
                    #Fim Dados

                    calculo_M2 = ((M2[1]-M2[0]) / M2[0]) * 100

                    calculo_TI = ((TI[1] - TI[0]) / TI[1]) * 100


                    print(f'{40 * "-"}\n')
                    print('Variação M2 no periodo: {:.2f}%\nInflação Periodo {:.2f}%\nAcumulado {:.2f}%\n'.format(calculo_M2, calculo_TI, calculo_M2 + calculo_TI))
                    print(f'{40 * "-"}')


                    #calculo Ganho Real
                    retorno_ano = dy_do_ativo-(calculo_M2+calculo_TI)
                    calculo_r = (1/(1-(abs(retorno_ano/100))))
                    #parte_cota = ((calculo-calculo_M2)*Valor_Cota)/100

                    print(f'{"lucro Real":^40}\nGanho Periodo {retorno_ano:.2f}%\n')
                    if retorno_ano <= 0.00:
                        print(f'Sem perda pela Inflação\nDividendo 12 Meses R${(dividend*calculo_r) + dividend:.2f}\nDiferença R$ {((dividend*calculo_r) + dividend)-dividend:.2f}\n')
                        #print(f'\n Variação Sobre o Preço da cota R${Valor_Cota - parte_cota:.2f}')
                        #print(calculo_r, '\n', (dividend*calculo_r) + dividend)


                    #Simulação
                    #investido = 1000


                elif user == 2:
                    dolar_cotacao = float(input('Cotação Dolar R$ '))
                    dividend = int(input('Valor do Dividendo USD $ '))

                elif user == 3:
                    from Dados import Edicao
                    user_2 = Edicao()
                    user_2.menu()

                elif user == 4:
                    print('Saindo...')
                    exit()


        except ValueError as erro:
            print(f'Erro {erro}')

loop = Principal()
loop.yild()
