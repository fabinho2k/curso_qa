import requests

dados = [
    {
        "nome": "Fabio",
        "CEP": 11631014
    },
    {
        "nome": "Grazy",
        "CEP": 11630350
    },
    {
        "nome": "Joao",
        "CEP": 11630000
    }
]

for dado in dados:
    cep = dado["CEP"]
    nome = dado["nome"]
    url_viacep = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url_viacep)
        
    if resposta.status_code == 200:
         
         #Transformar a resposta em JSON
         dados_cep = resposta.json()
         
         # Checa se o ViaCEP retornou um erro (ex: CEP não encontrado)
         if dados_cep.get("erro"):
             print(f"Olá {nome}, não foi possível encontrar o CEP {cep}.")
         else:
             # Pega a cidade (a chave no ViaCEP é "localidade")
             cidade = dados_cep["localidade"]
             uf = dados_cep["uf"]
             print(f'Olá {nome}, sua cidade é {cidade} - {uf}')
        
    else:
        print(f"Erro ao consultar o CEP {cep} para {nome}. Status: {resposta.status_code}")