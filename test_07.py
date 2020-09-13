import time
import pytest
@pytest.fixture(scope="function")
def start(request):
    print("开始执行function")

@pytest.mark.usefixtures("start")
def test_a(start):
    print("用例a")

@pytest.mark.usefixtures("start")
class Test_aaa():
    def test_1(self):
        print("用例1")
    def test_2(self):
        print("用例2")
if __name__ == "__main__":
    pytest.main(["-s","test_7.py"])

