

# df1 = pd.read_excel('CONCORADANCE_20240117.xlsx')
# df1['cc'] = df1['cc'].ffill()
# df = df1.drop_duplicates(subset=['cc', 'kc'])
# print('lin')
# df.to_csv('csv_data.csv', index=False)

import pandas as pd

df1 = pd.read_excel('CONCORADANCE_20240117.xlsx', usecols=['cc', 'kc'])
df2 = pd.read_excel('CONCORADANCE_20240131.xlsx', usecols=['cc', 'kc'])
df1['cc']= df1['cc'].ffill()
df2['cc'] = df2['cc'].ffill()
if not df1.equals(df2):
    diff_data = pd.concat([df1, df2]).drop_duplicates(keep=False)
    print(diff_data)
#     al = diff_data[diff_data['cc'] == 'AL'].index
#     if al.empty:
#         diff_data.to_csv('diff_data_whole.csv', index=False)
#         print('both the files have the same')
#     else:
#         first_file = diff_data.iloc[:al[1]]
#         second_file = diff_data.iloc[al[1]:]
#         first_file.to_csv('file_117.csv', index=False)
#         second_file.to_csv('file_131.csv', index=False)
#     # diff_data.to_csv('diff_data_n.csv', index=False)
#         print('difference data is saved into two files')
    

# # li = ['tea', 'eat', 'ate', 'top', 'pot']



# import pandas as pd
# import json

# def compare_excel_files(file1, file2):
#     # Read the Excel files into pandas dataframes
#     df1 = pd.read_excel(file1)
#     df2 = pd.read_excel(file2)

#     # Compare the dataframes
#     diff_data = {}

#     # Iterate over each row in both dataframes
#     for index, row in df1.iterrows():
#         if index not in df2.index:
#             diff_data[index] = {'in_file1': row.to_dict(), 'in_file2': None}
#         else:
#             for col in df1.columns:
#                 if row[col] != df2.loc[index, col]:
#                     if index not in diff_data:
#                         diff_data[index] = {'in_file1': row.to_dict(), 'in_file2': df2.loc[index].to_dict()}
#                     else:
#                         diff_data[index]['in_file2'] = df2.loc[index].to_dict()

#     # Add rows present in df2 but not in df1
#     for index, row in df2.iterrows():
#         if index not in df1.index:
#             diff_data[index] = {'in_file1': None, 'in_file2': row.to_dict()}

#     # Convert the differential data to JSON format
#     json_data = json.dumps(diff_data, indent=4)
    
#     return json_data

# # Example usage
# file1 = 'CONCORADANCE_20240117.xlsx'
# file2 = 'CONCORADANCE_20240131.xlsx'

# json_diff = compare_excel_files(file1, file2)

# # Write the differential data to a JSON file
# with open('differential_data.json', 'w') as json_file:
#     json_file.write(json_diff)