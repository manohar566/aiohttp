import logging


access_log = logging.getLogger('aiohttp.access')
client_log = logging.getLogger('aiohttp.client')
internal_log = logging.getLogger('aiohttp.internal')
server_log = logging.getLogger('aiohttp.server')
web_log = logging.getLogger('aiohttp.web')
websocket_log = logging.getLogger('aiohttp.websocket')
