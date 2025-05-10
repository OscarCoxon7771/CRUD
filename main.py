from flask import Flask, request,render_template
app=Flask(__name__)

usuarios=[]
id_contador=1

@app.route("/", methods=["GET", "POST"])
def crud():
    global id_contador
    if request.method=="POST":
        nombre=request.form["nombre"]
        correo=request.form["correo"]

    return render_template("crud.html")













if __name__ == "__main__":
    app.run(debug=True)