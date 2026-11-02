from bottle import route, run, template, Bottle, response #type: ignore

app = Bottle()

main_html_path = "html/main.html"

@route('/')
def main():
    main = open(main_html_path, "r")
    data = main.read()
    main.close()
    return data

@route('/css/<file>')
def style(file):
    response.content_type = "text/css"
    style = open('css/' + file, "r")
    data = style.read()
    style.close()
    return data

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True, reloader=True)