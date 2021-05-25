from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/loginpage',methods=['GET', 'POST'])
def gologin():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된 값",email,pwd)
        if email == "a@a.com" and pwd == "1234":
            return '로그인 성공'
        else : 
            return '로그인 실패'
        return '전달된 값(POST)'

@app.route('/naver')
def naver():
    return render_template("naver.html")

@app.route('/signin')
def signin():
    return render_template("signin.html")

@app.route('/action_page', methods=['GET', 'POST'])
def gonaver():
    if request.method == 'GET':
        return "GET으로 전달"
    else:
        email = request.form['email']
        pwd = request.form['pwd']
        print("전달된 값", email, pwd)
        return "회원가입 데이터(POST)"

if __name__ == '__main__':
    app.run()