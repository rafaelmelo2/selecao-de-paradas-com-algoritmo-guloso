from testes import executar_teste, executar_todos_testes_performance

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
    print("5. Teste de desempenho (100.000 postos)")
    print("6. Teste de desempenho (200.000 postos)")
    print("7. Teste de desempenho (300.000 postos)")
    print("8. Teste de desempenho (1.000.000 postos)")
    print("9. Teste de desempenho (10.000.000 postos)")
    print("10. 🚀 EXECUTAR TODOS OS TESTES DE PERFORMANCE")
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
            opcao = int(input("Digite sua opção (0-10): "))
            if 0 <= opcao <= 10:
                return opcao
            else:
                print("❌ Opção inválida! Digite um número entre 0 e 10.")
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
        elif opcao == 10:
            executar_todos_testes_performance()
        else:
            executar_teste(opcao)
        
        input("\nPressione ENTER para continuar...")
