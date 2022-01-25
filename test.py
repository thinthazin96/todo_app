from app import app

#just a comment
def test1():
    
    """
    This function test that the flask application has a 
    correct response code when the application goes live 
    """
    response = app.test_client().get("/")
    assert response.status_code == 200


def test2():
    """A dummy docstring"""
    response = app.test_client().get("/edit")
    assert response.status_code == 200
    

def test3():
    """this fucntion check whether these text exits in the /edit browser"""
    response = app.test_client().get("/edit")
    assert b"To Do App" in response.data
    assert b"To Do Title" in response.data
    assert b"Add" in response.data