# generate_folder_structure_readme.py

import os

def processStr(n:str):
    newSt = ''
    for i in n.replace(root_path,''): # 替換空格
        newSt += '%20' if i == ' ' else i
    return newSt[1:].replace("\\","/") # 去掉根目錄，把反斜線換成斜線


def dfs(directory, output, depth=1):
    global sec_id
    try:
        items = os.listdir(directory)
        for item_idx, item in enumerate(items, start=1):
            if item in gitignore:
                continue
            item_path = os.path.join(directory, item)

            space = ' ' * (depth-1) * 4
            if os.path.isdir(item_path):
                title = f"第{sec_id}章"
                print(f"{space}- # {title} {item}", "\n", file=output)
                dfs(item_path, output, depth=depth + 1)
            else:
                title = f"{sec_id:02d}-{item_idx}"
                print(f"{space}- {title} [{item}]({processStr(item_path)})", file=output)

            if depth == 1:
                sec_id += 1

        # print("\n", file=output)

    except OSError:
        print(f"Error reading files in directory: {directory}")

gitignore = ['.git','README.md','folder_path_readme_generator.py','demo.md'] # 要忽略的檔案
sec_id = 1
folder_name = os.path.abspath('.')
root_path = f'{folder_name}'
output = open(f"{folder_name}/demo.md", "w", encoding="utf-8")
dfs(root_path, output)
output.close()