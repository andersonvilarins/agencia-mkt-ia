"""
 Este agente atua como um gestor dentro do sistema de automação de anúncios, assegurando que os anúncios sejam criados e publicados 
 de maneira eficiente e eficaz, com foco na maximização do impacto e no alcance do público-alvo desejado.
"""

# Importação da classe base Agent do módulo agency_swarm.agents.
from agency_swarm.agents import Agent

# Definição da classe FacebookManagerAgent, que herda de Agent.
class FacebookManagerAgent(Agent):
    # Método construtor da classe.
    def __init__(self):
        # Chamada ao construtor da classe base (Agent) com parâmetros específicos para este agente.
        super().__init__(
            # Nome do agente, que o identifica dentro do framework "Agency Swarm".
            name="FacebookManagerAgent",
            # Descrição do propósito do agente: gerenciar agendamento e postagem de anúncios no Facebook.
            description="Cuida do agendamento e postagem dos anúncios no Facebook. Garante que cada anúncio seja publicado de acordo com as melhores práticas de tempo e segmentação de público.",
            # Caminho para um arquivo markdown com instruções de uso do agente.
            instructions="./instructions.md",
            # Diretório onde o agente pode armazenar ou acessar arquivos necessários durante sua operação.
            files_folder="./files",
            # Diretório para armazenar esquemas de dados usados pelo agente, auxiliando na validação de dados.
            schemas_folder="./schemas",
            # Lista de ferramentas que o agente pode utilizar. Inicialmente vazia, indicando que este agente pode ser configurado com ferramentas específicas mais tarde.
            tools=[],
            # Diretório onde estão localizadas as ferramentas que o agente pode usar. Isso permite uma modularidade e expansão fácil do agente.
            tools_folder="./tools"
        )
