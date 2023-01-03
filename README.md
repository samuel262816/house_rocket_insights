# Conhecendo o negócio

A House Rocket Company é uma empresa norte americana fictícia, que tem como modelo de negócio a compra e venda de imóveis. Sua principal estratégia é comprar bons imóveis e revendê-los posteriormente por preços mais altos. Porém, as casas possuem diversas características que podem torna-las mais ou menos interessante, como por exemplo a condição do imóvel, a localização e até mesmo o período do ano podem influenciar nos preços.

Nesse projeto, o objetivo é utilizar a análise e manipulação de dados para responder as questões de negócios e trazer insights para o CEO da empresa.

# 1.	Questões de negócio
  1. Quais são os imóveis que a House Rocket deveria comprar e por qual preço?
  2. Após comprado, qual o melhor momento para vende-lo e por qual preço?

# 2.	Premissas assumidas para a análise

  1. A análise foi realizada com dados entre 02/05/2014 e 27/05/2015
  2. O imóvel com 33 quartos foi considerado erro de digitação, pois seu tamanho não condiz com a quantidade de quartos e por isso foi removido da análise.
  3. Os imóveis com 0 banheiros também foram considerados erro de digitação e removido da análise.
  4. Os valores da coluna yr_renovated iguais a 0, são de casas que nunca foram reformadas
  5. A classificação da coluna view foi considerado: 0 = sem vista, 1 = vista ruim, 2 = vista regular, 3 = vista boa e 4 = vista excelente.
  6. A classificação da coluna grade foi considerado: 1-3 = muito baixa, 4-6 = baixa, 7 = média, 8-10 = alta, 11-13 = muito alta.
  7. A classificação da coluna condição foi considerado: 1 = muito ruim, 2 = ruim, 3 = regular, 4 = boa e 5 = excelente.

# 3.	Estratégia da solução
  1. Coletar os dados no kaggle
  2. Fazer a limpeza e descrição dos dados
  3. Criar novos atributos para auxilio na manipulação dos dados
  4. Fazer análise exploratória de dados para validar as hipóteses levantadas e encontrar insights para o negócio
  5. Responder as questões de negócio
  6. Criar dashboard no stramlit para visualização dos dados

## Planegamento para responder as questões de negócio:
1. Quais imóveis da House Rocket deveria comprar:
    - Agrupar os dados por região (zipcode)
    - Dentro de cada região, encontrar a mediana de preços
    - Sugerir compra dos imóveis com preço abaixo da mediana e que estejam em boas condições

2. Após comprado, qual o melhor momento para vende-lo e por qual preço:
    - Agrupar os dados por região (zipcode) e sazonalidade 
    - Dentro de cada região, encontrar a mediana de preços

### Condições de venda:
1. Se o preço da compra for maior que a mediana + sazonalidade:
   - Preço da venda = preço da compra + 10%

2. Se o preço da compra for menor que a mediana + sazonalidade:
   - Preço da venda = preço da compra + 30%

# 4.	Top 4 Insiths de dados

  1. Imóveis com vista para água são em média, 221% mais caros.

  2. Imóveis novos são em média 30% mais baratos do que os reformados.

  3. Imóveis com vista excelente são cerca de 50% mais caros.

  4. Imóveis com nota de construção acima de 10 são cerca de 227% mais caros do que os com nota abaixo de 10.

# 5.	O produto final do projeto

### 2 Relatórios:
1.	Sugestões de compras de imóveis por um valor recomendado
2.	Sugestões de vendas de imóveis por um valor recomendado

### Painel online: 
  Hospedado em uma cloud e disponível para acesso em qualquer dispositivo conectado à internet.
  
  O painel pode ser acessado através do link: https://house-rocket-samuel.streamlit.app/

# 6.	Conclusão
O objetivo desse projeto foi responder as questões de negócio e trazer os relatórios e insights em um dashboard para visualização. Sendo assim, todos os objetivos foram alcançados, trazendo boas recomendações de compra e venda de imóveis.

Caso fosse implementado, esse projeto seria capaz de trazer um lucro de aproximadamente US$76 Milhões. 

# 7.	Próximos Passos
  1.	Criar novos filtros
  2.	Utilizar modelos de machine learning para previsão dos preços dos imóveis
