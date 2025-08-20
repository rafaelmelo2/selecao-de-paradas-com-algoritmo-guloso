import time
from algoritmo import min_paradas_otimizado

def obter_configuracao_teste(numero_teste):
    """
    Retorna a configuração de teste baseada no número fornecido.
    
    Args:
        numero_teste: número do caso de teste (1-5)
    
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
            'explicacao': 'Milhares de postos → o algoritmo ainda deve rodar rápido, mostrando que é O(n)',
            'saida_esperada': 'Métrica: medir tempo de execução'
        }
    }
    
    if numero_teste not in casos_teste:
        return None
    
    return casos_teste[numero_teste]

def executar_teste(numero_teste):
    """
    Executa um teste específico baseado no número fornecido.
    
    Args:
        numero_teste: número do caso de teste (1-5)
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
    
    # Medição de tempo para o caso de desempenho
    if numero_teste == 5:
        inicio = time.time()
        paradas_necessarias = min_paradas_otimizado(posicoes_postos, autonomia_veiculo, destino_final)
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"⏱️ Tempo de execução: {tempo_execucao:.6f} segundos")
    else:
        paradas_necessarias = min_paradas_otimizado(posicoes_postos, autonomia_veiculo, destino_final)
    
    # Exibe resultado
    print(f"\n📋 RESULTADOS:")
    if paradas_necessarias is not None:
        print(f" ✅ Postos de gasolina para parar: {paradas_necessarias}")
        print(f" 📊 Total de paradas: {len(paradas_necessarias)}")
    else:
        print("❌ Não é possível completar a viagem com a autonomia fornecida.")
