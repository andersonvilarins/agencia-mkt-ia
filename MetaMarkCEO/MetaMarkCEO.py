"""

Este script introduz o MetaMarkCEO como uma entidade central no controle e supervisão das atividades dentro do ecossistema de automação
de marketing Agency Swarm. Atuando como um CEO, este agente é crucial para iniciar o processo de campanhas publicitárias e para garantir 
que os diversos agentes especializados (como geradores de texto de anúncio, criadores de imagem e gerenciadores de publicação de anúncios) 
colaborem de maneira eficaz e coordenada.

"""

# Importa a classe base Agent, fundamental para a criação de qualquer agente dentro do framework "Agency Swarm".
from agency_swarm.agents import Agent

# Define a classe MetaMarkCEO, que herda da classe Agent, significando que possui todas as características e funcionalidades de um agente.
class MetaMarkCEO(Agent):
    # Método construtor para inicializar uma nova instância do MetaMarkCEO.
    def __init__(self):
        # Chamada ao construtor da superclasse, passando parâmetros que definem propriedades específicas deste agente.
        super().__init__(
            # O nome do agente, que neste caso sugere uma função de supervisão ou liderança, similar a um CEO em uma empresa.
            name="MetaMarkCEO",
            # Descrição do papel deste agente: 
            description="""
                        Supervisiona toda a operação, mantém o fluxo de trabalho entre os agentes e garante o cumprimento dos objetivos
                        da agência. Atua como supervisor estratégico e iniciador do processo de campanha publicitária.
                        """,
            # Caminho para um arquivo markdown com instruções detalhadas de operação do agente. Útil para outros desenvolvedores ou usuários do sistema.
            instructions="./instructions.md",
            # Diretório destinado ao armazenamento de arquivos que podem ser necessários durante a execução das tarefas do agente.
            files_folder="./files",
            # Diretório para armazenar esquemas de dados, que podem ser utilizados para validar as informações processadas ou geradas pelo agente.
            schemas_folder="./schemas",
            # Lista de ferramentas específicas que este agente pode utilizar em suas operações. Inicia vazia, indicando que pode ser configurada conforme a necessidade.
            tools=[],
            # Caminho para o diretório onde estão armazenadas as ferramentas específicas deste agente.
            tools_folder="./tools"
        )
