import re

from paserCollection.ComponentParser import ComponentParser


class SafetyCapacitorParser(ComponentParser):
    def parse(self, description):
        capacitance_pattern = re.compile(r'(\d+\.?\d*\s?(?:[pPnNuUmM]?[Ff]))')
        voltage_pattern = re.compile(r'(\d+\.?\d*\s?[Vv])')
        tolerance_pattern = re.compile(r'±(\d+\.?\d*%)')

        capacitance_match = capacitance_pattern.search(description)
        voltage_match = voltage_pattern.search(description)
        tolerance_match = tolerance_pattern.search(description)

        capacitance = capacitance_match.group(1).upper() if capacitance_match else ''
        voltage = voltage_match.group(1).upper() if voltage_match else ''
        tolerance = tolerance_match.group(1) if tolerance_match else ''

        return {
            "type": "Safety Capacitor",
            "specification": capacitance + ' ' + str(voltage) + ' ' + tolerance
            # "voltage": voltage,
            # "tolerance": tolerance
        }
