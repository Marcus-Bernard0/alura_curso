def greet_user ():
    "mostra uma simples saudação"
    print("Hello")

greet_user()


def greet_user (username):
    "mostra uma simples saudação"
    print(f"Hello {username.title()}")

greet_user('marcus')


