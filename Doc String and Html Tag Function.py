def html_tag(text, html_tag):
    """
    Generate or return text with desire html tag
    :param text: text that want to add html tag
    :param html_tag: tag which is used to add on text
    :return: html tag
    """
    html = f'<{html_tag}> {text} </{html_tag}>'
    return html
print(html_tag.__doc__)
print(html_tag("This is H1 Tag", "h1"))
print(html_tag("This is H2 Tag", "h2"))
print(html_tag("This is paragraph Tag", "p"))
print(html_tag("This is strong Tag", "strong"))
