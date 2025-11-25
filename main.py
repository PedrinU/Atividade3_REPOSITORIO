import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Questão 1
# ==============================================================================
print("\n" + "="*50)
print("QUESTÃO 1: Carregamento do Dataset")
print("="*50)

url = 'https://github.com/alanjones2/dataviz/raw/master/londonweather.csv'

df_weather = pd.read_csv(url)
print("Dados carregados com sucesso (Primeiras 5 linhas):")
print(df_weather.head())


# Questão 2
# ==============================================================================
print("\n" + "="*50)
print("QUESTÃO 2: Visualização e Compressão Inicial dos Dados")
print("="*50)
print("Estatísticas Descritivas (Resumo das colunas numéricas):")
print(df_weather.describe())
print("\nInformações sobre Tipos de Dados e Valores Não-Nulos:")
df_weather.info()


# Questão 3-A
# ==============================================================================
print("\n" + "="*50)
print("QUESTÃO 3-A: Verificando o Último Ano Registrado")
print("="*50)

df_weather['Year'] = pd.to_numeric(df_weather['Year'], errors='coerce')
ultimo_ano = df_weather['Year'].max()

print(f"O último ano registrado no dataset é: **{int(ultimo_ano)}**")


# Questão 3-B
# ==============================================================================
print("\n" + "="*50)
print("QUESTÃO 3-B: Obtendo os Últimos 10 Anos de Dados")
print("="*50)

ano_inicio = ultimo_ano - 9

df_ultimos_10_anos = df_weather[
    (df_weather['Year'] >= ano_inicio) &
    (df_weather['Year'] <= ultimo_ano)
]
print(
    f"DataFrame filtrado para os 10 anos: de **{int(ano_inicio)}** até **{int(ultimo_ano)}**.")
print(f"Total de linhas no novo DataFrame: {len(df_ultimos_10_anos)}")
print("\nPrimeiras 5 linhas do DataFrame filtrado:")
print(df_ultimos_10_anos.head())


# Questão 4
# ==============================================================================
print("\n" + "="*50)
print("QUESTÃO 4: Gráfico de Séries Sobreposto")
print("="*50)

df_ultimos_10_anos['DataCompleta'] = pd.to_datetime(
    df_ultimos_10_anos[['Year', 'Month']].assign(Day=1)
)

plt.figure(figsize=(14, 7))
plt.plot(
    df_ultimos_10_anos['DataCompleta'],
    df_ultimos_10_anos['Tmax'],
    label='Temperatura Máxima (Evolução Contínua)',
    color='darkred',
    linewidth=1.5
)
plt.title(
    f'Evolução Contínua da Temperatura Máxima em Londres ({int(ano_inicio)} - {int(ultimo_ano)})',
    fontsize=16
)
plt.xlabel('Ano', fontsize=12)
plt.ylabel('Temperatura Máxima (°C)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y'))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# Questão 5
# ==============================================================================
print("\n" + "="*50)
print("QUESTÃO 5: Gráfico Sobreposto")
print("="*50)

anos_unicos = df_ultimos_10_anos['Year'].unique()
num_anos = len(anos_unicos)
cores = cm.get_cmap('tab10', num_anos)
marcadores = ['o', 's', 'D', '^', 'v', 'p', '*', 'h', '+', 'x']

plt.figure(figsize=(14, 8))

for i, ano in enumerate(anos_unicos):
    df_ano = df_ultimos_10_anos[df_ultimos_10_anos['Year'] == ano]

    plt.plot(
        df_ano['Month'],
        df_ano['Tmax'],
        label=f'Ano {int(ano)}',
        color=cores(i),
        marker=marcadores[i % len(marcadores)],
        linestyle='-',
        linewidth=2,
        alpha=0.8
    )

