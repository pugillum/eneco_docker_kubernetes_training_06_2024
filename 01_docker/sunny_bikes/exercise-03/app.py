from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return render_template(
        template_name_or_list="hello.html", name=request.args.get("name")
    )


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
