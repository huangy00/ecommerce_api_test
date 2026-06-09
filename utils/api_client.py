import requests
from utils.logger import logger

class APIClient:
    """企业级接口请求封装"""
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def request(self, method, endpoint, **kwargs):
        """
        统一请求方法
        :param method: 请求方法 (GET, POST, PUT, DELETE)
        :param endpoint: 接口路径 (如 /products/1)
        :param kwargs: 其他参数 (json, params, headers等)
        """
        url = f"{self.base_url}{endpoint}"
        
        # 记录请求日志
        logger.info(f"发起请求: {method} {url}")
        logger.debug(f"请求参数: {kwargs}")

        try:
            response = self.session.request(method, url, timeout=10, **kwargs)
            
            # 记录响应日志
            logger.info(f"响应状态码: {response.status_code}")
            logger.debug(f"响应内容: {response.text[:500]}")  # 只打印前500个字符防刷屏
            
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"请求发生异常: {e}")
            raise e

    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request("POST", endpoint, **kwargs)