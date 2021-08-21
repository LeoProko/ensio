class Create:
    @staticmethod
    def _replace_macros_in_html_page(base_type, page_title, content_html, content_css, content_js):
        html_template = open('templates/html/factory/' + base_type + '.html', 'r').read()
        html_template = html_template.replace('&page_title&', page_title)
        html_template = html_template.replace('&content_html&', content_html)
        html_template = html_template.replace('&content_css&', content_css)
        html_template = html_template.replace('&content_js&', content_js)

        return html_template

    @staticmethod
    def _create(base_type, page_title, directory, html_name, css_name, js_name):
        html = open('templates/html/' + directory + '/' + html_name + '.html', 'r').read()
        if css_name != '':
            css = open('templates/css/' + directory + '/' + css_name + '.css', 'r').read()
        else:
            css = ''
        if js_name != '':
            js = open('templates/js/' + directory + '/' + js_name + '.js', 'r').read()
        else:
            js = ''

        return Create._replace_macros_in_html_page(base_type, page_title, html, css, js)

    @staticmethod
    def new_create(folder_name, page_title, html_name):
        html_content = open('templates/html/' + folder_name + '/' + html_name + '.html', 'r').read()

        html_template = open('templates/html/' + folder_name + '/base.html', 'r').read()
        html_template = html_template.replace('&page_title&', page_title)
        html_template = html_template.replace('&content_html&', html_content)

        return html_template

    @staticmethod
    def back_office(page_title, directory, html_name, css_name, js_name):
        return Create._create('base_back_office', page_title, directory, html_name, css_name, js_name)

    @staticmethod
    def customer_app(page_title, directory, html_name, css_name, js_name):
        return Create._create('base_customers', page_title, directory, html_name, css_name, js_name)

    @staticmethod
    def empty(page_title, directory, html_name, css_name, js_name):
        return Create._create('base_empty', page_title, directory, html_name, css_name, js_name)

class BaseHtmlFactory:
    create = Create
