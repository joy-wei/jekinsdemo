import time
import pytest
@pytest.fixture(scope="function")
def start(request):
    print("开始执行function")
def test_a(start):
    print("用例a执行")

class test_aaa:
    def test_1(self,start):
        print("用例01")
    def test_2(self,start):
        print("用例02")
if __name__ == "__main__":
    pytest.main(["-s","test_06.py"])