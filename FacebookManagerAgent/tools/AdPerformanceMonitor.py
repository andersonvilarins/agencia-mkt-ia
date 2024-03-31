# Importa BaseTool de agency_swarm.tools, uma base para todas as ferramentas criadas na framework.
from agency_swarm.tools import BaseTool

# Importa classes específicas da API de negócios do Facebook para manipular conjuntos de anúncios e campanhas.
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.campaign import Campaign

# Importa Field de pydantic, usado para definir campos com validação e descrições em modelos de dados.
from pydantic import Field

# Importa o módulo os para interagir com o sistema operacional, aqui usado principalmente para acessar variáveis de ambiente.
import os

# Importa o módulo facebook_business para acessar a API do Facebook.
import facebook_business

# Importa FacebookAdsApi para inicialização e configuração da API do Facebook.
from facebook_business.api import FacebookAdsApi

# Importa classes de adobjects para manipulação de anúncios.
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adreportrun import AdReportRun

# Importa uma exceção específica para lidar com erros de requisição à API do Facebook.
from facebook_business.exceptions import FacebookRequestError

# Importa load_dotenv do dotenv para carregar variáveis de ambiente de um arquivo .env.
from dotenv import load_dotenv

# Executa a função load_dotenv, que carrega variáveis de ambiente do arquivo .env para o ambiente do Python.
load_dotenv()

# Acessa e armazena variáveis de ambiente específicas para autenticação na API do Facebook.
access_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
app_id = os.getenv('FACEBOOK_APP_ID')
app_secret = os.getenv('FACEBOOK_APP_SECRET')
ad_account_id = os.getenv('FACEBOOK_AD_ACCOUNT_ID')

# Inicializa a API do Facebook Ads com as credenciais obtidas das variáveis de ambiente.
FacebookAdsApi.init(access_token=access_token, app_id=app_id, app_secret=app_secret)

# Define uma classe para monitoramento do desempenho de anúncios no Facebook, estendendo BaseTool.
class AdPerformanceMonitor(BaseTool):
    """
    Permite o monitoramento do desempenho de anúncios no Facebook, incluindo métricas como cliques, impressões e taxas de conversão.
    """
    # Define o ID do anúncio como um campo obrigatório para monitoramento.
    ad_id: str = Field(
        ..., description="O ID do anúncio a ser monitorado."
    )
    # Define os campos que serão recuperados das informações do anúncio, como impressões, cliques e gastos.
    fields: list = Field(
        ["impressions", "clicks", "spend"], description="Os campos a serem recuperados das informações do anúncio."
    )

    # Define o método run, que é chamado para executar o monitoramento do desempenho do anúncio.
    def run(self):
        try:
            # Cria um objeto de anúncio com o ID fornecido.
            ad = Ad(self.ad_id)
            # Define parâmetros para a consulta de insights, como o intervalo de datas.
            params = {
                "date_preset": "maximum",
            }
            # Retorna os insights do anúncio com base nos campos especificados.
            return ad.get_insights(fields=self.fields,params=params)
        except FacebookRequestError as e:
            # Retorna uma mensagem de erro caso ocorra um problema ao acessar as métricas de desempenho do anúncio.
            return f"Erro ao acessar métricas de desempenho do anúncio: {e.api_error_message()}"

# Verifica se o script é o módulo principal sendo executado, e não um módulo importado.
if __name__ == "__main__":
    # Cria uma instância da ferramenta com um ID de anúncio de exemplo e executa o método run, imprimindo o resultado.
    tool = AdPerformanceMonitor(ad_id="23853583733130117")
    print(tool.run())
