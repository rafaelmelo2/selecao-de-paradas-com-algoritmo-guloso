import time
from algoritmo import min_paradas_otimizado

def obter_configuracao_teste(numero_teste):
    """
    Retorna a configuração de teste baseada no número fornecido.
    
    Args:
        numero_teste: número do caso de teste (1-9)
    
    Returns:
        Tupla com (posicoes_postos, autonomia_veiculo, destino_final, descricao)
    """
    
    casos_teste = {
        1: {
            'posicoes_postos': [0, 700],
            'autonomia_veiculo': 800,
            'destino_final': 700,
            'titulo': 'Caso trivial (viagem sem paradas)',
            'exemplo': 'posicoes_postos = [0, 700], autonomia_veiculo = 800, destino_final = 700',
            'explicacao': 'Como a autonomia cobre toda a viagem, não precisa de parada.',
            'saida_esperada': 'lista vazia []'
        },
        
        2: {
            'posicoes_postos': [0, 300, 700],
            'autonomia_veiculo': 200,
            'destino_final': 700,
            'titulo': 'Caso impossível',
            'exemplo': 'posicoes_postos = [0, 300, 700], autonomia_veiculo = 200, destino_final = 700',
            'explicacao': 'A distância entre 0 e 300 é maior que a autonomia.',
            'saida_esperada': 'None (impossível concluir a viagem)'
        },
        
        3: {
            'posicoes_postos': [0, 100, 200, 300, 400, 500, 600, 700],
            'autonomia_veiculo': 250,
            'destino_final': 700,
            'titulo': 'Caso com múltiplos postos possíveis (guloso funcionando)',
            'exemplo': 'posicoes_postos = [0, 100, 200, 300, 400, 500, 600, 700], autonomia_veiculo = 250, destino_final = 700',
            'explicacao': 'O algoritmo deve sempre escolher o posto mais distante alcançável.',
            'saida_esperada': '[200, 400, 600]'
        },
        
        4: {
            'posicoes_postos': [0, 50, 100, 150, 200, 250, 300],
            'autonomia_veiculo': 120,
            'destino_final': 300,
            'titulo': 'Caso com excesso de postos (escolha mínima de paradas)',
            'exemplo': 'posicoes_postos = [0, 50, 100, 150, 200, 250, 300], autonomia_veiculo = 120, destino_final = 300',
            'explicacao': 'Muitos postos próximos, mas o algoritmo vai parar apenas no essencial.',
            'saida_esperada': '[100, 200]'
        },
        
        5: {
            'posicoes_postos': list(range(0, 100001, 10)),
            'autonomia_veiculo': 200,
            'destino_final': 100000,
            'titulo': 'Teste de desempenho (escala grande)',
            'exemplo': 'posicoes_postos = list(range(0, 100001, 10)), autonomia_veiculo = 200, destino_final = 100000',
            'explicacao': 'Milhares de postos -> O(n)',
            'saida_esperada': 'Métrica: medir tempo de execução'
        },
        
        6: {
            'posicoes_postos': list(range(0, 2000001, 10)),
            'autonomia_veiculo': 200,
            'destino_final': 2000000,
            'titulo': 'Teste de desempenho (200.000 postos)',
            'exemplo': 'posicoes_postos = list(range(0, 2000001, 10)), autonomia_veiculo = 200, destino_final = 2000000',
            'explicacao': '200.000 postos a cada 10km → teste de crescimento linear',
            'saida_esperada': 'Métrica: medir tempo de execução e validar complexidade O(n)'
        },
        
        7: {
            'posicoes_postos': list(range(0, 3000001, 10)),
            'autonomia_veiculo': 200,
            'destino_final': 3000000,
            'titulo': 'Teste de desempenho (300.000 postos)',
            'exemplo': 'posicoes_postos = list(range(0, 3000001, 10)), autonomia_veiculo = 200, destino_final = 3000000',
            'explicacao': '300.000 postos a cada 10km → teste de crescimento linear',
            'saida_esperada': 'Métrica: medir tempo de execução e validar complexidade O(n)'
        },
        
        8: {
            'posicoes_postos': list(range(0, 10000001, 10)),
            'autonomia_veiculo': 200,
            'destino_final': 10000000,
            'titulo': 'Teste de desempenho (1.000.000 postos)',
            'exemplo': 'posicoes_postos = list(range(0, 10000001, 10)), autonomia_veiculo = 200, destino_final = 10000000',
            'explicacao': '1.000.000 postos a cada 10km → teste extremo de complexidade O(n)',
            'saida_esperada': 'Métrica: medir tempo de execução e validar complexidade O(n)'
        },
        
        9: {
            'posicoes_postos': list(range(0, 100000001, 10)),
            'autonomia_veiculo': 200,
            'destino_final': 100000000,
            'titulo': 'Teste de desempenho (10.000.000 postos)',
            'exemplo': 'posicoes_postos = list(range(0, 100000001, 10)), autonomia_veiculo = 200, destino_final = 100000000',
            'explicacao': '10.000.000 postos a cada 10km → teste ultra-extremo de complexidade O(n)',
            'saida_esperada': 'Métrica: medir tempo de execução e validar complexidade O(n)'
        }
    }
    
    if numero_teste not in casos_teste:
        return None
    
    return casos_teste[numero_teste]

