import allure
import pytest


@allure.feature("用户管理模块")
class TestUser:
    @allure.story("用户登录功能")
    @allure.title("测试正常登录")
    def test_login_success(self):
        with allure.step("步骤1：输入用户名和密码"):
            username = "admin"
            password = "123456"

        with allure.step("步骤2：验证登录结果"):
            assert username == "admin" and password == "123456"

    @allure.story("用户注册功能")
    @allure.title("测试邮箱格式校验")
    @pytest.mark.parametrize("email, is_valid", [
        ("test@example.com", True),
        ("invalid_email", False)
    ])
    def test_register_email(self, email, is_valid):
        with allure.step(f"验证邮箱格式：{email}"):
            # 根据预期结果调整断言
            assert ("@" in email) == is_valid, f"邮箱格式校验不符合预期：{email}"
