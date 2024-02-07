# generate_folder_structure_readme.py

import os

def processStr(n:str):
    newSt = ''
    for i in n.replace(root_path,''): # 替換空格
        newSt += '%20' if i == ' ' else i
    return newSt[1:].replace("\\","/") # 去掉根目錄，把反斜線換成斜線


def dfs(directory, output, folderIdxs,depth=1):
    try:
        items = os.listdir(directory)
        flag = 0
        for idx,item in enumerate(items,start=1):
            if item in gitignore: continue
            item_path = os.path.join(directory, item)
            space = ' ' * (depth-1) * 4

            if os.path.isdir(item_path):
                folderIdxs[-1] = str(int(folderIdxs[-1]) + 1)
                number = '#' * depth if depth < 7 else ''

                print(f"{space}- {number} 第{'-'.join(folderIdxs)}章 {item}", file=output)
                dfs(item_path, output,folderIdxs + [str(flag)], depth=depth + 1)
            else:
                title = f"{'-'.join(folderIdxs[:-1])}_**{idx:02d}**"
                print(f"{space}- {title} [{item}]({processStr(item_path)})", file=output)

    except OSError:
        print(f"Error reading files in directory: {directory}")

gitignore = ['.git','README.md','folder_path_readme_generator.py','folder_path_readme_generator1.py','demo.md'] # 要忽略的檔案
folder_name = os.path.abspath('.')
root_path = f'{folder_name}'
output = open(f"{folder_name}/demo.md", "w", encoding="utf-8")
dfs(root_path, output,['0'])
output.close()