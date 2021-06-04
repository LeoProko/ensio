class BaseHtmlFactory:
    @staticmethod
    def add_in_base(page_title, content_html, content_css, content_js):
        html_template = open('frontend_server/templates/html/base.html', 'r').read()
        html_template = html_template.replace('&page_title&', page_title)
        html_template = html_template.replace('&content_html&', content_html)
        html_template = html_template.replace('&content_css&', content_css)
        html_template = html_template.replace('&content_js&', content_js)

        return html_template

    @staticmethod
    def create(page_title, html_name, css_name, js_name):
        html = open('frontend_server/templates/html/' + html_name + '.html', 'r').read()
        if css_name != '':
            css = open('frontend_server/templates/css/' + css_name + '.css', 'r').read()
        else:
            css = ''
        if js_name != '':
            js = open('frontend_server/templates/js/' + js_name + '.js', 'r').read()
        else:
            js = ''

        return BaseHtmlFactory.add_in_base(page_title, html, css, js)
