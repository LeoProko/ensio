from back_office.html_factories.base import BaseHtmlFactory

class CustomHtmlFactory:
    @staticmethod
    def create(page_title, html_name, css_name, js_name):
        html = open('back_office/templates/html/' + html_name + '.html', 'r').read()
        if css_name != '':
            css = open('back_office/templates/css/' + css_name + '.css', 'r').read()
        else:
            css = ''
        if js_name != '':
            js = open('back_office/templates/js/' + js_name + '.js', 'r').read()
        else:
            js = ''

        return BaseHtmlFactory.create(page_title, html, css, js)
