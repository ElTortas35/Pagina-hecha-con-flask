from flask import Flask
import random

app = Flask(__name__)
lista_random = [
    "No uses mucho el celular ya que puede afectarte fisicamente como emocionalmete",
    "La dependencia tecnológica es una relación poco saludable y adictiva con dispositivos tecnológicos",
    "Hay que poner limites en el uso de la tecnologia",
    ]
@app.route("/")
def index():
    return """
    <h1>Hola y bienvenido<h1>
    <center>esta pagina es para informar sobre la dependencia tecnologica que hay en estos dias</center>
    <p>La dependencia tencologica es muy mala ya que el uso constante y repetitivo de la tecnologia puede casuar problemas a en la salud de uno</p>
    <BODY BGCOLOR="BLACK" TEXT="WHITE">
    <a href="/random_factor">ver datos</a>
    <a href="/dependencia">consecuencias</a>
    <style>
    @keyframes color-change{
    0% {
     color: blue;
    }
    50% {
    color: red;
    }
    100% {
    color: blue;
    }
    }
    h1 {
    animation: color-change 3s infinite;
    }
    </style>
    <style>
    p {
    text-aling: center;
    color: white;
    }
    center {
    color: white;
    }
    a {
    list-style-type: none;
    background-color: grey;
    padding: 0px;
    color: white;
    font-family; Courier New ,sans-serif
    margin: 0px;
    text-decoration: none;
    display: block;
    text-align: center;
    }
    </style>
    """
@app.route("/random_factor")
def rando():
    return f'<p>{random.choice(lista_random)}</p> <h1>No dependas de la tecnologia!</h1> <BODY BGCOLOR="BLACK" TEXT="WHITE"> <a href="/">volver a el inicio</a>'
@app.route("/dependencia")
def randm():
    return """
    <h1>Depender de la tecnologia y sus consecuencias</h1>
    <center>La dependencia tecnológica puede tener consecuencias tanto positivas como negativas. Por un lado, la tecnología nos brinda numerosos beneficios, como la comunicación instantánea, el acceso a información y la automatización de tareas. Sin embargo, también existen desafíos:
    Problemas de salud física y mental: La dependencia tecnológica puede llevar al sedentarismo, la falta de actividad física y el aislamiento social1. Además, el uso excesivo de dispositivos electrónicos puede afectar nuestra capacidad de concentración y nuestra salud mental2.
    Desafíos en la resolución de problemas: Dependiendo demasiado de la tecnología puede dificultar nuestra capacidad para resolver problemas sin depender de ella. Es importante mantener habilidades cognitivas y creativas independientes de los dispositivos.
    Impacto en las relaciones interpersonales: La tecnología puede afectar negativamente nuestras relaciones con los demás. El aislamiento social directo es una consecuencia común, ya que las personas utilizan la tecnología para relacionarse pero se alejan del contacto directo</center>
    <a href="/">volver a el inicio</a>
    <BODY BGCOLOR="BLACK" TEXT="WHITE"> 
    <style>
    a {
    list-style-type: none;
    background-color: grey;
    padding: 0px;
    color: white;
    font-size: 20px;
    font-family; Courier New ,sans-serif
    margin: 0px;
    text-decoration: none;
    display: block;
    text-align: center;
    }
    </style>
    """
app.run(debug=True)
