import re

from paserCollection.ComponentParser import ComponentParser


class CapacitorParser(ComponentParser):
    def parse(self, description):
        capacitance_match = self.parse_and_convert_capacitance(description)
        voltage_pattern = re.compile(r'(\d+\.?\d*\s?[Vv])')
        material_pattern = re.compile(r'(NP0|C0G|NPO|COG|X7R|X5R|Y5V|Z5U)', re.IGNORECASE)
        tolerance_pattern = re.compile(r'±?(\d+\.?\d*%)')

        voltage_match = voltage_pattern.search(description)
        material_match = material_pattern.search(description)
        tolerance_match = tolerance_pattern.search(description)

        voltage = voltage_match.group(1) if voltage_match else ''
        material = material_match.group(1).upper() if material_match else ''
        tolerance = '±' + tolerance_match.group(1) if tolerance_match else ''

        return {
            "type": "Capacitor",
            "specification": capacitance_match + " " + voltage + " " + tolerance + " " + str(material)
            # "capacitance": capacitance,
            # "voltage": voltage,
            # "tolerance": tolerance,
            # "material": material
        }

    def parse_and_convert_capacitance(self,description):
        # 定义电容值的正则表达式，包含不同的 µ 字符
        capacitance_pattern = re.compile(r'(\d+\.?\d*)\s*([pPnNuUμ\u00b5\u03bcmM]?[Ff])', re.UNICODE)

        # 搜索匹配项
        match = capacitance_pattern.search(description)
        if not match:
            return ''
        unit = match.group(2)
        # 提取数值和单位
        if '\u00b5' in unit:
            unit = unit.replace('\u00b5', 'u')
        if '\u03bc' in unit:
            unit = unit.replace('\u03bc', 'u')
        value = float(match.group(1))
        unit = unit.upper()
        # 定义单位转换规则
        unit_multipliers = {
            'PF': 1e-12,
            'NF': 1e-9,
            'UF': 1e-6,
            'MF': 1e-3,
            'F': 1.0
        }

        # 计算数值以法拉为单位
        for u, multiplier in unit_multipliers.items():
            if unit == u:
                value_in_farad = value * multiplier
                break
        else:
            return ''

        # 转换数值和单位
        if value_in_farad < 1e-9:
            value = value_in_farad * 1e12
            new_unit = 'pF'
        elif value_in_farad < 1e-6:
            value = value_in_farad * 1e9
            new_unit = 'nF'
        elif value_in_farad < 1e-3:
            value = value_in_farad * 1e6
            new_unit = 'uF'
        elif value_in_farad < 1.0:
            value = value_in_farad * 1e3
            new_unit = 'mF'
        else:
            value = value_in_farad
            new_unit = 'F'

        return f"{value:g}{new_unit}"

# CapacitorParser = CapacitorParser()
# if __name__ == '__main__':
#     desc = 'MSAST105SB5104KFNA01 MLCC 0.1μF ±10% 25V X5R 0402'
#     print(CapacitorParser.parse(desc))