from ipware import get_client_ip
import logging

class Logger:
    def __init__(self, name, domain):
        self.logger = logging.getLogger(name)
        self.domain = domain

    def log_path(self, request):
        ip, is_routable = get_client_ip(request)
        log_message = 'ip: ' + str(ip) + ' path: ' + str(self.domain) + str(request.path)
        self.logger.info(log_message)
