# 아래에 코드를 작성하시오.
class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
  
  def show_info(self):
    return f'Name: {self.name}, Email: {self.email}'

class AdminUser(User):
  def __init__(self, name, email, permission):
    super().__init__(name, email)
    self.permissions = permission

  def show_info(self):
    return f'Name: {self.name}, Email: {self.email}, Permissions: {self.permissions}'

alice = User("Alice","alice@example.com")
bob = User("Bob","bob@example.com")
charlie = AdminUser("Charlie","charlie@example.com", "Full Access")

print(alice.show_info())
print(bob.show_info())
print(charlie.show_info())