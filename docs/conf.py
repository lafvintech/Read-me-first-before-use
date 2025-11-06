# -- Project information -----------------------------------------------------
project = "Read Me First — Before Use"
author = "Project Owner"

# -- General configuration ---------------------------------------------------
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = ['custom.css']

# Keep sidebar compact for landing-style content
html_theme_options = {
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 2,
}