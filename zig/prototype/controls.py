class SelectDropdown:
    html = """
            <select class="{1}" id="{0}" >
                {2}
            </select>
                """
    list_option_html = """<option >{0}</option>"""

    def __init__(self, tag_id, css_class, list_items):
        self.list_items = list_items
        self.tag_id = tag_id
        self.css_class = css_class

    def __str__(self):
        htmlcode = ""
        for item in self.list_items:
            htmlcode += (SelectDropdown.list_option_html.format(item))
        return SelectDropdown.html.format(self.tag_id, self.css_class, htmlcode)


