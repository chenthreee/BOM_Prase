import re

from paserCollection.ComponentParser import ComponentParser

class VaristorParser(ComponentParser):
    def parse(self, description):
        width_pattern = re.compile(r'(\d+\.?\d*)mm\(\s*宽度\s*\)')
        thru_hole_pattern = re.compile(r'通孔')

        width_match = width_pattern.search(description)
        thru_hole_match = thru_hole_pattern.search(description)

        width = width_match.group(1) + 'mm' if width_match else ''
        thru_hole = True if thru_hole_match else False

        return {
            "type": "Varistor",
            "thru_hole": thru_hole,
            "specification": width
        }