# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ADR-RID portalen'
copyright = '2025, Direktoratet for samfunnssikkerhet og beredskap'
author = 'Henrik Kringhaug'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []
language = 'nb_NO'
templates_path = ['_templates']
exclude_patterns = ['originals/rst/*.rst','originals/word/*.docx','originals/tabellA/*']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_logo = 'logo.SVG'
# html_theme_options = {
#     "logo": {
#         "link": "https://www.dsb.no",
#     }
# }


# =============================================================================
# #Remove sidebar for the following pages
html_sidebars = {
  "docs/ADRRID2025/Del3Tabell/Del3Tabell": [],
  "docs/ADRRID2025/Del0/OmADRRID":[],
  "docs/ADRRID2025/landtransportforskriften":[],
  "docs/ADRRID2025/landtransportforskriftenindex":[],
  "docs/ADRRID2025/ADRRID2025Index":[],
}

# =============================================================================
##This is global setting
# html_theme_options = {
#     "secondary_sidebar_items": {
#         "docs/ADRRID2025/Del3Tabell/Del3Tabell": [],
#     },
# }
# =============================================================================

html_theme_options = {
    "secondary_sidebar_items": {
         "**": ["page-toc", "edit-this-page", "sourcelink"],
         "docs/ADRRID2025/Del3Tabell/Del3Tabell": [],
    },
    "external_links": [
        {"name": "Farliggodspermen", "url": "https://farliggodspermen.no/"}
    ],
    "icon_links": [
    {
        "name": "18a",
        "url": "/ADRRIDOnline/_static/modulvogntog_snake.html",
        "icon": "fa-solid fa-truck-front",
        "type": "fontawesome",
    },
    ],
}




#This loads datatables globally for all
html_js_files = [
    "https://code.jquery.com/jquery-3.7.1.min.js",  # Include jQuery
    "https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js",  # DataTables JS
]

html_css_files = [
    "https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css",  # DataTables CSS
]


def add_my_files(app, pagename, templatename, context, doctree):
    if pagename == "docs/ADRRID2025/Del3Tabell/Del3Tabell":  # Match the exact page name
        app.add_css_file("tablescustom.css")  
        # app.add_js_file("https://code.jquery.com/jquery-3.7.1.min.js")# Add the custom CSS file
        # app.add_js_file("https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js")
        app.add_js_file("tablescustom.js", loading_method='defer')   # Add the custom JS file



def setup(app):
    app.connect("html-page-context", add_my_files)

