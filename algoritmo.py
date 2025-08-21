def min_paradas_otimizado(posicoes_postos, autonomia_veiculo, destino_final):
    """
    Algoritmo guloso para encontrar o número mínimo de paradas para abastecimento.
    
    Args:
        posicoes_postos: lista das posições dos postos, incluindo 0 (início) e o destino final.
        autonomia_veiculo: capacidade máxima de combustível (distância que pode percorrer).
        destino_final: a posição do destino.
    
    Returns:
        Lista com as posições dos postos onde deve parar para abastecer, ou None se impossível.
    """
    # Adiciona o destino à lista para garantir que o algoritmo o trate como a última "parada"
    if posicoes_postos[-1] != destino_final:
        posicoes_postos.append(destino_final)

    paradas_necessarias = []
    posicao_atual_veiculo = 0  # Posição atual do veículo (começa em 0)
    indice_proximo_posto = 0  # Índice do próximo posto a ser verificado

    # O loop principal continua enquanto não atingimos o destino
    while posicao_atual_veiculo < destino_final:
        posto_mais_distante_alcancavel = posicao_atual_veiculo

        # O(n) - Esse laço interno percorre a lista de postos uma única vez no total, porque a variável indice_proximo_posto nunca volta para trás, só avança.
        while indice_proximo_posto < len(posicoes_postos) and posicoes_postos[indice_proximo_posto] <= posicao_atual_veiculo + autonomia_veiculo:
            posto_mais_distante_alcancavel = posicoes_postos[indice_proximo_posto]
            indice_proximo_posto += 1

        # Se não houver postos alcançáveis e a posição não avançou, é impossível continuar.
        if posto_mais_distante_alcancavel == posicao_atual_veiculo:
            return None

        # Se a posição do posto mais distante alcançável não é o destino, adicionamos como parada
        if posto_mais_distante_alcancavel < destino_final:
            paradas_necessarias.append(posto_mais_distante_alcancavel)

        # Atualiza a posição atual para o posto escolhido
        posicao_atual_veiculo = posto_mais_distante_alcancavel

    return paradas_necessarias
