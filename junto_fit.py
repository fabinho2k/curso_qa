
'''
lista_presença = 0
dia_do_mês = 1

while lista_presença <= 21:
    select = int(input("Seja Bem-Vindo à academia JUNTOFIT\n" \
    "Escolhe uma opção no menu: \n" 
    "1- Confirmar Entrada!\n" \
    "2- Atualizar Cadastro!\n" \
    "3- Alterar forma de pagamento!\n"))


    if select == 1:
        print(f'Sua entrada em {dia_do_mês} de outubro foi confirmada. Você está participando da nossa promo Treina Junto')
        lista_presença += 1
        dia_do_mês +=1
        print(f'Quantidade de dias seguidos: {lista_presença}')
        print('\n')

    elif select == 2:
        print('Suas informações foram atualizadas!')

    elif select == 3:
        print('Forma de pagamento alterada com sucesso!')

if lista_presença >= 21:
    print(f'Parabéns. Você teve uma frequencia de {lista_presença} dias seguidos.'\
          'Agora você pode presentear um amigo ou amiga para treinar com você')
'''
select = int(input("Seja Bem-Vindo à academia JUNTOFIT\n" \
"Informe a quantidade de dias seguidos que você frequentou a academia!: \n"))

def frequencia(qtde_dias):
    frequencia_dias = 0
    frequencia_dias += qtde_dias
    return frequencia_dias


frequencia_dias = frequencia(select)

if frequencia_dias >= 21:
    print(f'Parabéns. Você teve uma frequencia de {frequencia_dias} dias seguidos.'\
          'Agora você pode presentear um amigo ou amiga para treinar com você')
else:
    print(f'Parabéns. Você está com uma frequência de {frequencia_dias} seguidos!'\
          'Quando chegar em 21 dias seguidos, você ')
    
#Terminar em casa