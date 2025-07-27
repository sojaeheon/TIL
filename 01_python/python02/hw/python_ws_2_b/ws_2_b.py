# 아래에 코드를 작성하시오.
class Post:
  post_count = 0

  def __init__(self, title, content):
    self.title = title
    self.content = content
    Post.post_count += 1
  
  def show_content(self):
    print(self.content)
  
  @classmethod
  def total_post(cls):
    return cls.post_count

  @staticmethod
  def description():
    print("SNS 게시물은 소셜 네트워크 서비스에서 사용자가 작성하는 글을 의미합니다.")

first = Post("First Post", "This is the content of the first post.")
second = Post("Second Post", "This is the content of the second post.")

print(f'Title: {first.title}')
print(f'Content: {first.content}')
print(f'Title: {second.title}')
print(f'Content: {second.content}')
print(f'Total posts: {Post.total_post()}')
Post.description()