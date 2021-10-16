from gs_support_tools import app
from gs_support_tools.home import home_api
from gs_support_tools.auth import auth_api

app.register_blueprint(home_api)
app.register_blueprint(auth_api)


if __name__ == '__main__':
    app.run(debug=True)
