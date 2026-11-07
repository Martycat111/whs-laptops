from bottle import route, run, template, Bottle, response, static_file #type: ignore

app = Bottle()

main_html_path = "html/main.html"
why_html_path = "html/why.html"
qa_html_path = "html/qa.html"
specs_html_path = "html/specs.html"
location_html_path = "html/locate.html"

@route('/')
def main():
    main = open(main_html_path, "r")
    data = main.read()
    main.close()
    return data

@route('/why')
def main():
    why = open(why_html_path, "r")
    data = why.read()
    why.close()
    return data

@route('/q+a')
def qa():
    qa = open(qa_html_path, "r")
    data = qa.read()
    qa.close()
    return data

@route('/specs')
def specs():
    specs = open(specs_html_path, "r")
    data = specs.read()
    specs.close()
    return data

@route('/getting-there')
def locate():
    location = open(location_html_path, "r")
    data = location.read()
    location.close()
    return data


@route('/css/<file>')
def style(file):
    response.content_type = "text/css"
    style = open('css/' + file, "r")
    data = style.read()
    style.close()
    return data

@route('/js/<file>')
def script(file):
    response.content_type = "text/javascript"
    script = open('js/' + file, "r")
    data = script.read()
    script.close()
    return data

@route('/elitebook-img/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='img/Elitebook-x360-1030-G3/')

@route('/surface-img/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='img/Microsoft-Surface/')

@route('/lenovo-chromealike/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='img/Lenovo-cheapbook/')

@route('/img/Ifixit.jpg')
def ifiximg():
    return static_file("Ifixit.jpg", root='img/')
if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True, reloader=True)