from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def Calculadora():

    resultado = None

   
    if request.method == "POST":

        
        n1 = int(request.form["numero1"])
        n2 = int(request.form["numero2"])

        # fazer a conta
        resultado = n1 + n2

    # enviar o resultado para o HTML
    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)