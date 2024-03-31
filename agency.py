#Este script configura uma agência automatizada onde diferentes agentes colaboram para criar, gerenciar e publicar anúncios no Facebook. 
#Ele demonstra a flexibilidade do framework Agency Swarm em modelar operações complexas de marketing digital, utilizando agentes 
#especializados para diferentes tarefas. A inclusão de uma interface Gradio na execução principal permite visualizar e interagir com o 
#processo de maneira simplificada, tornando o sistema acessível até para quem não tem experiência profunda em programação.


# Importa a classe central Agency e os agentes específicos do framework Agency Swarm.
from agency_swarm import Agency  # Classe que coordena a interação entre diferentes agentes.
from FacebookManagerAgent import FacebookManagerAgent  # Agente responsável por gerenciar as postagens de anúncios no Facebook.
from ImageCreatorAgent import ImageCreatorAgent  # Agente encarregado de gerar imagens para os anúncios.
from AdCopyAgent import AdCopyAgent  # Agente especializado na criação de copy para anúncios.
from MetaMarkCEO import MetaMarkCEO  # Agente que atua como o supervisor ou CEO da operação de marketing.

# Importa a função load_dotenv do módulo dotenv, que é usada para carregar variáveis de ambiente de um arquivo .env.
from dotenv import load_dotenv
load_dotenv()  # Carrega as variáveis de ambiente definidas no arquivo .env.

# Instancia cada um dos agentes definidos, criando objetos que representam suas funcionalidades específicas.
ceo = MetaMarkCEO()  # Cria uma instância do agente CEO, que supervisiona toda a operação.
adCopyAgent = AdCopyAgent()  # Cria uma instância do agente de criação de textos para anúncios.
imageCreatorAgent = ImageCreatorAgent()  # Cria uma instância do agente de criação de imagens.
facebookManagerAgent = FacebookManagerAgent()  # Cria uma instância do agente de gerenciamento de anúncios no Facebook.

# Cria uma instância da agência, definindo a colaboração entre os agentes e passando instruções compartilhadas.
agency = Agency([
                  ceo, facebookManagerAgent,  # Define uma colaboração direta entre o CEO e o gerenciador do Facebook.
                 [ceo, adCopyAgent],  # Define uma colaboração entre o CEO e o agente de texto de anúncios.
                 [adCopyAgent, imageCreatorAgent],  # Estabelece uma colaboração entre o agente de copy e o de imagens.
                 [ceo, facebookManagerAgent],  # Repete a colaboração direta para enfatizar a gestão contínua.
                 [ceo, imageCreatorAgent]],  # Define uma colaboração entre o CEO e o agente de criação de imagens.
                shared_instructions='./agency_manifesto.md')  # Caminho para um arquivo com instruções compartilhadas.

# Verifica se este script é o módulo principal sendo executado.
if __name__ == '__main__':
    agency.demo_gradio()  # Executa uma demonstração da agência usando Gradio, uma biblioteca para criar interfaces web.

