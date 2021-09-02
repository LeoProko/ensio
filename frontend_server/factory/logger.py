from ipware import get_client_ip
import logging

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def log_path(self, request):
        ip, is_routable = get_client_ip(request)
        log_message = 'ip: ' + str(ip) + ' path: ' + str(request.path)
        self.logger.info(log_message)
