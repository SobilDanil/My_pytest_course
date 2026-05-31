class ExternalLogger:
    def send(self, message):
        print(f'External logger: {message}')
external_logger = ExternalLogger()