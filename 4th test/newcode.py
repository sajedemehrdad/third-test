import pandas as pd
import emoji
# print(pd.__version__)
data = {
    "name": ["sajede", "parham", "farid"],
    "sen": [21,22,33],
    "maghz":["ziad","ziadtar", "kam"]
}
df = pd.DataFrame(data)
# print(df)


pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.set_option('display.width',None)
pd.set_option('display.unicode.east_asian_width',True)
pd.set_option('display.unicode.ambiguous_as_wide',True)
dx = pd.read_excel(r'C:\Users\Ordibehesht\Downloads\بازدید از کارخانه تجهیزات نفتی شرکت انرژی دانا (DOT) (Responses) (4).xlsx')
# print(dx[['Timestamp','نام و نام خانوادگی']])
# print(dx.columns.to_list())
# try:
#     import os
#     print("i found it")
# except ImportError:
#     print("it is not here")

# try:
#     import sys
#     print("i found it")
# except ImportError:
    # print("it is not here")

# import os 
# # current_path = os.getcwd()
# os.mkdir("my_folder")
# with open('my_file.txt','w', encoding="utf-8") as f:
    # print(df, file=f)
    # f.write(df.to_string())?????
print(emoji.emojize(":red_heart:"))
    