# 🚗 Algoritmo de Paradas Mínimas

## 📋 Problema Resolvido

**Problema do Caminhoneiro**: Um caminhão com autonomia limitada precisa viajar de um ponto A até um ponto B, passando por diversos postos de gasolina. O objetivo é encontrar o **número mínimo de paradas** necessárias para completar a viagem.

### 🎯 Características do Problema:
- **Entrada**: Lista de posições dos postos, autonomia do veículo, destino final
- **Saída**: Lista das posições onde parar para abastecer (mínimo possível)
- **Restrição**: O caminhão não pode ficar sem combustível
- **Objetivo**: Minimizar o número total de paradas

### 💡 Solução Implementada:
**Algoritmo Guloso** que sempre escolhe o posto mais distante alcançável a partir da posição atual, garantindo a **otimalidade** da solução com **complexidade O(n)**.

## 📋 Descrição

Este projeto implementa um **algoritmo guloso** para resolver o **problema do caminhoneiro** - encontrar o número mínimo de paradas necessárias para abastecimento em uma viagem.

## 🏗️ Estrutura do Projeto

```
Trabalho 3/
├── app.py              # Arquivo principal (ponto de entrada)
├── algoritmo.py        # Implementação do algoritmo guloso
├── testes.py           # Casos de teste e execução
├── interface.py        # Interface do usuário e menu
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto
```

## 📁 Módulos

### `algoritmo.py`
- **Função**: `min_paradas_otimizado()`
- **Responsabilidade**: Implementação do algoritmo guloso
- **Complexidade**: O(n) onde n é o número de postos

### `testes.py`
- **Função**: `executar_teste()` e `obter_configuracao_teste()`
- **Responsabilidade**: Gerenciamento dos casos de teste
- **Casos incluídos**: 5 cenários diferentes de teste

### `interface.py`
- **Função**: `menu_principal()` e funções auxiliares
- **Responsabilidade**: Interface do usuário e validação de entrada

### `app.py`
- **Função**: Ponto de entrada do programa
- **Responsabilidade**: Inicialização e execução do menu principal

## 🧪 Casos de Teste

### Casos Básicos:
1. **Caso Trivial**: Viagem sem paradas necessárias
2. **Caso Impossível**: Viagem que não pode ser completada
3. **Algoritmo Guloso**: Múltiplos postos possíveis
4. **Escolha Mínima**: Excesso de postos, escolha otimizada

### Testes de Performance (Demonstração O(n)):
5. **100.000 postos**: Base de comparação
6. **200.000 postos**: 2x crescimento
7. **300.000 postos**: 3x crescimento
8. **1.000.000 postos**: 10x crescimento
9. **10.000.000 postos**: 100x crescimento
10. **🚀 Todos os Testes**: Execução automática com análise comparativa
11. **📊 Gerar Gráficos**: Criação de gráficos de desempenho

## 🚀 Como Executar

### Instalação das Dependências
```bash
pip install -r requirements.txt
```

### Execução do Programa
```bash
python app.py
```

## 📊 Exemplo de Uso

```
🚗 BEM-VINDO AO ALGORITMO DE PARADAS MÍNIMAS!
Este programa demonstra um algoritmo guloso para otimizar paradas de abastecimento.

============================================================
🚗 ALGORITMO DE PARADAS MÍNIMAS - CASOS DE TESTE
============================================================
Escolha um caso de teste:
1. Caso trivial (viagem sem paradas)
2. Caso impossível
3. Caso com múltiplos postos possíveis (guloso funcionando)
4. Caso com excesso de postos (escolha mínima de paradas)
5. Teste de desempenho (100.000 postos)
6. Teste de desempenho (200.000 postos)
7. Teste de desempenho (300.000 postos)
8. Teste de desempenho (1.000.000 postos)
9. Teste de desempenho (10.000.000 postos)
10. 🚀 EXECUTAR TODOS OS TESTES DE PERFORMANCE
11. 📊 GERAR GRÁFICOS DE DESEMPENHO
0. Sair
------------------------------------------------------------
Digite sua opção (0-11): 11
```

### 📈 Funcionalidade de Gráficos

A opção 11 executa testes de performance e gera um gráfico comparativo focado:

- **Comparação O(n) vs O(n²)**: Demonstra visualmente a eficiência do algoritmo guloso
- **Análise estatística**: Inclui R² para validar o ajuste linear
- **Comparação quantitativa**: Mostra quantas vezes seria mais lento se fosse quadrático
- **Testes em grande escala**: Usa 1M, 5M e 25M de postos para demonstrar claramente o crescimento linear O(n)

O gráfico é salvo como `comparacao_on_vs_on2_grande_escala.png` e também exibido na tela.

## 🎯 Benefícios da Modularização

- **🔧 Manutenibilidade**: Código organizado e fácil de modificar
- **🧪 Testabilidade**: Cada módulo pode ser testado independentemente
- **📚 Legibilidade**: Estrutura clara e documentada
- **🔄 Reutilização**: Módulos podem ser reutilizados em outros projetos
- **👥 Colaboração**: Múltiplos desenvolvedores podem trabalhar em módulos diferentes

## 📈 Complexidade

- **Tempo**: O(n) - onde n é o número de postos
- **Espaço**: O(1) - apenas variáveis auxiliares

## 🎓 Aplicação Acadêmica

Este projeto é ideal para:
- Demonstração de algoritmos gulosos
- Análise de complexidade
- Apresentações de algoritmos
- Estudos de otimização
