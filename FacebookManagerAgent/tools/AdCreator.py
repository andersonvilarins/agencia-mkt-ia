#Este script exemplifica a integração e utilização da API do Facebook Business para automatizar a criação de anúncios no Facebook, 
# destacando a importância da organização e validação de pré-requisitos no processo de automação de marketing digital.

# Importações necessárias para o funcionamento do script.
import os  # Módulo do sistema operacional para interagir com o sistema de arquivos.

# Importa as ferramentas e classes necessárias do framework agency_swarm e da API do Facebook.
from agency_swarm.tools import BaseTool  # Classe base para todas as ferramentas criadas no framework.
from facebook_business.adobjects.ad import Ad  # Classe para manipular anúncios no Facebook.
from facebook_business.adobjects.adaccount import AdAccount  # Classe para acessar contas de anúncios.
from facebook_business.adobjects.adcreative import AdCreative  # Classe para criar o criativo do anúncio.
from facebook_business.adobjects.adimage import AdImage  # Classe para manipular imagens dos anúncios.
from facebook_business.api import FacebookAdsApi  # API do Facebook Ads para autenticação e execução de operações.
from facebook_business.exceptions import FacebookRequestError  # Classe de exceção para erros da API do Facebook.
from pydantic import Field, model_validator  # Ferramentas do Pydantic para validação de dados e modelos.

# Carrega as variáveis de ambiente do arquivo .env, uma prática comum para manter segredos e configurações.
from dotenv import load_dotenv
load_dotenv()

# Obtém credenciais de acesso à API do Facebook a partir de variáveis de ambiente.
access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
app_id = os.getenv('FACEBOOK_APP_ID')
app_secret = os.getenv('FACEBOOK_APP_SECRET')
ad_account_id = os.getenv('FACEBOOK_AD_ACCOUNT_ID')

# Inicializa a API do Facebook Ads com as credenciais carregadas.
FacebookAdsApi.init(access_token=access_token, app_id=app_id, app_secret=app_secret)

# Define a classe AdCreator, que é responsável por criar anúncios no Facebook.
class AdCreator(BaseTool):
    """
    Facilita a programação e a publicação de anúncios no Facebook, otimizando para o melhor timing e direcionamento de público.
    """
    # Campos necessários para a criação do anúncio, validados pelo Pydantic.
    name: str = Field(..., description='Título do anúncio.')
    link: str = Field(..., description="URL para o qual o anúncio redirecionará o usuário.")

    # Função principal que executa a lógica de criação do anúncio.
    def run(self):
        # Cria uma imagem do anúncio na plataforma do Facebook, usando um caminho de arquivo armazenado no estado compartilhado.
        image = AdImage(parent_id=ad_account_id)
        image[AdImage.Field.filename] = self.shared_state.get('image_path')
        image.remote_create()  # Envia a imagem para o Facebook.

        # Prepara o criativo do anúncio combinando a imagem, título, e texto.
        creative = AdCreative(parent_id=ad_account_id)
        creative[AdCreative.Field.title] = self.shared_state.get('ad_headline')
        creative[AdCreative.Field.body] = self.shared_state.get('ad_copy')
        creative[AdCreative.Field.object_story_spec] = {
            'page_id': os.getenv('FACEBOOK_PAGE_ID'),
            'link_data': {
                'image_hash': image.get_hash(),
                "call_to_action": {'type': 'LEARN_MORE'},
                'link': self.link,
                "name": self.shared_state.get('ad_headline'),
                "message": self.shared_state.get('ad_copy'),
            }
        }
        creative.remote_create()  # Cria o criativo no Facebook.

        # Cria o anúncio propriamente dito, associando-o ao conjunto de anúncios e ao criativo.
        ad = Ad(parent_id=ad_account_id)
        ad[Ad.Field.name] = self.name
        ad[Ad.Field.adset_id] = self.shared_state.get('ad_set_id')
        ad[Ad.Field.creative] = {'creative_id': creative['id']}
        ad.remote_create(params={'status': Ad.Status.paused})  # Publica o anúncio, inicialmente pausado.

        # Retorna uma mensagem de sucesso após a criação do anúncio.
        return f"Anúncio criado com sucesso com ID: {ad['id']}"

    # Decorador para validar se todos os requisitos foram atendidos antes da criação do anúncio.
    @model_validator(mode="after")
    def validate(self):
        # Verifica se todos os pré-requisitos estão presentes antes de permitir a execução.
        if not self.shared_state.get('image_path') or not self.shared_state.get('ad_set_id') or not self.shared_state.get('campaign_id') or not self.shared_state.get('ad_copy'):
            raise ValueError('Certifique-se de que todas as dependências foram atendidas: imagem, ID do conjunto de anúncios, ID da campanha e texto do anúncio.')

# Bloco que verifica se este script é o ponto de entrada principal e executa a criação do anúncio.
if __name__ == "__main__":
    # Exemplo de uso da classe, criando um anúncio com dados específicos.
    tool = AdCreator(name="Test Creative 2", link="https://www.example.com")
    tool.shared_state.set('image_path', 'image2.png')
    tool.shared_state.set('ad_set_id', '120207414681720118')
    tool.shared_state.set('ad_copy', '123')
    print(tool.run())


