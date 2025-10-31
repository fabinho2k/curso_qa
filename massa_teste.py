from faker import Faker
import pandas as pd

fake = Faker("pt_BR")

def dados_fake():
    dados = []
    for i in range(10):
        nome = fake.name()
        nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
        idade = 2025 - nascimento.year
        cidade = fake.city()

        dados.append({
            "nome": nome,
            "idade": idade,
            "cidade": cidade
        })
    
    df = pd.DataFrame(dados)
    df.to_csv('dados_fake.csv', index=False, encoding='utf-8')

    return(dados)    

dados_fake()
print('Dados criados com sucesso!')

