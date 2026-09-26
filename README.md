# Projeto Final - Estrutura de Dados
 
Sistema de cadastro de reserva de estudantes com três perfis de usuários (Secretário, Diretor e Assistente), utilizando diferentes estruturas de dados em memória.
 
## Estruturas Utilizadas
 
- **Lista Encadeada Simples (`lista_encadeada.py`):** Utilizada nas operações do Secretário para cadastro dinâmico na lista de espera.
- **Árvore Binária de Busca - BST (`arvore_binaria.py`):** Utilizada pelo Diretor para busca, ordenação alfabética (mínimo e máximo), edição e remoção de registros.
- **Grafo Ponderado e Não-Direcionado (`grafo.py`):** Carregado a partir do arquivo `cidades_vizinhas.csv`, com o algoritmo de Dijkstra implementado para calcular menores distâncias e rotas a partir da escola (Guarujá) para o Assistente.
 
## Arquivos do Projeto
 
- `main.py`: Interface de linha de comando com menus e validações de entrada.
- `atribuicoes_secretario.py`: Camada de ligação entre o menu e a Lista Encadeada.
- `atribuicoes_diretor.py`: Camada de ligação entre o menu e a Árvore Binária.
- `atribuicoes_assistente.py`: Camada de ligação entre o menu e o Grafo/Dijkstra.
- `cidades_vizinhas.csv`: Base de dados de conexões e distâncias entre cidades.
 
## Como Executar
 
Execute o arquivo principal no terminal:
 
```bash
python3 main.py