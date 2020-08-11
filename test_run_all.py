import pytest

class TestClass:
        def test_one(self):
            x = "hello"
            assert 'h' in x
            print("success1")

        def test_two(self):
            x = "hello"
            # assert hasattr(x, 'check')
            assert 'h' in x
            print("success2")

        def test_three(self):
            a = "hello"
            b = "hello world"
            assert a in b
            print("success3")

if __name__ == "__main__":
    pytest.main('-q test_run_all.py')

