from greet import greet 
def test_greet():
    assert greet("Alice")=="Hello, Alice!"
    assert greet("ankit")=="Hello, ankit!"
    assert greet("ho")=="Hello, ho!"
    assert greet("")=="Hello, !"
    