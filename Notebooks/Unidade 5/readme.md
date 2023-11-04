# Wine Dataset for Clustering

Fonte: [Kaggle](https://www.kaggle.com/datasets/harrywang/wine-dataset-for-clustering?select=wine-clustering.csv)

Este conjunto de dados foi adaptado do Conjunto de Dados do Vinho de [https://archive.ics.uci.edu/ml/datasets/wine](https://archive.ics.uci.edu/ml/datasets/wine), removendo as informações sobre os tipos de vinho para aprendizado não supervisionado.

As seguintes descrições são adaptadas da página da UCI:

Estes dados são o resultado de uma análise química de vinhos cultivados na mesma região da Itália, mas derivados de três diferentes cultivares. A análise determinou as quantidades de 13 constituintes encontrados em cada um dos três tipos de vinhos.

Os atributos são:

* Álcool
* Ácido málico
* Cinza (Ash)
* Alcalinidade da cinza
* Magnésio
* Fenóis totais
* Flavonoides
* Fenóis não flavonoides
* Proantocianidinas
* Intensidade da cor
* Matiz (Hue)
* OD280/OD315 de vinhos diluídos
* Proline

# Groceries dataset

Fonte: [Kaggle](https://www.kaggle.com/datasets/heeraldedhia/groceries-dataset)

O conjunto de dados possui 38765 linhas de pedidos de compra de pessoas em supermercados. Esses pedidos podem ser analisados e regras de associação podem ser geradas usando Análise de Cesta de Mercado por algoritmos como o Algoritmo Apriori.

# Market Basket Analysis

Fonte [Kaggle](https://www.kaggle.com/datasets/aslanahmedov/market-basket-analysis)

* BillNo: número de 6 dígitos atribuído a cada transação. Nominal.
* Itemname: Nome do produto. Nominal.
* Quantity: As quantidades de cada produto por transação. Numérico.
* Date: O dia e a hora em que cada transação foi gerada. Numérico.
* Price: Preço do produto. Numérico.
* CustomerID: número de 5 dígitos atribuído a cada cliente. Nominal.
* Country: Nome do país onde cada cliente reside. Nominal.

# Arquivos .ipynb nessa pasta

* O arquivo ```clusterizacao.ipynb``` explora algoritmos de clusterizaçao utilizando os dados sobre vinho como substrato
* O arquivo ```regras_associacao.ipynb``` explora o conceito de mineração de regras de associação utilizando o algoritmo Apriori sobre os dados de ```Groceries_Dataset.csv``` e também faz uma análize de clusterização sobre os resultados de uma análise RFM sobre os dados de ```Assignment-1_Data.xlsx```