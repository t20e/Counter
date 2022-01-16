from flask import Flask, render_template, redirect,request,session

app = Flask(__name__)
app.secret_key = '8974twjfnIUJJNL5%^VIOEH904b92390SCKJBIWSOF49saj492wbbsavcksd'
# Build a flask application that counts the number of times the root route ('/') has been viewed. 

@app.route('/')
def home_page():
    if 'amount' not in session:
        session['amount'] = 0
    return render_template('index.html')

@app.route('/amount_clicked_timnes', methods=['POST'])
def revisit_times():
    num = int(request.form['numOfTimes'])
    session['amount'] = session['amount'] + num

    print(session['amount'])
    print('user times')
    return redirect('/')


@app.route('/amount_clicked', methods=['POST'])
def revisit():
    session['amount'] = session['amount'] + 1

    print(session['amount'])
    print('revisted 1 more')
    return redirect('/')

@app.route('/inc_2', methods=['POST'])
def inc_2():
    session['amount'] = session['amount'] + 2

    print(session['amount'])
    print('revisted 1 more')
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['amount'] = 0

    print(session['amount'])
    print('revisted 1 more')
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destroy():
    session.clear()
    print('data destroyed')
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)


