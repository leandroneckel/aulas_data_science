# Projeto da unidade 4
## Machine Learning de Classificação.

### Sobre o dataset:

As informações coletadas são da DAEWOO Steel Co. Ltd em Gwangyang, Coreia do Sul. Ela produz vários tipos de bobinas, chapas de aço e chapas de ferro. As informações sobre o consumo de eletricidade estão armazenadas em um sistema baseado na nuvem. As informações sobre o consumo de energia da indústria estão armazenadas no site da Korea Electric Power Corporation (pccs.kepco.go.kr), e as perspectivas dos dados diários, mensais e anuais são calculadas e exibidas.

#### Informações dos atributos:

Column Name | Data Variables | Type | Measurement | Feature ou Target
--- | --- | --- | --- | ---
usage_kwh | Industry Energy Consumption | Continuous | kWh | Target
lagging_current_reactive_power_kvarh | Lagging Current reactive power | Continuous | kVarh | Feature
leading_current_reactive_power_kvarh | Leading Current reactive power | Continuous | kVarh | Feature
co2_tco2_ | tCO2(CO2) | Continuous | ppm | Feature
lagging_current_power_factor | Lagging Current power factor | Continuous | % | Feature
leading_current_power_factor | Leading Current Power factor | Continuous | % | Feature
nsm | Number of Seconds from midnight | Continuous | S | Feature
weekstatus | Week status | Categorical | Weekend or a Weekday | Feature
day_of_week | Day of week | Categorical | Sunday, Monday â€¦. Saturday | Feature
load_type | Load Type | Categorical | Light Load, Medium Load, Maximum Load | Feature

#### Fonte:

[Repositório de DataSets de Machine Learning da UCI](https://archive.ics.uci.edu/dataset/851/steel+industry+energy+consumption) (Traduzido com o ChatGPT4)

### Sobre o projeto

Em grupos de até 6 pessoas, desenvolver um jupyter notebook que treine e avalie modelos de Machine Learning de Regressão. 

Deve haver:

* Préprocessamento 
* Feature Engineering (PCA, por exemplo)
* Tuning de hiperparâmetros e Cross Validation
* Métodos de Ensemble (Boosting, Baggins, Stacking, etc...)

#### Métricas de avaliação:
* R2
* MAPE (Mean Absolut Percentage Error)

#### Objetivo
Encontrar o melhor modelo de regressão possível para o dataset fornecido.

#### O que deverá ser submetido:
Em um arquivo .rar, ter:
* A base de dados
* Arquivo de jupyter notebook com a sequência de procedimentos de tratamento de dados e treinamento de algoritmos de ML
* O arquivo de requerimentos necessários (requirements.txt)

Obs.: Serão aceitos mais de um jupyter notebook se o grupo desejar notebooks diferentes para diferentes rotas de preprocessamento, treinamento, etc.

## Iniciando projeto
Para iniciar o projeto, coloque o arquivo ```dados_projeto_4.csv``` em uma nova pasta em seu computador e, após isto, com o cmd ou o Powershell aberto nessa pasta, inicie e ative o venv por meio de

```powershell
>>> python -m venv venv
>>> .\venv\Scripts\Activate.ps1
```

Após isto, dentro do venv ativado, instale as bibliotecas iniciais necessárias para qualquer projeto:

```powershell
>>> pip install pandas jupyter scikit-learn matplotlib seaborn
```

Após a instalação, para gerar automaticamente o arquivo de requerimentos, também com o venv ativado, utilize

```powershell
>>> pip freeze > requirements.txt
```

Lembre-se de selecionar o kernel criado antes de executar a primeira célula de um jupyter notebook

Se, ao longo do projeto, outras bibs forem necessárias, instale utilizando ```pip install (...)``` e não esqueça de rodar também o ```pip freeze > requirements.txt``` após isto.

Antes da entrega, lembrar de rodar o ```pip freeze > requirements.txt``` para anexar o arquivo com todas as dependencias no ```.rar``` a ser publicado

Obs.: Para a entrega, não incluir no arquivo compactado a pasta ```venv```