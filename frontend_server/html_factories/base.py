class BaseHtmlFactory:
    @staticmethod
    def create(page_title, content_html, content_css, content_js):
        html_template = open('frontend_server/templates/html/base.html', 'r').read()
        html_template = html_template.replace('&page_title&', page_title)
        html_template = html_template.replace('&content_html&', content_html)
        html_template = html_template.replace('&content_css&', content_css)
        html_template = html_template.replace('&content_js&', content_js)

        return html_template
