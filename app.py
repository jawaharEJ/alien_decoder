from flask import Flask, render_template, request

app = Flask(__name__)

def decode_signal(signal):

    signal = signal.lower()

    if "help" in signal:
        return "Distress signal detected from unknown civilization."

    elif "xj" in signal:
        return "Navigation coordinates from alien spacecraft."

    elif "ztr" in signal:
        return "Encrypted communication requesting contact."

    elif "42" in signal:
        return "Energy signature detected in the transmission."

    else:
        return "Unknown alien language. Further analysis required."


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/decode", methods=["POST"])
def decode():

    signal = request.form["signal"]

    result = decode_signal(signal)

    return render_template("result.html", signal=signal, result=result)


if __name__ == "__main__":
    app.run(debug=True)