def app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ['Hello world!'.encode('utf-8')]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    server = make_server('', 6543, app)
    server.serve_forever()
