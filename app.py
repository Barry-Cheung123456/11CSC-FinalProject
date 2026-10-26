from bottle import run, route, view, static_file

@route('/')
@view('home')
def home():
    return {}

@route('/myths')
@view('myths')
def myths():
    return {}

@route('/issues')
@view('issues')
def issues():
    return {}

@route('/solutions')
@view('solutions')
def solutions():
    return {}

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)