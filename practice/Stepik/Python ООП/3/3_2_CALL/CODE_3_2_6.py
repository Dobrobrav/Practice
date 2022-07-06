from typing import Literal


class RenderList:
    _type_list: Literal['ul', 'ol']

    def __init__(self, type_list: str):
        if type_list == 'ol':
            self._type_list = 'ol'
        else:
            self._type_list = 'ul'

    def __call__(self, lst: list) -> str:
        """
        Return multiline html-string
        '''<type_list>
        <li>Menu item 1</li>
        <li>Menu item 2</li>
        ...
        <li>Menu item len(lst)</li>
        </type_list>'''
        """
        tag = self._type_list
        html_string = f"<{tag}>\n"
        for menu_item in lst:
            html_string += f"<li>{menu_item}</li>\n"
        html_string += f"</{tag}>"

        return html_string
