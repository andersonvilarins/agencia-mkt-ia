"""
Este agente é projetado para automatizar a criação de textos publicitários, aproveitando a inteligência artificial para gerar conteúdo 
que se alinha às necessidades do público-alvo e às características destacadas do produto ou serviço. A classe não especifica ferramentas 
internas (tools=[]), o que sugere que depende de ferramentas externas ou adicionadas posteriormente para executar suas tarefas. 
O uso de diretórios para arquivos, esquemas e ferramentas indica uma estrutura organizada para recursos e dados que o agente pode necessitar 
durante sua operação.
"""

# Importa a classe base Agent de agency_swarm.agents, usada para criar agentes com funções específicas.
from agency_swarm.agents import Agent

# Define a classe AdCopyAgent, que herda da classe base Agent.
class AdCopyAgent(Agent):
    # Método construtor para inicializar uma nova instância do AdCopyAgent.
    def __init__(self):
        # Chama o construtor da classe base (Agent) com parâmetros específicos deste agente.
        super().__init__(
            name="AdCopyAgent",  # Nome do agente, usado para identificação.
            description="""É especializado na geração de textos de anúncios criativos e envolventes usando ferramentas de IA. 
                           Avalia o público-alvo e as características do produto/serviço para criar mensagens atraentes.""",  # Descrição do propósito e especialização do agente.
            instructions="./instructions.md",  # Caminho para um arquivo de instruções que detalha como o agente deve ser usado.
            files_folder="./files",  # Diretório onde os arquivos manipulados pelo agente são armazenados.
            schemas_folder="./schemas",  # Diretório para esquemas de dados usados pelo agente.
            tools=[],  # Lista de ferramentas (instâncias de BaseTool ou derivadas) que o agente pode usar para realizar suas tarefas.
            tools_folder="./tools"  # Diretório onde as definições de ferramentas específicas do agente são armazenadas.
        )
