from bottle import route, run, template, Bottle, response #type: ignore

app = Bottle()

main_html_path = "html/main.html"
why_html_path = "html/why.html"
qa_html_path = "html/qa.html"

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

@route('/css/<file>')
def style(file):
    response.content_type = "text/css"
    style = open('css/' + file, "r")
    data = style.read()
    style.close()
    return data

if __name__ == '__main__':
    Bottle.debug(True)
    Bottle.reloader(True)
    run(host='localhost', port=8080)