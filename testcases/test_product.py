
from utils.logger import logger


class TestProduct:
    def test_get_product_by_id(self, api_client, test_data):
        """测试根据ID获取商品详情"""
        product_id = test_data['product_data']['product_id']
        
        # 直接调用 fixture 注入的客户端，一行代码发请求
        response = api_client.get(f"/products/{product_id}")
        
        # 断言状态码
        assert response.status_code == 200
        
        # 断言返回的数据
        data = response.json()
        logger.info(f"成功获取到商品: {data['title']}")
        assert data['id'] == product_id