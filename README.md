# LimparJournal

Este repositório contém um script Python chamado `interface.py`. Siga as instruções abaixo para instalar o PyInstaller, navegar até a pasta do arquivo e criar um executável.

## Pré-requisitos

1. **Realizar o Download do Repositório**

   - Baixe o repositório no formato ZIP e descompacte-o no local de sua preferência.

2. **Instalar o PyInstaller**

   - Abra o terminal e instale o PyInstaller com o comando:
     ```bash
     pip install pyinstaller
     ```

## Criando o Executável

1. **Navegue até a pasta** onde o arquivo `interface.py` está localizado. No terminal, use:
   ```bash
   cd caminho/para/a/pasta
2 Execute o comando PyInstaller para gerar um executável único sem console
  - pyinstaller --onefile --noconsole interface.py
