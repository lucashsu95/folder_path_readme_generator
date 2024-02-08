# generate_folder_structure_readme.py

import os

def process_path(n:str):
    path = ''
    for i in n.replace(folder_name,''): # 替換空格
        path += '%20' if i == ' ' else i
    return path[1:].replace("\\","/") # 去掉根目錄，把反斜線換成斜線
    

# def process_path(path):
#     """處理路徑，替換空格為 %20 並將反斜線換成斜線"""
#     return path.replace(' ', '%20').replace("\\", "/")[1:]


def dfs(directory, output, folderIdxs,depth=1):
    try:
        items = os.listdir(directory)
        flag = 0
        for idx,item in enumerate(items,start=1):
            if item in ('.git','README.md','demo.md','folder_path_readme_generator.py'): continue
            item_path = os.path.join(directory, item)
            space = ' ' * (depth - 1) * 4

            if os.path.isdir(item_path):
                folderIdxs[-1] = str(int(folderIdxs[-1]) + 1)

                print(f"{space}- {'#' * min(depth, 7)} 第{'-'.join(folderIdxs)}章 [{item}]({process_path(item_path)})", file=output)
                if depth < 9999:
                    dfs(item_path, output,folderIdxs + [str(flag)], depth=depth + 1)
            else:
                title = f"{'-'.join(folderIdxs[:-1])}_**{idx:02d}**"
                print(f"{space}- {title} [{item}]({process_path(item_path)})", file=output)

    except OSError:
        print(f"Error reading files in directory: {directory}")


# 設置根目錄和輸出文件名
folder_name = os.path.abspath('.')
output_file_path = os.path.join(folder_name, 'demo.md')

# 開始生成文件夾結構
with open(output_file_path, "w", encoding="utf-8") as output_file:
    dfs(folder_name, output_file,['0'])
