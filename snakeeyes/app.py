from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/account/", methods=['POST','GET'])
def account():
  if request.method == 'POST':
    print request.form
    name = request.form['name']
    return "Hello %s" % name

  else:
    page ='''
    <html><body>
      <form action="" method="post" name="form">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name"/>
        <input type="submit" name="submit" id="submit"/>
      </form>
      </body><html>'''

    return page

@app.route('/terms')
def terms():
    return render_template('terms.html')


@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)