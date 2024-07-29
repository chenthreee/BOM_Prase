import re

from paserCollection.ComponentParser import ComponentParser


class TactileSwitchParser(ComponentParser):
    def parse(self, description):
        package_pattern = re.compile(r'(\d+\.?\d*\s*x\s*\d+\.?\d*\s*x\s*\d+\.?\d*mm?)|(\d+\.?\d*\s*x\s*\d+\.?\d*mm)', re.IGNORECASE)
        force_pattern = re.compile(r'(\d+\.?\d*\s*gf)', re.IGNORECASE)

        package_match = package_pattern.search(description)
        force_match = force_pattern.search(description)

        package = package_match.group(0) if package_match else ''
        force = force_match.group(1) if force_match else ''

        return {
            "type": "Tactile Switch",
            "specification": force+" "+package
            # "force": force
        }
