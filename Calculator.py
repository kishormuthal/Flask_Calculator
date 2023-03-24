from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)
# Calculator on browser
@app.route("/", methods=["GET"])
def homepage():
    return render_template("index.html")

@app.route("/math", methods = ["POST"])
def  calculator():
 try:
     if (request.method == "POST"):
        ops = request.form["operation"]
        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])

        if (ops == "add"):
         r = num1 + num2
         result = " addition of " + str(num1) + " and " + str(num2) + " is " + str(r)

        if (ops == "subtract"):
         r = num1 - num2
         result = " subtraction of " +str(num1) + " and " + str(num2)+ " is " + str(r)

        if (ops == "multiply"):
         r = num1 * num2
         result = " multiplication of " + str(num1) + " and " +str(num2) + " is " + str(r)

        if (ops == "divide"):
         r = num1 / num2
         result = " division of " + str(num1) + " and " + str(num2) + " is " + str(r)
    
        return render_template("results.html",result= result)

 except ZeroDivisionError as e:
        return render_template("results.html",result= e)
     


# test code on postman
@app.route("/postman_action", methods = ["POST"])
def  calculator1():
 try:
     if (request.method == "POST"):
        ops = request.json["operation"]
        num1 = int(request.json["num1"])
        num2 = int(request.json["num2"])

        if (ops == "add"):
         r = num1 + num2
         result = " addition of " + str(num1) + " and " + str(num2) + " is " + str(r)

        if (ops == "subtract"):
         r = num1 - num2
         result = " subtraction of " +str(num1) + " and " + str(num2)+ " is " + str(r)

        if (ops == "multiply"):
         r = num1 * num2
         result = " multiplication of " + str(num1) + " and " +str(num2) + " is " + str(r)

        if (ops == "divide"):
         r = num1 / num2
         result = " division of " + str(num1) + " and " + str(num2) + " is " + str(r)
    
        return jsonify(result)
 except ZeroDivisionError as e:
      result = str(e)
      return jsonify(result)


    
         
if (__name__ == "__main__"):
  app.run(host="0.0.0.0", port=5000)

