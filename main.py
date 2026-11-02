from sanic import Sanic #type: ignore
from sanic.response import html, css #type: ignore

app = Sanic("whs-laptops")

main_html_path = "html/main.html"

@app.route('/')
def main(request):
    return html(open(main_html_path).read())

@app.route('/css/<file>')
def style(file):
    return css(open("css/" + file).read())