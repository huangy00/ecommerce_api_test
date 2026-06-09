import pytest
import allure
from utils.logger import logger

@allure.epic("电商系统")
@allure.feature("用户模块")
class TestLogin:
    
    @allure.story("登录接口")
    @allure.title("{case_name}")  # 动态显示测试用例名称
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        "case_data", 
        [
    {"case_name": "正确的账号密码登录", "username": "mor_2314", "password": "83r5^_", "expected_status": 201},
    {"case_name": "错误的密码登录", "username": "mor_2314", "password": "wrong_password", "expected_status": 401},
    {"case_name": "账号为空登录", "username": "", "password": "83r5^_", "expected_status": 400},
],
        ids=["正确账号密码", "错误密码", "账号为空"]  # 给每个用例起个别名
    )
    def test_login(self, api_client, case_data):
        """测试用户登录接口"""
        logger.info(f"正在执行测试: {case_data['case_name']}")
        
        # 发起登录请求
        response = api_client.post("/auth/login", json={
            "username": case_data["username"],
            "password": case_data["password"]
        })
        
        # 断言状态码
        assert response.status_code == case_data["expected_status"]
        
        # 将请求和响应附加到 Allure 报告中（超级加分项！）
        allure.attach(
            body=f"请求URL: {response.request.url}\n请求体: {response.request.body}",
            name="请求信息",
            attachment_type=allure.attachment_type.TEXT
        )
        allure.attach(
            body=f"状态码: {response.status_code}\n响应体: {response.text}",
            name="响应信息",
            attachment_type=allure.attachment_type.TEXT
        )