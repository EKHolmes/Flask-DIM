from flask import Flask, request, make_response, render_template, redirect
import essvar

app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])
def landing():
    code = request.cookies.get("code")
    if code is None:
        return render_template("authorize.html")
    else:
        return redirect("/index")




@app.route('/receiver', methods = ["GET", "POST"])
def receivePost():
    userCode = request.args["code"]
    returnResp = make_response(render_template('baseIndex.html'))
    returnResp.set_cookie('code', userCode)
    return redirect("/", code=302, Response=returnResp)
app.run(host='0.0.0.0', port=81)




@app.route('/index')
def index():
    return "you made it"