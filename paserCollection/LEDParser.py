import re

from paserCollection.ComponentParser import ComponentParser


class LEDParser(ComponentParser):
    def parse(self, description):
        color_pattern = re.compile(r'(红|red|绿|green|蓝|blue|黄|yellow|白|white|橙|orange|紫|purple|粉|pink)', re.IGNORECASE)

        color_match = color_pattern.search(description.lower())

        color = color_match.group(1).lower() if color_match else ''

        return {
            "type": "LED",
            "specification": color
        }
