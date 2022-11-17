import re

ITALICS = re.compile(r'<em>(.+?)</em>')
SPACES = re.compile(r'\s+') #el \s coincide con los caracteres de los espacios en blanco
PARAGRAPHS = re.compile(r'<p>(.+?)</a>') # el . hace que coincida con cualquier caracter excepto con una nueva linea
                                        # el ? hace que coincida con uno o con otro, ej ab? a o ab
URLS = re.compile(r'<a href="(.+?)">(.+?)</a>')


def html2markdown(html):
    '''Take in html text as input and return markdown'''
    # re.sub(pattern, repl, string) re.compile guarda el pattern
    # Esta funcion Retorna la cadena obtenida reemplazando las
    # ocurrencias no superpuestas del pattern («patrón») en la
    # string («cadena») por el reemplazo de repl.
    markdown = ITALICS.sub(r'*\1*', html)
    markdown = SPACES.sub(r' ', markdown)
    markdown = PARAGRAPHS.sub(r'\1\n\n', markdown)
    markdown = URLS.sub(r'[\2](\1)', markdown)
    return markdown.strip()
