class User:
    def __init__(self,name,role):
        self.role= role
        self.name = name


def is_admin(func):
    def wrapper(user):
        if user.role == 'admin':
            return func(user)
        else:
            print('нет прав')
    return wrapper



def logger(func):
    def wrapper(*args, **kwargs):
        print("Начало операции")
        
        result = func(*args, **kwargs)
        
        print("Конец операции")
        return result
    
    return wrapper

@is_admin
@logger
def delete_account(user):
    print('акк удален')

admin_user = User("Karim", 'admin')
normal_user = User('Ali', 'user')

delete_account(admin_user)
delete_account(normal_user)





        