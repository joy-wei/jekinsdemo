import time
import pytest
@pytest.fixture(scope="module",autouse=True)
def start(request):
    print("开始执行module")
    print("module    {}".format(request.module.__name__))
    print("启动浏览器")


    yield
    print("结束测试")

class Test_aaa():
    @pytest.fixture(scope="function", autouse=True)
    def open_home(self,request):
        print("function:{}回到首页".format(request.function.__name__))

    def test_01(self):
        print("用例01")

    def test_02(self):
        print("用例02")

    if __name__ == "__main__":
        pytest.main(["-s", "test_08.py"])