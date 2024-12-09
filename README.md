# YILD REAl

A Escola Austríaca de economia tem uma abordagem distinta em relação ao cálculo da inflação, diferenciando-se das abordagens mais convencionais, como a do mainstream econômico.

1. **Definição de Inflação**: Para a Escola Austríaca, inflação não é apenas o aumento geral dos preços (como é comumente entendido), mas sim a expansão da oferta monetária, ou seja, o aumento na quantidade de dinheiro em circulação. Esse aumento na oferta monetária é visto como a causa fundamental de um aumento geral nos preços ao longo do tempo.

2. **Ênfase na Teoria do Ciclo Econômico**: A Escola Austríaca foca na teoria do ciclo econômico, que postula que a inflação (expansão da oferta monetária) leva a uma distorção na estrutura de produção da economia. Isso significa que a inflação, ao alterar as taxas de juros artificiaismente baixas, induz investimentos que não são sustentáveis a longo prazo, o que pode levar a crises econômicas futuras.

3. **Críticas ao Índice de Preços ao Consumidor (IPC)**: A Escola Austríaca critica o uso do IPC como medida de inflação, argumentando que ele não captura adequadamente todas as mudanças nos preços, especialmente em um ambiente de constante mudança tecnológica e inovação. Além disso, a Escola Austríaca enfatiza que o impacto da inflação pode ser sentido de forma desigual na economia, afetando diferentes setores e grupos de maneiras distintas.

4. **Cálculo da Inflação**: Para calcular a inflação do ponto de vista austríaco, o foco seria na análise da expansão da base monetária, na manipulação das taxas de juros pelo banco central e nos efeitos disso sobre a estrutura produtiva da economia. Em termos práticos, isso envolveria monitorar a política monetária, a criação de dinheiro pelo banco central e como esses fatores afetam a economia real ao longo do tempo.

Para calcular a taxa de inflação usando o M2, podemos aplicar a seguinte fórmula:

  Taxa de Inflação=((M2 inicial - M2 final) / M2 inicial ​ )×100
  
//------------------------------------------------------------------------------------------------------------------------//

  Finalidade do Codigo
O Codigo tem como objetivo calcular o yild real de inflação com base na abordagem da Escola Austríaca de economia.

- **Parâmetros:**
  - `M2_inicial`: Representa o valor inicial da oferta monetária (M2) em uma unidade monetária específica (por exemplo, trilhões de dólares).
  - `M2_final`: Representa o valor final da oferta monetária (M2) após um período de tempo.
 
  - `IPCA_inicial`: Representa o valor inicial da Variação dos Preços no Periodo (IPCA) em específica (por %).
  - `IPCA_final`: Representa o valor final da Variação dos Preços no Periodo (IPCA) após um período de tempo.

- **Cálculo da Taxa de Inflação:**
  - A função calcula a taxa de inflação utilizando a seguinte fórmula:
    
        Taxa de Inflação M2 =((M2 inicial - M2 final) / M2 inicial ​ )×100
        Taxa de Inflação IPC = ((IPCA/IPC inicial - IPCA/IPC final) / IPCA/IPC inicial ​ )×100
        Total Acumulado = Taxa de Inflação M2 +  Taxa de Inflação IPCA

        Yild_Final = Yild do Periodo - Total Acumulado #Em %
    
  - Esta fórmula determina a variação percentual entre o valor final e o valor inicial da oferta monetária (M2), expressando a mudança como uma porcentagem da base inicial.

- **Retorno do yild do Investimento:**
  - A função retorna a taxa de inflação calculada como um número decimal, representando a porcentagem de mudança na oferta monetária durante o período considerado;
  - A Função Retorna o Total Acumulado do Periodo.
  - 
  //------------------------------------------------------------------------------------------------------------------------//
