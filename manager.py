from flask_script import Manager

from twittor import create_app

app = create_app
manager = Manager(app)

if __name__ == "__main__":
    manager.run()


# Remarks:
# option + z ----Toggle word wrap:切换块注释，即：将一行长代码在一页显示完整。