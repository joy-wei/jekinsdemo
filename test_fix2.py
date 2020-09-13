import pytest
def test_4(login):
    print("用例4：登录后其他动作111")

def test_5():
    print("用例5：不需要登录，操作222")

if __name__ == "__main__":
    pytest.main(["-s","test_fix2.py"])