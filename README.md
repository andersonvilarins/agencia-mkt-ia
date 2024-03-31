# MetaMarkAgência

Bem-vindo ao repositório **MetaMarkAgency**, uma solução de ponta projetada para automatizar e aprimorar seus esforços de marketing no Facebook usando o poder da IA. Esta agência SmmA é construída sobre a estrutura **Agency Swarm**, permitindo a criação de agentes especializados para lidar com diferentes aspectos do marketing do Facebook: geração de textos de anúncios, criação de imagens e gerenciamento de postagens no Facebook.

### Estrutura da Agência

A AI SmmA Live Agency é composta por três agentes principais:

- **Ad Copy Agent**: gera textos de anúncios atraentes e adaptados aos objetivos da sua campanha.
- **Agente Criador de Imagens**: utiliza Dalle 3 para criar imagens visualmente atraentes que complementam o texto do anúncio.
- **Facebook Manager Agent**: cuida da publicação de anúncios no Facebook, juntamente com a criação de campanhas e conjuntos de anúncios.

## Configuração do aplicativo do Facebook

Para utilizar o Facebook Manager Agent para postar anúncios, você precisa configurar um aplicativo do Facebook e obter as credenciais e permissões necessárias. Siga estas etapas para começar:

1. **Crie seu aplicativo do Facebook**:
    - Visite o site [Facebook for Developers](https://developers.facebook.com/) e faça login.
    - Clique em “Meus Aplicativos” e selecione “Criar Aplicativo”.
    - Escolha "Comercial" como tipo de aplicativo e forneça um nome para ele.
    - Siga as instruções para concluir o processo de criação do aplicativo.

2. **Adicione a API Marketing**:
    - No painel do seu aplicativo, encontre a seção "Adicionar um produto" e selecione "API de marketing".
    - Clique em "Configurar" para adicionar a API Marketing ao seu aplicativo.

3. **Definir configurações do aplicativo**:
    - Navegue até "Configurações" > "Básico" no painel do seu aplicativo.
    - Anote seu "App ID" e "App Secret" para uso posterior.
    - Adicione o domínio do seu aplicativo, URL da política de privacidade e outros detalhes necessários.

4. **Obter token de acesso**:
    - Acesse o [Facebook Graph API Explorer](https://developers.facebook.com/tools/explorer/).
    - Selecione seu aplicativo no menu suspenso "Aplicativo".
    - Clique em “Gerar Token de Acesso” e conceda as permissões necessárias para gerenciamento de anúncios.
    - Copie o token de acesso gerado para uso na configuração da sua agência.

5. **Atualizar arquivo de ambiente**:
    - Crie um arquivo `.env` no diretório do seu projeto, caso ainda não o tenha feito.
    - Adicione seu "App ID", "App Secret" e "Access Token" ao arquivo como variáveis de ambiente.

     ```env
     FB_APP_ID=seu_app_id
     FB_APP_SECRET=seu_app_secret
     FB_ACCESS_TOKEN=seu_token de acesso
     ```

6. **Instale o Facebook Business SDK** (se exigido pelas suas ferramentas):
    - Execute o seguinte comando para instalar o SDK: