# Como Executar o Arquivo `interface.py`

Este repositório contém um script Python chamado `interface.py`. Siga as instruções abaixo para baixar o código e gerar um executável que pode ser executado sem abrir o console.

## Pré-requisitos

- Python instalado em sua máquina.
- PyInstaller instalado. Você pode instalar o PyInstaller usando pip:
  ```sh
  pip install pyinstaller
  
Passos
1. Clone o Repositório
Clone o repositório para sua máquina local:

sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Gere o Executável
Use o PyInstaller para criar um executável a partir do arquivo interface.py sem abrir o console:

sh
pyinstaller --onefile --noconsole interface.py
Explicação das opções:

--onefile: Cria um único arquivo executável.

--noconsole ou -w: Evita que o console seja aberto quando o executável for executado.

3. Encontre o Executável Gerado
Após executar o comando acima, o PyInstaller criará uma pasta dist no mesmo diretório onde o comando foi executado. O executável estará localizado dentro dessa pasta.

4. Execute o Executável
Agora, você pode executar o arquivo gerado (por exemplo, interface.exe no Windows) sem abrir o console:

sh
./dist/interface.exe
Problemas Comuns
Permissões negadas: Certifique-se de ter as permissões corretas para executar o arquivo.

Bibliotecas faltando: Se o seu script Python depender de bibliotecas externas, certifique-se de que elas estejam instaladas no ambiente onde o PyInstaller é executado.

Contribuições
Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request se você tiver sugestões ou melhorias.