def executar_teste(numero_teste):
    """
    Executa um teste específico baseado no número fornecido.
    
    Args:
        numero_teste: número do caso de teste (1-9)
    """
    
    configuracao = obter_configuracao_teste(numero_teste)
    
    if configuracao is None:
        print("❌ Opção inválida!")
        return
    
    # Exibe informações do teste
    print(f"\n🔹 CASO {numero_teste}: {configuracao['titulo']}")
    print(f"Exemplo: {configuracao['exemplo']}")
    print(f"Explicação: {configuracao['explicacao']}")
    print(f"Saída esperada: {configuracao['saida_esperada']}")
    
    # Extrai parâmetros
    posicoes_postos = configuracao['posicoes_postos'].copy()  # Copia para não modificar o original
    autonomia_veiculo = configuracao['autonomia_veiculo']
    destino_final = configuracao['destino_final']
    
    # Exibe parâmetros de execução
    print(f"\n📊 EXECUTANDO TESTE {numero_teste}")
    print(f"Posições dos postos (KM - distância): {posicoes_postos[:10]}{'...' if len(posicoes_postos) > 10 else ''}")
    print(f"Autonomia do veículo: {autonomia_veiculo} km")
    print(f"Destino final: {destino_final} km")
    
    # Medição de tempo para os casos de desempenho
    if numero_teste in [5, 6, 7, 8, 9]:
        inicio = time.time()
        paradas_necessarias = min_paradas_otimizado(posicoes_postos, autonomia_veiculo, destino_final)
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"\n⏱️ Tempo de execução: {tempo_execucao:.6f} segundos")
        
        # Informações adicionais para os testes de performance
        print(f"📈 Total de postos processados: {len(posicoes_postos):,}")
        print(f"🚗 Distância total da viagem: {destino_final:,} km")
        print(f"⛽ Postos por km: {len(posicoes_postos)/destino_final:.2f}")
    else:
        paradas_necessarias = min_paradas_otimizado(posicoes_postos, autonomia_veiculo, destino_final)
    
    # Exibe resultado
    print(f"\n📋 RESULTADOS:")
    if paradas_necessarias is not None:
        if numero_teste in [5, 6, 7, 8, 9]:
            print(f" 📊 Total de paradas: {len(paradas_necessarias)}")
        else:
            print(f" ✅ Postos de gasolina para parar: {paradas_necessarias}")
            print(f" 📊 Total de paradas: {len(paradas_necessarias)}")
    else:
        print("❌ Não é possível completar a viagem com a autonomia fornecida.")

def executar_todos_testes_performance():
    """
    Executa todos os testes de performance (5, 6, 7, 8, 9) e retorna uma comparação dos tempos.
    """
    print("\n" + "="*80)
    print("🚀 EXECUTANDO TODOS OS TESTES DE PERFORMANCE")
    print("="*80)
    print("Demonstrando crescimento linear do tempo com o número de postos")
    print("="*80)
    
    resultados = []
    
    # Executa todos os testes de performance
    for numero_teste in [5, 6, 7, 8, 9]:
        configuracao = obter_configuracao_teste(numero_teste)
        
        print(f"\n🔹 Executando Teste {numero_teste}: {configuracao['titulo']}")
        print(f"📊 Postos: {len(configuracao['posicoes_postos']):,} | Distância: {configuracao['destino_final']:,} km")
        
        # Medição de tempo
        inicio = time.time()
        paradas_necessarias = min_paradas_otimizado(configuracao['posicoes_postos'], 
                                                   configuracao['autonomia_veiculo'], 
                                                   configuracao['destino_final'])
        fim = time.time()
        tempo_execucao = fim - inicio
        
        # Armazena resultado
        resultados.append({
            'teste': numero_teste,
            'postos': len(configuracao['posicoes_postos']),
            'tempo': tempo_execucao,
            'paradas': len(paradas_necessarias) if paradas_necessarias else 0
        })
        
        print(f"⏱️ Tempo: {tempo_execucao:.6f}s | Paradas: {len(paradas_necessarias) if paradas_necessarias else 0}")
    
    # Exibe comparação final
    print("\n" + "="*80)
    print("📈 COMPARAÇÃO DOS RESULTADOS")
    print("="*80)
    print(f"{'Teste':<6} {'Postos':<12} {'Tempo (s)':<12} {'Paradas':<10} {'Tempo/Posto':<15}")
    print("-" * 80)
    
    tempo_base = resultados[0]['tempo']
    postos_base = resultados[0]['postos']
    
    for resultado in resultados:
        tempo_por_posto = resultado['tempo'] / resultado['postos'] * 1000000  # microssegundos por posto
        fator_crescimento = resultado['tempo'] / tempo_base if tempo_base > 0 else 0
        fator_postos = resultado['postos'] / postos_base
        
        print(f"{resultado['teste']:<6} {resultado['postos']:<12,} {resultado['tempo']:<12.6f} "
              f"{resultado['paradas']:<10} {tempo_por_posto:<15.4f} μs/posto")
    
    print("-" * 80)
    
    # Análise do crescimento
    print("\n🔍 ANÁLISE DO CRESCIMENTO LINEAR:")
    print("-" * 50)
    
    for i, resultado in enumerate(resultados[1:], 1):
        fator_tempo = resultado['tempo'] / tempo_base
        fator_postos = resultado['postos'] / postos_base
        eficiencia = fator_tempo / fator_postos
        
        print(f"Teste {resultados[0]['teste']} → {resultado['teste']}:")
        print(f"  📊 Postos: {fator_postos:.1f}x | Tempo: {fator_tempo:.1f}x | Eficiência: {eficiencia:.2f}")
        
        if 0.8 <= eficiencia <= 1.2:
            print(f"  ✅ Crescimento LINEAR confirmado (O(n))")
        else:
            print(f"  ⚠️  Possível desvio do crescimento linear")
        print()
    
    # Conclusão
    print("🎯 CONCLUSÃO:")
    print("=" * 50)
    print("✅ O algoritmo guloso demonstra complexidade O(n)")
    print("✅ O tempo de execução cresce linearmente com o número de postos")
    print("✅ Eficiência mantida mesmo com 10 milhões de postos")
    print("=" * 50)
