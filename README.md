# ThomB93.github.io

To add new changes to the site, execute the following commands in order:

$ python -m pelican content -o output -s pelicanconf.py
$ python -m ghp_import output -b gh-pages
$ git push origin gh-pages
