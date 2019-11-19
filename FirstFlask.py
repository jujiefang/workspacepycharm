from flask import Flask
app = Flask(__name__)#参数__name__必须写，模块是按应用方式使用还是作为一个模块导入
@app.route('/hello')
@app.route('/') #多个URL请示发送到hello_world,则与两个@app.route()
def hello_world():
    return 'Hello, World!----'
@app.route('/he')
@app.route('/he/<username>')
def hello(username=None):#若多个请示URL都由此方法处理，若username不是必传的，可以将参数设置为username=None
    return 'hello %s'%username

from flask import render_template
@app.route('/index')
def index():
    return render_template('index.html',name='lisi')
from flask import request
@app.route('/login',methods=['POST', 'GET'])
def login():
    error = "ee"
    print(request.method)
    if request.method == 'POST':
        print(request.form["name"])
        error = request.form["name"]
        if(request.form["name"]=='admin' and  request.form["password"]=="admin"):
            return render_template('loginSuccess.html',info=request.form["name"])
        else:
            error ="用户名或密码错误"
            return render_template('login.html',info=error)

    return render_template('login.html',info=error)
if __name__ == '__main__':
    app.run(debug=True) #每次修改都需要重新启动服务，可以启动debug模式，修改后，自动生效


