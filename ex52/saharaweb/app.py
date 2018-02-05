from flask import Flask, render_template, request, session, abort, url_for, redirect, flash
import maps

users = {'username':'helena', 'password':'python'}

app = Flask(__name__)

# login in this case is only possible with the username 'admin' and password 'password'
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] not in users['username'] or request.form['password'] not in users['password']:
            error = 'Invalid Credentials. Please try again.'
        else:
            return render_template('show_scene.html', hello_title="Hello", welcome_title=users['username'])
    return render_template('login.html', error=error)


@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = maps.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        session['scene'] = maps.START.urlname
        return render_template('show_scene.html', hello_title="Hello", welcome_title=users['username'])


@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            pass 
            #return render_template('you_died.html')
        else:
            currentscene = maps.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                #There is no transition for that user input.
                #what should your code do in response?
                return render_template('you_died.html')
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        #There is no transition for that user input.
        #what should your code do in response?
        return render_template('you_died.html')

#This URL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = maps.START.urlname
    return redirect(url_for('game_get')) #redirect the browser to the url for game_get


app.secret_key = '0302g15159hw357530'

if __name__ == "__main__":
    #debugging is pretty helpful. refreshes the application automatically
    app.run(debug=True)
