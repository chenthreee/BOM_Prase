import re

from paserCollection.ComponentParser import ComponentParser


class MOSFETParser(ComponentParser):
    def parse(self, description):
        n_channel_pattern = re.compile(r'N[\-\s]?沟道|N[\-\s]?channel', re.IGNORECASE)
        p_channel_pattern = re.compile(r'P[\-\s]?沟道|P[\-\s]?channel', re.IGNORECASE)

        n_channel_match = n_channel_pattern.search(description)
        p_channel_match = p_channel_pattern.search(description)

        if n_channel_match:
            channel_type = "N沟道"
        elif p_channel_match:
            channel_type = "P沟道"
        else:
            channel_type = ''

        return {
            "type": "MOSFET",
            "specification": channel_type
        }
