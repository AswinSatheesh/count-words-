from flask import Flask,jsonify
app = Flask(__name__)
PORT=5000
@app.route("/",methods=["GET","POST"])
def hello():
    r={"Hai":"helo"}
    return jsonify(r)

@app.route("/count",methods=["GET","POST"])
def count():
    file=open("text.txt","r")
    data=file.read()
    words=data.split()

    result=len(words)
    print("Number of words in this text file is:",len(words))
    return str(result)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=PORT)