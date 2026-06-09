import pytest
import yaml
from utils.api_client import APIClient

@pytest.fixture(scope="session")
def test_data():
    """全局读取测试数据，整个测试会话只读取一次"""
    with open("data/test_data.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data

@pytest.fixture(scope="session")
def api_client():
    """全局初始化 API 客户端，整个测试会话只初始化一次"""
    # 这里我们暂时写死 base_url，后续可以结合你的 config 读取
    client = APIClient(base_url="https://fakestoreapi.com")
    return client