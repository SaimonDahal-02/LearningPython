def make_bold(func):
    def wrapper():
        return f'<b>{func()}</b>'
    return wrapper
def make_italic(func):
    def wrapper():
        return f'<i>{func()}</i>'
    return wrapper
def make_underline(func):
    def wrapper():
        return f'<u>{func()}</u>'
    return wrapper
@make_bold
@make_underline
@make_italic
def html():
    return '<p> We are learning python</p>'
print(html())