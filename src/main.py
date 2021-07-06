from bot import thread
from API import app
from waitress import serve


if __name__ == '__main__':
    thread.start()
    serve(app, host='0.0.0.0', port=80)
