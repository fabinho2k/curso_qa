import pandas as pd

dados = {
    "nome": ["Fabio", "Grazy", "Patricia"],
    "idade": [29, 52, 30],
    "cidade": ['Ilhabela', 'São Sebastião', 'Caragua']
}

df = pd.DataFrame(dados)

df_ilhabela = df[df["cidade"]=="Ilhabela"]
print(df_ilhabela)