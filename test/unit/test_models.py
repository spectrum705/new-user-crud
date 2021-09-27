import pytest
import requests
import random
# from crud import app
# from models import User
url = "https://shine-scalloped-level.glitch.me"
email = "testuser"+ str(random.randint(1,100))+ "@test.com"

    


#test for adding new user
def test_add_user():
    """
    GIVEN user data
    WHEN a new User is created
    THEN check the email, first name, last name and password fields are added correctly
    """

    user_data =   {
    "f_name":"testuser",
    "l_name":"one",
    "email":email,
    "pwd" : "testhere",
    }

    req = requests.post(url+"/add", json=user_data)
    content = req.json()
    assert req.status_code == 200
    assert content["response"] == "new user added"
    # print(content)
    # print(req)


#testing unique users
def test_user_already():
    """
    GIVEN user data
    WHEN a new User is already present
    THEN check database for unique data
    """

    user_data =   {
    "f_name":"testuser",
    "l_name":"one",
    "email":email,
    "pwd" : "testhere",
    }
    req = requests.post(url+"/add", json=user_data)
    content = req.json()
    assert content["response"] == "Email already used"


#searching user
def test_existing_user_search():
    """
    GIVEN user data
    WHEN a new User is already present
    THEN check database with search funtions 
    """

    user_data =          {
        "query":"f_name",
        "value":"testuser"

    }

    req = requests.post(url+"/search", json=user_data)
    content = req.json()
    assert req.status_code == 200
    assert "result" in content

#testing non existing user
def test_notexisting_user_search():
    """
    GIVEN user data
    WHEN a new User not present
    THEN check database with search funtions 
    """

    user_data =          {
        "query":"f_name",
        "value":"asfklsafksal"

    }

    req = requests.post(url+"/search", json=user_data)
    content = req.json()
    assert req.status_code == 200
    assert "result" not in content
    
#updating existing user
def test_update_user_data():
    """
    GIVEN user data
    WHEN a user is  present
    THEN update the query 
    """

    user_data=     {
        "query":"f_name",
        "old_value": "testuser",
        "changethis":"email",
        "new_value": "emailupdated@waynecorp.com"

        }
    req = requests.post(url+"/update", json=user_data)
    content = req.json()
    assert req.status_code == 200
    assert content["response"] == "data updated"

    
#trying to update non existing user
def test_update_nonuser_data():
    """
    GIVEN user data
    WHEN a user is  not present
    THEN update the query should fail
    """

    user_data=     {
        "query":"f_name",
        "old_value": "dagjakg",
        "changethis":"email",
        "new_value": "emailupdated@waynecorp.com"

        }
    req = requests.post(url+"/update", json=user_data)
    content = req.json()
    assert req.status_code == 200
    assert content["response"] == "user doesn't exist"

    
    
#deleting existing user
def test_delete_user():
    """
    GIVEN user data
    WHEN a user is  present
    THEN delete the user data 
    """

    user_data=    {
                "query":"email",
                "value": "emailupdated@waynecorp.com"
                }
    req = requests.post(url+"/delete", json=user_data)
    content = req.json()
    assert req.status_code == 200
    assert content["response"] == "user removed"

#deleting nonexisting user
def test_delete_nonuser():
    """
    GIVEN user data
    WHEN a user is not  present
    THEN delete the user data  should fail
    """

    user_data=    {
                "query":"email",
                "value": "dasfaf@gmail.com"
                }
    req = requests.post(url+"/delete", json=user_data)
    content = req.json()
    assert req.status_code == 200
    assert content["response"] == "user does't exist"


#invalid route
def test_404():
    """
    GIVEN non existent route
    WHEN a route is called
    THEN return 404
    """

    
    req = requests.get(url+"/test")
    # content = req.json()
    assert req.status_code == 404
    

