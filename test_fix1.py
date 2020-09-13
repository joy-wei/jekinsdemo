import pytest
def test_1(login):
    print("用例1：登录后其他动作111")

def test_2():
    print("用例2：不需要登录，操作222")

def test_3(login):
    print("用例3：登录之后其他动作333")

if __name__ == "__main__":
    pytest.main(["-s","test_fix1.py"])