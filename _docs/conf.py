import os
import sys

from recommonmark.parser import CommonMarkParser

templates_path = ['_templates']

source_suffix = ['.rst', '.md', '.markdown']
source_parsers = {
    '.md': CommonMarkParser,
    '.markdown': CommonMarkParser,
}

master_doc = 'index'
project = u'WebBSC Dokumentation'

html_static_path = ['_static']

html_extra_path = ['../_uploads']

html_theme = 'default'
htmlhelp_basename = 'ReadtheDocsTemplatedoc'

language = 'de'
