from src.external_logger import external_logger

def log_message(message):
    # Эта функция ничего не возвращает, только вызывает другую
    external_logger.send(message)