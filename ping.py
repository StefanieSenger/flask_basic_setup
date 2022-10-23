from flask import Flask

app = Flask('ping') #'ping' is the name of the adress, so we can open http://0.0.0.0:9696/ping or call
                    # "curl http://0.0.0.0:9696/ping" from the terminal

@app.route('/ping', methods=['GET'])
def ping():
    return 'PONG'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696) # host='0.0.0.0' is the same as host='localhost'

# template form [this video](https://www.youtube.com/watch?v=W7ubna1Rfv8&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=52)
