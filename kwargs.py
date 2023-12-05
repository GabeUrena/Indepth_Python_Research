# When you dont know how many keyword arguments are going to get passed
# Simply use Kwargs, type ** infront of an argument

def user(**username):
    print (username)
    
user(username1='xyz', username2='abc')

def user2(**user_info):
    print(user_info['username'])
    
user2(username='Gabriel', age='22')

