def par_ou_impar():
    print("Bem-vindo ao jogo de Par ou Ímpar!")
    
    # Escolha dos jogadores
    jogador1 = input("Jogador 1, escolha Par ou Ímpar (P/I): ").strip().upper()
    while jogador1 not in ['P', 'I']:
        jogador1 = input("Escolha inválida. Por favor, escolha Par (P) ou Ímpar (I): ").strip().upper()
    
    jogador2 = 'P' if jogador1 == 'I' else 'I'
    
    print(f"Jogador 1 escolheu {'Par' if jogador1 == 'P' else 'Ímpar'}. Jogador 2 será {'Par' if jogador2 == 'P' else 'Ímpar'}.")

    # Escolha dos números
    numero1 = int(input("Jogador 1, escolha um número: "))
    numero2 = int(input("Jogador 2, escolha um número: "))
    
    # Soma dos números
    soma = numero1 + numero2
    print(f"A soma dos números escolhidos é {soma}.")
    
    # Determinação do vencedor
    if soma % 2 == 0:
        print("A soma é Par.")
        vencedor = "Jogador 1" if jogador1 == 'P' else "Jogador 2"
    else:
        print("A soma é Ímpar.")
        vencedor = "Jogador 1" if jogador1 == 'I' else "Jogador 2"
    
    print(f"{vencedor} venceu!")

# Executar o jogo
par_ou_impar()
