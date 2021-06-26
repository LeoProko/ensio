class BaseHtmlFactory:
    @staticmethod
    def replace_macros_in_html_page(base_type, page_title, content_html, content_css, content_js):
        html_template = open('frontend_server/templates/html/' + base_type + '.html', 'r').read()
        html_template = html_template.replace('&page_title&', page_title)
        html_template = html_template.replace('&content_html&', content_html)
        html_template = html_template.replace('&content_css&', content_css)
        html_template = html_template.replace('&content_js&', content_js)

        return html_template

    @staticmethod
    def create_back_office(page_title, directory, html_name, css_name, js_name):
        html = open(directory + '/html/' + html_name + '.html', 'r').read()
        if css_name != '':
            css = open(directory + 'css/' + css_name + '.css', 'r').read()
        else:
            css = ''
        if js_name != '':
            js = open(directory + 'js/' + js_name + '.js', 'r').read()
        else:
            js = ''

        return BaseHtmlFactory.replace_macros_in_html_page('base_back_office', page_title, html, css, js)

    @staticmethod
    def create_customer_app(page_title, directory, html_name, css_name, js_name):
        html = open(directory + '/html/' + html_name + '.html', 'r').read()
        if css_name != '':
            css = open(directory + 'css/' + css_name + '.css', 'r').read()
        else:
            css = ''
        if js_name != '':
            js = open(directory + 'js/' + js_name + '.js', 'r').read()
        else:
            js = ''

        return BaseHtmlFactory.replace_macros_in_html_page('base_customers', page_title, html, css, js)
