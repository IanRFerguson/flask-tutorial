# Flask Tutorial

This is a quick rundown of a few interesting features of Flask

## How To Run

You can run this app at the command line like so:

```bash
# Run the WSGI file
python3 wsgi.py

# Run the app outside of WSGI
flask run
```

## Where Things Live

* The app itself is created in **`./example_app/__init__.py`** 
* This is where the routes are defined, the app is created, and a few common variables are defined
* The **`wsgi.py`** file imports the app so you can run it with Python (this is also a file that most web servers will expect when you want to run an app in production)

* Flask convention requires a `/static` and `/templates` folder
* `/static` contains files that don't change - CSS, JavaScript, images you want to render
* `/templates` includes the HTML - Flask allows you to dynamically update HTML files, so you can point the Flask app to an HTML form with a given set of variables and they will render natively

## More Exploring!

* There  are LOTS of things not covered by this tutorial

* Check out `Flask-SQLAlchemy` `Flask-Migrate` and other native db solutions that work great with Flask