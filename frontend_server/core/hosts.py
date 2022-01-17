# DNS setup
# https://devilbox.readthedocs.io/en/latest/howto/dns/add-custom-dns-server-on-linux.html
#
# django-hosts
# docs: https://django-hosts.readthedocs.io/en/latest/
# tutorial: https://www.ordinarycoders.com/blog/article/django-subdomains
#

from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host('', 'core.urls', name='base'),
    host('docs', 'docs.urls', name='docs'),
    host('shop', 'shop.urls', name='shop'),
    host('crm', 'crm.urls', name='crm'),
    host('design', 'design.urls', name='design'),
)
