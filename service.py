import os
import shutil
import logging
import time
directory_path = "C:\InterSystems\Cache\mgr\journal"

logging.basicConfig(
    filename="app.log",          
    filemode="a",                
    format="%(asctime)s - %(levelname)s - %(message)s",  
    level=logging.INFO         
)

def deleta_arquivos_journal():
    log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
    try:
        items = os.listdir(directory_path)
        for item in items:
            item_path = os.path.join(directory_path, item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                    log_mensagem(f"Deleted file: {item}")
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    log_mensagem(f"Deleted directory: {item}")
            except PermissionError:
                log_mensagem(f"Permission denied to delete {item}. It may be in use.")
            except Exception as e:
                log_mensagem(f"Could not delete {item}: {e}")
    except FileNotFoundError:
        log_mensagem(f"The directory {directory_path} does not exist.")
    except PermissionError:
        log_mensagem(f"Permission denied to access the directory {directory_path}.")


# Função para registrar uma mensagem personalizada
def log_mensagem(mensagem, nivel="info"):
    """
    Loga para registro de dados

    Args:
        mensagem (str): A mensagem a ser logada.
        nivel (str): O nível do log. Pode ser "debug", "info", "warning", "error" ou "critical".
    """
    if nivel == "debug":
        logging.debug(mensagem)
    elif nivel == "info":
        logging.info(mensagem)
    elif nivel == "warning":
        logging.warning(mensagem)
    elif nivel == "error":
        logging.error(mensagem)
    elif nivel == "critical":
        logging.critical(mensagem)
    else:
        logging.info(mensagem)  # Caso o nível seja desconhecido, usa "info" por padrão

