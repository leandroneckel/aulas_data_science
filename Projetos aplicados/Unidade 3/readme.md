# Projeto da unidade 3
## Machine Learning de Classificação.

### Sobre o dataset:

Os dados são gerados por MC (veja abaixo) para simular o registro de partículas gama de alta energia em um telescópio gama Cherenkov atmosférico terrestre usando a técnica de imagem. O telescópio gama Cherenkov observa raios gama de alta energia, aproveitando a radiação emitida por partículas carregadas produzidas dentro dos chuveiros eletromagnéticos iniciados pelos gamas, e se desenvolvendo na atmosfera. Esta radiação Cherenkov (de comprimentos de onda visíveis a UV) vaza através da atmosfera e é registrada no detector, permitindo a reconstrução dos parâmetros do chuveiro. A informação disponível consiste em pulsos deixados pelos fótons Cherenkov que chegam nos tubos fotomultiplicadores, organizados em um plano, a câmera. Dependendo da energia do gama primário, um total de algumas centenas a cerca de 10.000 fótons Cherenkov são coletados, em padrões (chamados de imagem do chuveiro), permitindo discriminar estatisticamente aqueles causados ​​por gamas primários (sinal) das imagens de chuveiros hadrônicos iniciados por raios cósmicos na atmosfera superior (fundo).

Tipicamente, a imagem de um chuveiro após algum pré-processamento é um agrupamento alongado. Seu eixo longo é orientado em direção ao centro da câmera se o eixo do chuveiro for paralelo ao eixo óptico do telescópio, ou seja, se o eixo do telescópio estiver direcionado para uma fonte pontual. Uma análise de componente principal é realizada no plano da câmera, o que resulta em um eixo de correlação e define uma elipse. Se as deposições fossem distribuídas como uma Gaussiana bivariada, esta seria uma elipse de equidensidade. Os parâmetros característicos desta elipse (frequentemente chamados de parâmetros Hillas) estão entre os parâmetros de imagem que podem ser usados para discriminação. As deposições de energia são tipicamente assimétricas ao longo do eixo principal, e essa assimetria também pode ser usada na discriminação. Há, além disso, outras características discriminantes, como a extensão do agrupamento no plano da imagem, ou a soma total das deposições.

#### Informações dos atributos:

1. fLength: contínuo # eixo principal da elipse [mm]
2. fWidth: contínuo # eixo menor da elipse [mm]
3. fSize: contínuo # 10-log da soma do conteúdo de todos os pixels [em #fot]
4. fConc: contínuo # razão da soma dos dois pixels mais altos sobre fSize [razão]
5. fConc1: contínuo # razão do pixel mais alto sobre fSize [razão]
6. fAsym: contínuo # distância do pixel mais alto até o centro, projetada no eixo principal [mm]
7. fM3Long: contínuo # 3ª raiz do terceiro momento ao longo do eixo principal [mm]
8. fM3Trans: contínuo # 3ª raiz do terceiro momento ao longo do eixo menor [mm]
9. fAlpha: contínuo # ângulo do eixo principal com vetor para a origem [graus]
10. fDist: contínuo # distância da origem até o centro da elipse [mm]
11. class: g,h # gama (sinal), hádron (fundo)

#### Fonte:

[Repositório de DataSets de Machine Learning da UCI](https://archive.ics.uci.edu/dataset/159/magic+gamma+telescope) (Traduzido com o ChatGPT4)

### Sobre o projeto

Em grupos de até 6 pessoas, desenvolver um jupyter notebook que treine e avalie modelos de Machine Learning de Classificação. Deve haver:
* Avaliação dos mesmos modelos treinados através de diferentes preprocessamentos da base
* Avaliaçao dos modelos treinados sob diferentes hyperparâmetros.

#### Métricas de avaliação:
* Accuracy Score
* Precision Score
* Recall Score
* F1 Score
* Matriz de Confusão

#### Objetivo
Encontrar o melhor modelo de classificação possível para o dataset fornecido.

#### O que deverá ser submetido:
Em um arquivo .rar, ter:
* A base de dados no
* Arquivo de jupyter notebook com a sequência de procedimentos de tratamento de dados e treinamento de algoritmos de ML
* O arquivo de requerimentos necessários (requirements.txt)

Obs.: Serão aceitos mais de um jupyter notebook se o grupo desejar notebooks diferentes para diferentes rotas de preprocessamento.

#### IMPORTANTE
Não utilizar GridSearchCV para busca dos melhores hyperparâmetros dos modelos. Será trabalhado nas próximas aulas.

## Iniciando projeto
Para iniciar o projeto, coloque o arquivo ```dados_projeto_03.csv``` em uma nova pasta em seu computador e, após isto, com o cmd ou o Powershell aberto nessa pasta, inicie e ative o venv por meio de

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