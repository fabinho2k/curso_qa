
#Código feito com ajuda de IA

def simular_catraca_juntofit():
    """
    Simula a lógica da catraca para a promoção "Treina Junto" da JUNTOFIT.
    """
    
    # Variável para rastrear os dias seguidos que o aluno veio
    dias_consecutivos = 0
    
    # O limite para ganhar a promoção
    LIMITE_PROMOCAO = 21

    print("--- 🏋️ BEM-VINDO À JUNTOFIT 🏋️ ---")
    print("Simulador da 'Promo Treina Junto'")
    print("---------------------------------------")

    # O programa fica rodando (em loop) para simular os dias passando
    while True:
        print("\nEscolha a ação do aluno:")
        print("  [1] Aluno passou na catraca (check-in de hoje)")
        print("  [2] Aluno faltou ontem (ou antes) e voltou hoje")
        print("  [0] Desligar sistema")
        
        escolha = input("Digite a opção: ")

        # --- Lógica Principal ---

        if escolha == '1':
            # O aluno veio. Incrementamos a contagem.
            dias_consecutivos += 1
            
            if dias_consecutivos == LIMITE_PROMOCAO:
                # CENÁRIO 2: Atingiu o limite
                print("\n***************************************************************************")
                print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ")
                print("***************************************************************************")
                # Reseta a contagem após ganhar
                dias_consecutivos = 0
            else:
                # CENÁRIO 1: Participando normalmente
                print(f"\n> VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO (Dia {dias_consecutivos})")

        elif escolha == '2':
            # CENÁRIO 3: O aluno quebrou a sequência
            print("\n> QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
            
            # A contagem reinicia, e o dia de hoje conta como o primeiro
            dias_consecutivos = 1
            print(f"> (Contagem atual: {dias_consecutivos} dia)")

        elif escolha == '0':
            # Sai do loop
            print("\nSistema desligado. Até logo!")
            break
            
        else:
            # Opção inválida
            print("\nOpção inválida. Tente novamente.")

# --- Para executar o programa ---
simular_catraca_juntofit()