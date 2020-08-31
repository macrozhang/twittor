from flask import render_template, redirect, url_for
#                 渲染模板          重载/重定位 
from twittor.forms import LoginForm

def index():
    # name = 'World'
    name = {'username':'root'}

    posts = [
        {
            'author': {'username': 'root'},
            'body': "hi I'm root!"
        },
        {
            'author': {'username': 'test'},
            'body': "hi I'm test!"
        },        
    ]
    return render_template('index.html', name=name, posts=posts)


def login():
    # form = LoginForm(csrf_enabled=False) # 初学暂时不需要考虑csrf安全问题 参数已过时
    form = LoginForm(meta={'csrf': False}) # 上行参数已过时 替换新参数

    if form.validate_on_submit():
        msg = "username={}, password={}, remember_me={}".format(
            form.username.data,
            form.password.data,
            form.remember_me.data
        )
        print(msg)
        return redirect(url_for('index'))
    return render_template('login.html', title="Sign In", form=form)






    # rows = [
    #     {'Name': 'Python','Age':23},
    #     {'Name': 'Python','Age':23},
    #     {'Name': 'Python','Age':23},
    #     {'Name': 'Python','Age':23},
    #     {'Name': 'Python','Age':23},
    #     {'Name': 'Python','Age':23}
    # ]