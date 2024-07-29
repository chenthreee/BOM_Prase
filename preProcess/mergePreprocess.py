import os

import pandas as pd


# 定义一个函数来合并行
def merge_rows(group, part_col_name):
    merged_row = {}
    for col in group.columns:

        if col != part_col_name:
            unique_values = group[col].dropna().unique()
            merged_row[col] = ','.join(map(str, unique_values))
        else:
            merged_row[col] = group[col].iloc[0]
    merged_row['COUNT'] = len(group)
    return pd.Series(merged_row)


def merge_preprocess(file_path, header_row, part_num_col):
    df = pd.read_excel(file_path, header=header_row)
    part_col_name = df.columns[part_num_col]
    merged_df = df.groupby(part_col_name).apply(lambda group: merge_rows(group, part_col_name)).reset_index(drop=True)

    file_dir, file_name = os.path.split(file_path)
    file_base, file_ext = os.path.splitext(file_name)
    output_file_path = os.path.join(file_dir, f"{file_base}_merge_preprocess{file_ext}")

    columns = list(merged_df.columns)
    columns.remove('COUNT')
    columns.append('COUNT')
    merged_df = merged_df[columns]

    merged_df.to_excel(output_file_path, index=False)
    count_col_index = merged_df.columns.get_loc('COUNT') + 1
    return output_file_path, count_col_index-1

# mergeProcess()
