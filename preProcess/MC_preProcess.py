import fnmatch
import os

import pandas as pd


def MC_preProcess(MC_BOM_file):
    # 读取第一个Excel文件
    # file1 = str(input("请输入主BOM文件名：")) + '.xlsx'
    file1 = MC_BOM_file
    df1 = pd.read_excel(file1)
    file2 = ''
    file_directory = os.path.dirname(file1)
    file_name = os.path.basename(file1)
    first_word = file_name.split()[0]
    # 遍历文件夹中的所有Excel文件
    for root, dirs, files in os.walk(file_directory):
        for filename in fnmatch.filter(files, '*.xlsx'):
            if first_word in filename and filename != file_name:
                file2 = os.path.join(root, filename)

    preview = pd.read_excel(file2, nrows=20)  # 假设前10行内能找到列标题

    # 找到包含 'Comment' 的行号
    header_row_index = 0
    for i, row in preview.iterrows():
        if 'Comment' in row.values:
            header_row_index = i
            break

    if header_row_index != 0:
        df2 = pd.read_excel(file2, skiprows=header_row_index + 1)
    else:
        print("未找到包含 'Comment' 的列标题行。")

    # df2 = pd.read_excel(file2, skiprows=skiprows_value)

    df1['Footprint'] = None
    df1['Designator'] = None

    # 遍历第一个数据框的每一行
    for i, row in df1.iterrows():
        key_value = row['CAD']
        if key_value != '':
            # 在第二个数据框中进行查询
            matched_row = df2[df2['Comment'] == key_value]

            if not matched_row.empty:
                # 获取第三列和第四列的数据
                column3_value = matched_row.iloc[0]['Footprint']
                column4_value = matched_row.iloc[0]['Designator']
                df1.at[i, 'Footprint'] = column3_value
                df1.at[i, 'Designator'] = column4_value
    # 遍历df1，如果CAD列为空，则复制上一行的指定列
    columns_to_copy = ['CAD', 'Description', 'Calc. quantity', 'Footprint', 'Designator']

    for i in range(1, len(df1)):  # 从第二行开始遍历
        if pd.isna(df1.at[i, 'CAD']):
            for column in columns_to_copy:
                df1.at[i, column] = df1.at[i - 1, column]

    new_rows = []

    # 遍历每一行
    for index, row in df1.iterrows():
        articles = str(row['Manufacturer article']).split('|')
        for article in articles:
            new_row = row.copy()
            new_row['Manufacturer article'] = article.strip()
            new_rows.append(new_row)

    # 将处理后的数据转换为DataFrame
    new_df = pd.DataFrame(new_rows)

    new_df.to_excel(os.path.join(file_directory, 'MC预处理原始BOM.xlsx'), index=False)
    return os.path.join(file_directory, 'MC预处理原始BOM.xlsx'),len(new_df)
