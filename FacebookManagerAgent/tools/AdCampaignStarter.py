# Importa as classes e funções necessárias de outros módulos e pacotes.
from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import facebook_business.exceptions
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.adaccountuser import AdAccountUser as AdUser

# Carrega variáveis de ambiente de um arquivo .env, útil para manter informações sensíveis ou configuráveis fora do código.
from dotenv import load_dotenv
load_dotenv()

# Acessa variáveis de ambiente que contêm as credenciais necessárias para autenticar na API do Facebook.
access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
app_id = os.getenv('FACEBOOK_APP_ID')
app_secret = os.getenv('FACEBOOK_APP_SECRET')
ad_account_id = os.getenv('FACEBOOK_AD_ACCOUNT_ID')

# Inicializa a API do Facebook Ads com as credenciais obtidas das variáveis de ambiente.
FacebookAdsApi.init(access_token=access_token, app_id=app_id, app_secret=app_secret)

# Define uma classe para iniciar campanhas publicitárias no Facebook.
class AdCampaignStarter(BaseTool):
    """
    Ferramenta para iniciar campanhas de anúncios no Facebook.
    """

    # Define os campos necessários para criar uma campanha, incluindo nome e orçamento diário.
    campaign_name: str = Field(..., description='Nome da campanha publicitária.')
    budget: int = Field(..., description='Orçamento diário para a campanha em centavos.')

    # Método que efetivamente cria a campanha no Facebook.
    def run(self):
        try:
            # Acessa a conta de anúncios usando o ID fornecido.
            ad_account = AdAccount(ad_account_id)
            # Define parâmetros para a criação da campanha, incluindo nome, objetivo, status, orçamento e moeda BRL.
            params = {
                'name': self.campaign_name,
                'objective': "OUTCOME_LEADS",
                'status': Campaign.Status.active,
                ##linha de baixo inserida para teste 05/04/24
                'currency':AdAccount.Currency.brl,
                'daily_budget': self.budget,
                'special_ad_categories': 'NONE',
            }
            # Cria a campanha na conta de anúncios e armazena o ID da campanha criada.
            campaign = ad_account.create_campaign(params=params)
            self.shared_state.set('campaign_id', campaign["id"])
            # Retorna uma mensagem de sucesso com o ID da campanha.
            return f'Campanha {self.campaign_name} iniciada com sucesso com ID {campaign["id"]}.'
        except facebook_business.exceptions.FacebookRequestError as e:
            # Em caso de erro na criação da campanha, retorna uma mensagem de erro.
            return f'Erro ao iniciar campanha publicitária: {e}'

# Verifica se este script é o ponto de entrada principal e, se for, cria e executa a ferramenta.
if __name__ == "__main__":
    # Cria uma instância da ferramenta com um nome de campanha e orçamento específicos.
    tool = AdCampaignStarter(campaign_name="Test Campaign", budget=1000)
    # Executa a ferramenta e imprime o resultado.
    print(tool.run())
