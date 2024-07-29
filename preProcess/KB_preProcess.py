def KB_manufacturer_process(description_list):
    temp_manufacturer = []
    for description in description_list:
        parts = description.split('-')
        last_part = parts[-1]
        temp_manufacturer.append(last_part)
    return temp_manufacturer

