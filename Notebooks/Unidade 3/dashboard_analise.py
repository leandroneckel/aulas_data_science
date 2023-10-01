import pandas as pd
dados = pd.read_excel('dados_vinho_tratado.xlsx')
x = dados.iloc[:,:13].values
y = dados.iloc[:,13].values
from sklearn.model_selection import train_test_split
x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,train_size=0.8,random_state=42)
colunas_x = dados.columns.tolist()
colunas_x.pop()
colunas_y = dados.columns.tolist()
colunas_y = colunas_y[-1]
y_test = pd.DataFrame(y_teste,columns=[colunas_y])
x_test = pd.DataFrame(x_teste,columns=colunas_x)
from sklearn.ensemble import RandomForestClassifier
from explainerdashboard import ClassifierExplainer, ExplainerDashboard
modelo = RandomForestClassifier(n_estimators=50, max_depth=5)
modelo.fit(x_treino, y_treino)
explainer = ClassifierExplainer(modelo, x_test, y_test)
dashboard = ExplainerDashboard(explainer, title="Meu Dashboard", mode='inline')
dashboard.run(port=8050)