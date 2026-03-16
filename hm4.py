import time

class User:
    def __init__(self,name,role):
        self.name=name
        self.role=role
    
def is_admin(func):
        def wrapper(user):
            if user["role"] == "admin":
                func(user)
            else:
                print ('нет прав')  
        return wrapper 
@is_admin
def delete_video(user):
        print('видео удалено')
    






def timer(func):
    def wrapper():
        start = time.time()     
        func()                   
        end = time.time()        
        print(f"Время выполнения: {end - start} секунд")
    return wrapper


@timer
def download_video():
    time.sleep(3)
    print("Видео загружено")



admin_user = {'name: ':  "Karim", 'role': "admin"}
normal_user = {'name: ' : 'Ali',  'role' :'user'}


delete_video(admin_user)
delete_video(normal_user)

download_video()