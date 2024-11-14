class User:
    posts = {}


    def __init__(self, name, email=None, drivers_liscence=None):
        self.Name = name
        self.Email = email
        self.Drivers_liscence = drivers_liscence
        self.User_posts = []

    def create_a_post(self):
        post_title = input("Post Title: ")
        post_body = input("Post Body: ")
        self.User_posts.append(post_title)

        posts_key = post_title+self.Name
        posts_key = posts_key.strip()

        User.posts[posts_key] = post_body

    def delete_a_post(self):
        index = int(input("Which post would you like to delete: "))
        index = index - 1

        key = self.User_posts[index]+self.Name
        key = key.strip()

        del User.posts[key]
        del self.User_posts[index]
        

    def see_my_posts(self):
        if len(self.User_posts) == 0:
            return ""
        else:
            print(self.User_posts)

    def see_all_posts(self):
        if len(User.posts) == 0:
            return ""
        else:
            print(list(User.posts.keys))


# user = User("John", "john@email.com", "FDUI87")
# user.create_a_post()
# user.see_my_posts()
# user.delete_a_post()
# user.see_my_posts()