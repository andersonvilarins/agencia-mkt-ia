#Este script ilustra a aplicação de modelos de inteligência artificial avançados (DALL-E 3) para a criação automatizada de imagens 
# baseadas em descrições textuais, uma tarefa útil para complementar anúncios com conteúdo visual relevante e atraente. A geração da 
# imagem é personalizada através de prompts detalhados, e a imagem resultante é salva localmente, com o caminho do arquivo atualizado 
# no estado compartilhado para uso posterior, como na criação de anúncios

# Importações necessárias para a execução do script.
from agency_swarm.tools import BaseTool  # Importa a classe base para ferramentas dentro do framework Agency Swarm.
from agency_swarm.util import get_openai_client  # Função utilitária para obter uma instância cliente da API da OpenAI.
from pydantic import Field  # Ferramenta do Pydantic para definir campos com validações em modelos de dados.
import openai  # Biblioteca oficial da OpenAI para interação com a API.
import os  # Módulo do sistema operacional para interagir com o sistema de arquivos e variáveis de ambiente.
import base64  # Módulo para codificação e decodificação de dados em base64.

# Carrega as variáveis de ambiente do arquivo .env, uma prática comum para manter segredos e configurações.
from dotenv import load_dotenv
load_dotenv()

# Configura a chave de API da OpenAI a partir de uma variável de ambiente.
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define a classe ImageGenerator, especializada na geração de imagens.
class ImageGenerator(BaseTool):
    """
    Gera imagens com base no texto do anúncio e em temas ou solicitações específicas, utilizando DALL-E 3.
    """
    # Define os campos para o texto do anúncio, tema e solicitações específicas para a geração da imagem.
    ad_copy: str = Field(..., description="A cópia do anúncio para basear a imagem.")
    theme: str = Field(..., description="O tema específico ou objetivos visuais da imagem.")
    specific_requests: str = Field(None, description="Quaisquer solicitações específicas relacionadas à criação da imagem.")

    # Método principal que executa a geração da imagem.
    def run(self):
        # Obtém o cliente da OpenAI e configura um timeout para a solicitação.
        client = get_openai_client()
        client.timeout = 120  # Configura o timeout para 120 segundos, permitindo tempo suficiente para a geração da imagem.
        # Constrói o prompt para a geração da imagem, incorporando o texto do anúncio, o tema e solicitações específicas.
        prompt = f"Crie uma imagem que represente visualmente: {self.ad_copy}. Tema: {self.theme}. {('Solicitações específicas: ' + self.specific_requests) if self.specific_requests else ''}"
        # Realiza a solicitação à API DALL-E 3 para gerar a imagem.
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024",
            response_format="b64_json",
        )
        # Salva a imagem gerada em um arquivo.
        self.save_image(response.data[0].b64_json)
        # Restaura o timeout do cliente para o valor padrão após a operação.
        client.timeout = 4
        # Retorna uma mensagem indicando o sucesso da operação.
        return "Imagem criada com sucesso. Agora você pode prosseguir com a criação de anúncios"

    # Método auxiliar para salvar a imagem codificada em base64 como um arquivo.
    def save_image(self, image_data):
        with open("image.png", "wb") as f:  # Abre (ou cria) um arquivo chamado "image.png" para escrita em modo binário.
            f.write(base64.b64decode(image_data))  # Decodifica os dados em base64 e escreve no arquivo.
            f.close()  # Fecha o arquivo após a escrita.
        # Atualiza o estado compartilhado com o caminho absoluto do arquivo de imagem gerado.
        self.shared_state.set("image_path", os.path.abspath("image.png"))

# Bloco que verifica se este script é o ponto de entrada principal e, nesse caso, executa a ferramenta.
if __name__ == "__main__":
    # Exemplo de uso da ferramenta, especificando texto do anúncio, tema e solicitações específicas.
    tool = ImageGenerator(ad_copy="Uma imagem de uma equipe de agentes de inteligência artificial", theme="IA", specific_requests="Incluir a interação de uma equipe de agentes de IA para construir todo o processo criativo de uma agência de marketing.")
    tool.run()  # Executa a ferramenta para gerar a imagem.
    # Imprime o caminho do arquivo da imagem gerada.
    print(tool.shared_state.get("image_path"))
