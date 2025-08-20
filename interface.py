from testes import executar_teste

def exibir_menu():
    """
    Exibe o menu principal do programa.
    """
    print("\n" + "="*60)
    print("🚗 ALGORITMO DE PARADAS MÍNIMAS - CASOS DE TESTE")
    print("="*60)
    print("Escolha um caso de teste:")
    print("1. Caso trivial (viagem sem paradas)")
    print("2. Caso impossível")
    print("3. Caso com múltiplos postos possíveis (guloso funcionando)")
    print("4. Caso com excesso de postos (escolha mínima de paradas)")
    print("5. Teste de desempenho (escala grande)")
    print("0. Sair")
    print("-"*60)

def obter_opcao_usuario():
    """
    Obtém e valida a opção escolhida pelo usuário.
    
    Returns:
        int: opção válida escolhida pelo usuário
    """
    while True:
        try:
            opcao = int(input("Digite sua opção (0-5): "))
            if 0 <= opcao <= 5:
                return opcao
            else:
                print("❌ Opção inválida! Digite um número entre 0 e 5.")
        except ValueError:
            print("❌ Entrada inválida! Digite um número.")

def menu_principal():
    """
    Menu principal para seleção dos casos de teste.
    """
    while True:
        exibir_menu()
        
        opcao = obter_opcao_usuario()
        
        if opcao == 0:
            print("👋 Saindo do programa...")
            break
        else:
            executar_teste(opcao)
        
        input("\nPressione ENTER para continuar...")
