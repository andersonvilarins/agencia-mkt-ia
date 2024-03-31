#Este agente, ImageCreatorAgent, é especializado na criação de imagens para anúncios, aproveitando o poder da IA, especificamente a 
# versão 3 do modelo DALL-E, conhecido por sua capacidade de gerar imagens detalhadas a partir de descrições textuais. A inclusão deste
# agente no ecossistema Agency Swarm indica um esforço para automatizar não apenas a parte textual dos anúncios mas também o componente 
# visual, essencial para capturar a atenção do público e melhorar a eficácia dos anúncios.

# Importa a classe base Agent do módulo agency_swarm.agents, que serve como base para todos os agentes.
from agency_swarm.agents import Agent

# Define a classe ImageCreatorAgent, que herda da classe Agent.
class ImageCreatorAgent(Agent):
    # Método construtor da classe.
    def __init__(self):
        # Chama o construtor da classe base (Agent) para inicializar o agente com propriedades específicas.
        super().__init__(
            # Nome do agente, identificando sua função dentro do ecossistema Agency Swarm.
            name="ImageCreatorAgent",
            # Descrição do papel do agente: utilizar DALL-E 3 para gerar imagens que acompanhem o texto dos anúncios.
            description="Utiliza DALL-E 3 para gerar imagens sincronizadas com o texto do anúncio. Com a tarefa de criar gráficos visualmente atraentes que chamam a atenção e transmitem a mensagem de forma eficaz.",
            # Caminho para um arquivo markdown com instruções detalhadas sobre como o agente deve ser utilizado.
            instructions="./instructions.md",
            # Diretório destinado ao armazenamento de arquivos gerados ou utilizados pelo agente.
            files_folder="./files",
            # Diretório para armazenar esquemas de dados que o agente pode usar para validar as informações processadas.
            schemas_folder="./schemas",
            # Lista inicial de ferramentas que o agente pode utilizar em suas operações. Começa vazia, indicando que pode ser configurada posteriormente.
            tools=[],
            # Diretório onde as ferramentas específicas do agente estão ou estarão armazenadas.
            tools_folder="./tools"
        )
