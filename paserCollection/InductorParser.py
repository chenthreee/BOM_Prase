import re

from paserCollection.ComponentParser import ComponentParser


class InductorParser(ComponentParser):
    def parse(self, description):
        inductance_pattern = re.compile(r'(\d+\.?\d*\s*[µuUnNpPmM]*[Hh])', re.IGNORECASE)
        tolerance_pattern = re.compile(r'(\d+\.?\d*\s*%)', re.IGNORECASE)

        inductance_match = inductance_pattern.search(description)
        tolerance_match = tolerance_pattern.search(description)

        inductance = inductance_match.group(1) if inductance_match else ''
        tolerance = '±' +tolerance_match.group(1) if tolerance_match else ''

        return {
            "type": "Inductor",
            "specification": inductance+' '+tolerance
            # "tolerance": tolerance
        }
