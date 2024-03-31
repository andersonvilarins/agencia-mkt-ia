#Este código exemplifica como criar um conjunto de anúncios no Facebook, definindo aspectos como o nome do conjunto, orçamento, 
#público-alvo e período de veiculação. Utiliza a API do Facebook para criar o conjunto de anúncios e armazena informações relevantes 
#no estado compartilhado para uso por outras ferramentas ou etapas do processo. A estrutura do código também inclui tratamento de erros
#e validações para garantir que todas as dependências necessárias estejam presentes antes de tentar a criação do conjunto de anúncios.

# Importa as bibliotecas e módulos necessários.
from datetime import datetime, timedelta  # Usado para manipular datas e horas, como definir o período de veiculação do conjunto de anúncios.

from agency_swarm.tools import BaseTool  # Importa a classe BaseTool do framework agency_swarm, base para todas as ferramentas.
from pydantic import Field  # Importa Field do Pydantic para definir campos com validações e descrições.
import os  # Módulo do sistema operacional para interagir com o sistema de arquivos e variáveis de ambiente.
import facebook_business.exceptions  # Importa exceções específicas da API do Facebook Business para tratamento de erros.
from facebook_business.api import FacebookAdsApi  # Importa a API do Facebook Ads para inicialização e uso.
from facebook_business.adobjects.adaccount import AdAccount  # Classe para acessar contas de anúncios no Facebook.
from facebook_business.adobjects.adset import AdSet  # Classe para manipular conjuntos de anúncios.

from dotenv import load_dotenv  # Ferramenta para carregar variáveis de ambiente de um arquivo .env.
load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env.

# Obtém credenciais necessárias da API do Facebook a partir de variáveis de ambiente.
access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
app_id = os.getenv('FACEBOOK_APP_ID')
app_secret = os.getenv('FACEBOOK_APP_SECRET')
ad_account_id = os.getenv('FACEBOOK_AD_ACCOUNT_ID')

# Inicializa a API do Facebook Ads com as credenciais carregadas.
FacebookAdsApi.init(access_token=access_token, app_id=app_id, app_secret=app_secret)

# Define a classe AdSetCreator, especializada na criação de conjuntos de anúncios.
class AdSetCreator(BaseTool):
    """
    Ferramenta para criar conjuntos de anúncios dentro de uma campanha no Facebook.
    """
    # Campos para o nome do conjunto de anúncios e o orçamento diário.
    name: str = Field(..., description='Nome do conjunto de anúncios.')
    budget: int = Field(..., description='Orçamento diário para o conjunto em centavos.')

    # Método principal que cria o conjunto de anúncios no Facebook.
    def run(self):
        try:
            # Verifica se o ID da campanha existe no estado compartilhado antes de prosseguir.
            if not self.shared_state.get('campaign_id'):
                raise ValueError('ID da campanha não encontrado. Por favor, use a ferramenta AdCampaignStarter primeiro.')

            # Acessa a conta de anúncios usando o ID fornecido.
            ad_account = AdAccount(ad_account_id)
            # Define parâmetros para a criação do conjunto de anúncios, incluindo público-alvo, orçamento, e período de veiculação.
            params = {
                'campaign_id': self.shared_state.get('campaign_id'),
                'name': self.name,
                'targeting': {"geo_locations": {"countries": ["US"]}},
                'start_time': datetime.today().isoformat(),
                'end_time': (datetime.today() + timedelta(days=7)).isoformat(),
                'status': AdSet.Status.active,
                "billing_event": "IMPRESSIONS",
                'optimization_goal': "LINK_CLICKS",
                "bid_amount": "100",
            }
            # Cria o conjunto de anúncios e armazena o ID no estado compartilhado.
            ad_set = ad_account.create_ad_set(params=params)
            self.shared_state.set('ad_set_id', ad_set["id"])
            # Retorna uma mensagem de sucesso após a criação.
            return f'Conjunto de anúncios {self.name} criado com sucesso com ID {ad_set["id"]}.'

        # Trata possíveis erros na criação do conjunto de anúncios.
        except facebook_business.exceptions.FacebookRequestError as e:
            return f'Erro ao criar conjunto de anúncios: {e}'

# Bloco que verifica se este script é o ponto de entrada principal e, nesse caso, executa a ferramenta.
if __name__ == "__main__":
    # Exemplo de uso da ferramenta, especificando nome e orçamento.
    tool = AdSetCreator(name="Teste Conjunto de Anúncios", budget=1000)
    tool.shared_state.set('campaign_id', '120207371826520118')  # Define o ID da campanha no estado compartilhado.
    print(tool.run())  # Executa a ferramenta e imprime o resultado.