plt.title(
    'Temperaturas Máximas Mensais Sobrepostas (Cor e Marcador por Ano)', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Temperatura Máxima (°C)', fontsize=12)
plt.xticks(np.arange(1, 13),
           ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'])
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(title='Anos', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout(rect=[0, 0, 0.85, 1])
plt.show()


# Questão 7
# ==============================================================================
print("\n" + "="*50)
print("QUESTÃO 7: Gráfico com Anotação do Pico de Temperatura Máxima")
print("="*50)

max_temp = df_ultimos_10_anos['Tmax'].max()
pico = df_ultimos_10_anos[df_ultimos_10_anos['Tmax'] == max_temp].iloc[0]

data_pico = pico['DataCompleta']
valor_pico = pico['Tmax']

mensagem = f"{valor_pico:.1f}°C é a maior temperatura registrada nos últimos 10 anos"

plt.figure(figsize=(14, 7))


plt.plot(
    df_ultimos_10_anos['DataCompleta'],
    df_ultimos_10_anos['Tmax'],
    label='Temperatura Máxima (Evolução Contínua)',
    color='darkred',
    linewidth=1.5
)


plt.annotate(
    mensagem,
    xy=(data_pico, valor_pico),
    xytext=(data_pico - pd.Timedelta(days=500), valor_pico + 5),
    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5),
    ha='center'
)


plt.title(
    f'Evolução Contínua da Temperatura Máxima em Londres (2010 - 2019) com Destaque no Pico',
    fontsize=16
)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Temperatura Máxima (°C)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y'))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# Questão 8
# ==============================================================================
print("\n" + "="*50)
print("QUESTÃO 8: Temperaturas Máximas Mensais")
print("="*50)

primeiro_ano = df_weather['Year'].min()
anos_analise = range(primeiro_ano, primeiro_ano + 10)

print(
    f"Analisando a primeira década registrada: {primeiro_ano} a {primeiro_ano + 9}")

df_primeiros_10_anos = df_weather[df_weather['Year'].isin(anos_analise)].copy()

df_primeiros_10_anos['DataCompleta'] = pd.to_datetime(
    df_primeiros_10_anos[['Year', 'Month']].assign(Day=1)
)

df_primeiros_10_anos['Mês_Nome'] = df_primeiros_10_anos['DataCompleta'].dt.strftime(
    '%b')
df_primeiros_10_anos['Mês_Num'] = df_primeiros_10_anos['DataCompleta'].dt.month

df_plot_8 = df_primeiros_10_anos.sort_values(by=['Year', 'Mês_Num'])

anos_unicos_primeiros = df_plot_8['Year'].unique()
num_anos_primeiros = len(anos_unicos_primeiros)

cores_primeiros = cm.get_cmap('tab10', num_anos_primeiros)
marcadores = ['o', 's', 'D', '^', 'v', 'p', '*', 'h', '+', 'x']

plt.figure(figsize=(12, 6))

for i, ano in enumerate(anos_unicos_primeiros):
    df_ano = df_plot_8[df_plot_8['Year'] == ano]
    plt.plot(
        df_ano['Mês_Nome'],
        df_ano['Tmax'],
        marker=marcadores[i % len(marcadores)],
        markersize=5,
        linestyle='-',
        linewidth=1.5,
        color=cores_primeiros(i),
        label=f'Ano {int(ano)}'
    )

plt.title(
    f'Temperaturas Máximas Mensais Sobrepostas (Primeiros 10 Anos: {primeiro_ano} - {primeiro_ano + 9})',
    fontsize=16
)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Temperatura Máxima (°C)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(title='Anos', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# EXERCICIO 2
# ==============================================================================
# ==============================================================================
print("\n" + "="*50)
print("EXERCÍCIO 2, QUESTÃO 1: Gráfico de Bolhas (SEMELHANTE AO EXEMPLO)")
print("="*50)

x_mes = df_weather['Month']
y_tmax = df_weather['Tmax']


tamanho_bolha_constante = 100


def get_grupo_cor(row):
    if row['Tmax'] > 20 and (row['Month'] >= 6 and row['Month'] <= 8):
        return 'Muito Quente Verão'
    elif row['Tmax'] < 10 and (row['Month'] <= 3 or row['Month'] >= 11):
        return 'Muito Frio Inverno'
    elif row['Tmax'] >= 10 and row['Tmax'] <= 20 and (row['Month'] >= 4 and row['Month'] <= 5):
        return 'Moderado Primavera'
    else:
        return 'Outros'


df_weather['GrupoCor'] = df_weather.apply(get_grupo_cor, axis=1)


cor_mapa = {
    'Muito Quente Verão': '#FF6347',
    'Muito Frio Inverno': '#66CDAA',
    'Moderado Primavera': '#4682B4',
    'Outros': '#9370DB'
}
cores_para_plot = df_weather['GrupoCor'].map(cor_mapa)


plt.figure(figsize=(10, 7))

scatter = plt.scatter(
    x=x_mes,
    y=y_tmax,
    s=tamanho_bolha_constante,
    c=cores_para_plot,
    alpha=0.8,
    edgecolors='black',
    linewidth=0.8
)


meses_labels = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai',
                'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
plt.xticks(np.arange(1, 13), meses_labels)

plt.title('Temperatura Máxima Mensal por Mês (1957-2019) - Agrupado', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Temperatura Máxima (°C)', fontsize=12)


handles = [plt.Line2D([0], [0], marker='o', color='w', label=label,
                      markerfacecolor=cor_mapa[label], markersize=10, markeredgecolor='black')
           for label in cor_mapa]
plt.legend(handles=handles, title='Grupos de Clima')


plt.grid(True, linestyle='--', alpha=0.4)

plt.tight_layout()
plt.show()
