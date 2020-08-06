from flask import Flask, request, render_template
import json
#import rinaBoard
app = Flask(__name__)
#board = rinaBoard.Board(64)

@app.route('/')
def homepage():
	return render_template("home.html")


@app.route('/color', methods=['POST'])
def color():
	print(request.json)
	color = request.json["color"]
	#board.fill(color)
	return "uwu"


if __name__ == '__main__':
	app.run(host='0.0.0.0')
