# Projeto da unidade 2
## Pré processamento de dados

### Metadados

* id - Unique ID for the customer
* Gender - Gender of the customer
* Age - Age of the customer
* Driving_License - 0 : Customer does not have DL, 1 : Customer already has DL
* Region_Code - Unique code for the region of the customer
* Previously_Insured - 1 : Customer already has Vehicle Insurance, 0 : Customer doesn't have Vehicle Insurance
* Vehicle_Age - Age of the Vehicle
* Vehicle_Damage - 1 : Customer got his/her vehicle damaged in the past. 0 : Customer didn't get his/her vehicle damaged in the past.
* Annual_Premium - The amount customer needs to pay as premium in the year
* Policy_Sales_Channel - Anonymized Code for the channel of outreaching to the customer ie. Different Agents, Over Mail, Over Phone, In Person, etc.
* Vintage - Number of Days, Customer has been associated with the company
* Response - 1 : Customer is interested, 0 : Customer is not interested

O dataset foi tirado do site do [Kaggle](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction), mas foi editado com inserção manual de valores faltantes e dados escritos de forma equivocada

### Atividade

Em grupos de até 6 pessoas, desenvolver um jupyter notebook que faça o preprocessamento dos dados e avalie o desempenho do modelo de Machine Learning de acordo com o pré-processamento

É importante que sejam explicados os passos que foram sendo dados ao longo do jupyter notebook por meio de células markdown

No início do Jupyter Notebook é necessário colocar o nome e número de matrícula dos componentes do grupo e a entrega do jupyter notebook finalizado deverá ser feita por meio do AVA até a data e hora definidas para postagem no AVA

Código do treinamento e teste do modelo de Machine Learning a ser utilizado no final do pré-processamento:

```python 
from sklearn.metrics import f1_score,accuracy_score
from sklearn.tree import DecisionTreeClassifier

x_treino = x # aqui deve ser colocado o array bidimensional balanceado ou nanãoo dos atributos para treino
y_treino = y # aqui deve ser colocado o array unidimensional balanceado ou não do target para treino
x_teste = teste.iloc[:,:index_col_target].values #separando os dados de teste em x
y_teste = teste.iloc[:,index_col_target].values #separando os dados de teste em y

modelo = DecisionTreeClassifier()
modelo.fit(x_bal,y_bal)
y_pred = modelo.predict(x_teste)
f1 = f1_score(y_teste,y_pred)
acc = accuracy_score(y_teste,y_pred)
print(f"Esse modelo retornou F1 Score = {f1} e Accuracy Score = {acc}")
```

Para que você possa organizar os resultados dos modelos, coloque o seguinte código no início do jupyter notebook (Lmebre-se de rodar essa célula somente uma vez, caso contrário o dataframe de registro de resultados será zerado)

```python
import pandas as pd
resultados = pd.DataFrame(columns = ['nome_modelo','f1_score','accuracy_score'])
```

E o seguinte código no final do jupyter notebook

```python
### Se você desejar colocar esse resultado em um dataframe, rode esta célula.
### Obs.: Vai ser pedido para você dar um nome ao modelo que treinou para que seja colocado no dataframe
nome = input('Digite o nome do modelo: ')
add = [nome,f1,acc]
resultados.loc[resultados.shape[0]]=add
resultados
```
