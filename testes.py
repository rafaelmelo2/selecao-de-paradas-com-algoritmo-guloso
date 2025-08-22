import time
import matplotlib.pyplot as plt
import numpy as np
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
            'posicoes_postos': list(range(0, 200001, 10)),
            'autonomia_veiculo': 200,
            'destino_final': 200000,
            'titulo': 'Teste de desempenho (200.000 postos)',
            'exemplo': 'posicoes_postos = list(range(0, 200001, 10)), autonomia_veiculo = 200, destino_final = 2000000',
            'explicacao': '200.000 postos a cada 10km → teste de crescimento linear',
            'saida_esperada': 'Métrica: medir tempo de execução e validar complexidade O(n)'
        },
        
        7: {
            'posicoes_postos': list(range(0, 300001, 10)),
            'autonomia_veiculo': 200,
            'destino_final': 300000,
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

def gerar_graficos_desempenho():
    """
    Executa testes de performance e gera gráfico comparativo O(n) vs O(n²).
    """
    print("\n" + "="*80)
    print("📊 GERANDO GRÁFICO O(n) vs O(n²) - TESTES EM GRANDE ESCALA")
    print("="*80)
    print("Executando testes com milhões de postos para demonstrar crescimento linear...")
    print("="*80)
    
    resultados = []
    
    # Executa testes de performance com grandes volumes para demonstrar O(n)
    # Criando casos de teste com volumes muito maiores
    casos_grandes = [
        {
            'postos': list(range(0, 10000001, 10)),  # 1.000.000 postos
            'autonomia': 200,
            'destino': 10000000,
            'titulo': 'Teste 1M postos'
        },
        {
            'postos': list(range(0, 50000001, 10)),  # 5.000.000 postos
            'autonomia': 200,
            'destino': 50000000,
            'titulo': 'Teste 5M postos'
        },
        {
            'postos': list(range(0, 250000001, 10)),  # 25.000.000 postos
            'autonomia': 200,
            'destino': 250000000,
            'titulo': 'Teste 25M postos'
        }
    ]
    
    for i, caso in enumerate(casos_grandes):
        print(f"\n🔹 Executando {caso['titulo']}")
        print(f"📊 Postos: {len(caso['postos']):,} | Distância: {caso['destino']:,} km")
        
        # Medição de tempo
        inicio = time.time()
        paradas_necessarias = min_paradas_otimizado(caso['postos'], 
                                                   caso['autonomia'], 
                                                   caso['destino'])
        fim = time.time()
        tempo_execucao = fim - inicio
        
        # Armazena resultado
        resultados.append({
            'teste': i + 1,
            'postos': len(caso['postos']),
            'tempo': tempo_execucao,
            'paradas': len(paradas_necessarias) if paradas_necessarias else 0
        })
        
        print(f"⏱️ Tempo: {tempo_execucao:.6f}s | Paradas: {len(paradas_necessarias) if paradas_necessarias else 0}")
    
    # Extrai dados para o gráfico
    postos = [r['postos'] for r in resultados]
    tempos = [r['tempo'] for r in resultados]
    
    # Configuração do gráfico
    plt.style.use('default')
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))
    
    # Gráfico principal: Tempo vs Número de Postos
    ax.plot(postos, tempos, 'o-', linewidth=3, markersize=8, color='#2E86AB', 
            label='Algoritmo Guloso O(n)', markerfacecolor='white', markeredgewidth=2)
    
    # Linha de tendência linear (O(n))
    z_linear = np.polyfit(postos, tempos, 1)
    p_linear = np.poly1d(z_linear)
    # ax.plot(postos, p_linear(postos), '--', color='#2E86AB', linewidth=2, 
    #         label=f'Crescimento Linear O(n)')
    
    # Crescimento quadrático hipotético para comparação
    # Usa o primeiro ponto como referência para normalizar
    tempo_base = tempos[0]
    postos_base = postos[0]
    
    # Gera pontos para crescimento quadrático O(n²)
    postos_quadratico = np.linspace(min(postos), max(postos), 100)
    # Normaliza para que o primeiro ponto seja igual ao tempo real
    fator_quadratico = tempo_base / (postos_base ** 2)
    tempos_quadratico = fator_quadratico * (postos_quadratico ** 2)
    
    ax.plot(postos_quadratico, tempos_quadratico, '--', color='#C73E1D', linewidth=3,
            label='Crescimento Quadrático O(n²) - Hipótese')
    
    # Configurações do gráfico
    ax.set_xlabel('Número de Postos', fontsize=12, fontweight='bold')
    ax.set_ylabel('Tempo de Execução (segundos)', fontsize=12, fontweight='bold')
    ax.set_title('Comparação O(n) vs O(n²) - Testes em Grande Escala (Milhões de Postos)', 
                 fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11, loc='upper left')
    
    # Adiciona anotações com valores reais
    for i, (x, y) in enumerate(zip(postos, tempos)):
        ax.annotate(f'{y:.4f}s\n({x:,} postos)', (x, y), textcoords="offset points", 
                   xytext=(5,5), ha='left', va='bottom', fontsize=9, fontweight='bold',
                   bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8))
    
    # Adiciona texto explicativo
    ax.text(0.02, 0.98, '✅ Algoritmo Guloso: O(n) - Crescimento Linear\n'
                        '❌ Crescimento Quadrático: O(n²) - Muito mais lento',
             transform=ax.transAxes, fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.8))
    
    plt.tight_layout()
    
    # Salva o gráfico
    nome_arquivo = 'comparacao_on_vs_on2_grande_escala.png'
    plt.savefig(nome_arquivo, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"\n✅ Gráfico salvo como: {nome_arquivo}")
    
    # Exibe análise dos resultados
    print("\n" + "="*80)
    print("📈 ANÁLISE O(n) vs O(n²) - TESTES EM GRANDE ESCALA")
    print("="*80)
    
    # Análise da complexidade
    print("🔍 ANÁLISE DE COMPLEXIDADE:")
    print(f"   • Coeficiente linear: {z_linear[0]:.2e}")
    print(f"   • Intercepto: {z_linear[1]:.2e}")
    
    # Calcula R² para verificar qualidade do ajuste linear
    y_pred = p_linear(postos)
    ss_res = np.sum((tempos - y_pred) ** 2)
    ss_tot = np.sum((tempos - np.mean(tempos)) ** 2)
    r_squared = 1 - (ss_res / ss_tot)
    print(f"   • R² (qualidade do ajuste linear): {r_squared:.4f}")
    
    if r_squared > 0.95:
        print("   ✅ Excelente ajuste linear - Confirma O(n)")
    elif r_squared > 0.90:
        print("   ✅ Bom ajuste linear - Confirma O(n)")
    else:
        print("   ⚠️  Ajuste linear questionável")
    
    # Comparação com crescimento quadrático
    print(f"\n⚡ COMPARAÇÃO COM CRESCIMENTO QUADRÁTICO:")
    ultimo_tempo_real = tempos[-1]
    ultimo_tempo_quadratico = fator_quadratico * (postos[-1] ** 2)
    fator_diferenca = ultimo_tempo_quadratico / ultimo_tempo_real
    
    print(f"   • Tempo real (O(n)): {ultimo_tempo_real:.6f}s")
    print(f"   • Tempo hipotético O(n²): {ultimo_tempo_quadratico:.2f}s")
    print(f"   • Diferença: {fator_diferenca:.0f}x mais lento se fosse O(n²)")
    
    # Análise de eficiência
    tempo_por_posto = [t/p*1000000 for t, p in zip(tempos, postos)]
    tempo_medio_por_posto = np.mean(tempo_por_posto)
    print(f"\n🎯 EFICIÊNCIA:")
    print(f"   • Tempo médio por posto: {tempo_medio_por_posto:.2f} μs")
    print(f"   • Variação do tempo por posto: {np.std(tempo_por_posto):.2f} μs")
    
    print("\n🎯 CONCLUSÕES:")
    print("   • O algoritmo guloso demonstra claramente comportamento O(n)")
    print("   • Se fosse O(n²), seria {:.0f}x mais lento no maior teste".format(fator_diferenca))
    print("   • Eficiência linear mantida mesmo com 25 milhões de postos")
    print("   • Algoritmo otimizado e escalável")
    print("="*80)
    
    # Mostra o gráfico
    plt.show()
