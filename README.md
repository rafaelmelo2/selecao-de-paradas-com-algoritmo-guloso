# 🚗 Algoritmo de Paradas Mínimas

## 📋 Descrição

Este projeto implementa um **algoritmo guloso** para resolver o **problema do caminhoneiro** - encontrar o número mínimo de paradas necessárias para abastecimento em uma viagem.

## 🏗️ Estrutura do Projeto

```
Trabalho 3/
├── app.py              # Arquivo principal (ponto de entrada)
├── algoritmo.py        # Implementação do algoritmo guloso
├── testes.py           # Casos de teste e execução
├── interface.py        # Interface do usuário e menu
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

1. **Caso Trivial**: Viagem sem paradas necessárias
2. **Caso Impossível**: Viagem que não pode ser completada
3. **Algoritmo Guloso**: Múltiplos postos possíveis
4. **Escolha Mínima**: Excesso de postos, escolha otimizada
5. **Teste de Desempenho**: Escala grande para demonstrar O(n)

## 🚀 Como Executar

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
5. Teste de desempenho (escala grande)
0. Sair
------------------------------------------------------------
Digite sua opção (0-5): 3
```

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
