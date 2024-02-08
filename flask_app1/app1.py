# Import the Flask class from the Flask library
from flask import Flask

# Create an instance of a Flask application
# The first argument is the name of the application’s module or package. __name__ is a convenient shortcut.
# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(__name__)
app.config['SECRET_KEY'] = "1234567890"


# Add a route for the 'home' page
# use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def Home():
    # The function returns the message we want to display in the user’s browser. The default content type is HTML,
    # so HTML in the string will be rendered by the browser.
    return 'Home Page'


@app.route('/Statistic')
def statistic():
    return 'Statistic Page'


# Run the app
if __name__ == '__main__':
    app.run(debug=True,port=5231)
