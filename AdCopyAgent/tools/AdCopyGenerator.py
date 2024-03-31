# Esse script ilustra como gerar textos de anúncios criativos e personalizados utilizando o GPT da OpenAI, adaptando-se ao público-alvo, 
# às características do produto e ao tom desejado para o anúncio. A implementação destaca o uso de tecnologias de IA para otimizar a 
#criação de conteúdo em marketing digital.

# Importa as classes e funções necessárias de outros módulos e pacotes.
from agency_swarm.tools import BaseTool  # Base para todas as ferramentas criadas no framework Agency Swarm.
from agency_swarm.util import get_openai_client  # Utilitário para obter uma instância do cliente da API OpenAI.
from pydantic import Field  # Importa Field de pydantic para definir campos com validações em modelos de dados.
import openai  # Importa a biblioteca da OpenAI para interação com o GPT.
import os  # Módulo do sistema operacional, usado aqui para acessar variáveis de ambiente.
import base64  # Módulo para codificação e decodificação de dados em base64.

from dotenv import load_dotenv  # Importa a função load_dotenv para carregar variáveis de ambiente do arquivo .env.
load_dotenv()  # Carrega as variáveis de ambiente.

# Define a chave de API da OpenAI usando uma variável de ambiente para autenticação nas requisições da API.
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a classe AdCopyGenerator estendendo BaseTool, para geração de textos de anúncios.
class AdCopyGenerator(BaseTool):
    """
    Gera textos de anúncios criativos e envolventes, adaptados aos dados demográficos do público-alvo,
    recursos do produto e tom de anúncio desejado.
    """
    # Define campos para a descrição do público-alvo, características do produto e o tom desejado do anúncio.
    target_audience: str = Field(..., description="Descrição dos dados demográficos do público-alvo.")
    product_features: str = Field(..., description="Características do produto ou serviço.")
    ad_tone: str = Field(..., description="Tom desejado do texto do anúncio.")

    # Método principal executado para gerar o texto do anúncio.
    def run(self):
        # Obtém uma instância do cliente da API da OpenAI.
        client = get_openai_client()
        # Monta o prompt que guiará a geração do texto pelo modelo GPT.
        prompt = f"""Gere uma segmentação criativa do texto do anúncio {self.target_audience}, 
        destacando os seguintes recursos: {self.product_features}. 
        O anúncio deverá ter um {self.ad_tone} tom. Não produza mais de 100 caracteres.
        Inclua um título em seu anúncio no seguinte formato:
        Título: [Seu título aqui]
        Ad Copy: [Your ad copy here]"""

        # Realiza a solicitação para geração do texto ao modelo GPT, especificando o modelo, o prompt e outras configurações.
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",  # Especifica o modelo GPT-3.5 turbo da OpenAI.
            prompt=prompt,
            temperature=0.7,  # Define a temperatura para variar a criatividade da resposta.
            max_tokens=250,  # Limita o número máximo de tokens na geração do texto.
        )
        # Extrai o texto gerado da resposta.
        text = response.choices[0].text.strip()
        # Separa o título do corpo do texto gerado.
        headline = text.split("Ad Copy:")[0].split("Título:")[1].strip()
        # Salva o título no estado compartilhado para uso posterior.
        self.shared_state.set("ad_headline", headline)
        # Separa e salva o corpo do anúncio no estado compartilhado.
        ad_copy = text.split("Ad Copy:")[1].strip()
        self.shared_state.set("ad_copy", ad_copy)
        # Retorna o texto completo do anúncio.
        return text

# Verifica se o script é executado diretamente e, em caso afirmativo, executa o exemplo.
if __name__ == "__main__":
    # Cria uma instância da ferramenta com parâmetros específicos e executa o método run.
    tool = AdCopyGenerator(
        target_audience="público jovem",
        product_features="sustentável, acessível, elegante",
        ad_tone="divertido, enérgico"
    )
    # Imprime o resultado da geração do texto do anúncio.
    print(tool.run())
