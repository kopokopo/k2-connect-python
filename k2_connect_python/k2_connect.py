from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/buyGoods_transaction', methods=['POST'])
def buygoods_transaction():
    if request.method == 'POST':
        print(request.json)
        return '', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
