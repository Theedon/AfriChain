from io import StringIO

from markdown import Markdown


def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        # Remove any occurrences of "sql" (case-insensitive)
        stream.write(element.text.lower().replace("sql", ""))
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail.lower().replace("sql", ""))
    return stream.getvalue()


# patching Markdown
Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False


def unmark(text):
    return __md.convert(text)
