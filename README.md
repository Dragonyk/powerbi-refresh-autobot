PowerBI AutoBot 🚀

Um bot automatizado para atualizar e publicar relatórios no Power BI Desktop sem necessidade de licença Pro, utilizando detecção de imagens e controle do mouse.
📌 Funcionalidades

    ⚡ Atualização automática de datasets no Power BI Desktop

    🚀 Publicação automática de relatórios atualizados

    ⏱️ Agendamento flexível de execução (horários fixos ou intervalos regulares)

    📁 Suporte a múltiplos arquivos .pbix

    🔍 Detecção inteligente de elementos da interface via reconhecimento de imagem

    📝 Log de execução para monitoramento

🛠️ Tecnologias Utilizadas

    Python 3.x

    PyAutoGUI (para automação de interface)

    Schedule (para agendamento de tarefas)

    OpenCV (para reconhecimento de imagens)

⚙️ Configuração
Pré-requisitos

    Power BI Desktop instalado no caminho padrão (C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe)

    Python 3.x instalado

    Pacotes Python listados em requirements.txt

Instalação

    Clone este repositório:
    bash

git clone https://github.com/seu-usuario/powerbi-autobot.git
cd powerbi-autobot

Instale as dependências:
bash

    pip install -r requirements.txt

    Configure os arquivos:

        Adicione suas imagens de referência na pasta res/

        Configure os arquivos .pbix no bot_settings.py

🎯 Como Usar

    Edite o arquivo bot_settings.py para configurar:

        Lista de arquivos .pbix para processar

        Modo de agendamento (intervalo ou horário específico)

        Configurações de tempo

    Execute o script principal:
    bash

    python main.py

    O bot irá:

        Abrir cada arquivo .pbix

        Clicar em "Atualizar"

        Aguardar a atualização completar

        Publicar no serviço Power BI

        Fechar o Power BI Desktop

⚠️ Limitações

    Requer que a interface do Power BI Desktop esteja em português (ou imagens correspondentes ao seu idioma)

    A resolução da tela deve ser consistente com as imagens de referência

    Não funciona com Power BI Desktop em segundo plano

Desenvolvido com ❤️ por Carlos L. S. Machado
