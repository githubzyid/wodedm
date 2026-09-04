import logging
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class StripPortMiddleware(MiddlewareMixin):
    def process_request(self, request):
        host = request.META.get('HTTP_HOST') or request.META.get('SERVER_NAME', '')
        logger.info("BEFORE STRIP: HTTP_HOST=%s, SERVER_NAME=%s", request.META.get('HTTP_HOST'), request.META.get('SERVER_NAME'))
        if ':' in host and not host.startswith('['):
            pure_host = host.split(':')[0]
            request.META['HTTP_HOST'] = pure_host
            request.META['SERVER_NAME'] = pure_host
            request.META['SERVER_PORT'] = '80'
            logger.info("AFTER STRIP: HTTP_HOST=%s, SERVER_NAME=%s", request.META.get('HTTP_HOST'), request.META.get('SERVER_NAME'))
        # 打印 get_host() 结果
        try:
            logger.info("GET_HOST after strip: %s", request.get_host())
        except Exception as e:
            logger.error("get_host error: %s", e)