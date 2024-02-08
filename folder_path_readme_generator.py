# generate_folder_structure_readme.py

import os

def process_path(name:str):
    return '/'.join(name.replace(folder_name,'').replace(' ', '%20').split('\\'))[1:]


def dfs(directory, output, folder_indexes,depth=1):
    try:
        ignore_list = ('.git', 'README.md', 'demo.md', 'folder_path_readme_generator.py')
        items = list(filter(lambda x: x not in ignore_list, os.listdir(directory)))
        items = sorted(items,key=lambda x: (os.path.isdir(os.path.join(directory, x))),reverse=True)
        folder_index = 0

        for idx,item in enumerate(items,start=1):
            item_path = os.path.join(directory, item)
            space = ' ' * (depth - 1) * 4

            if os.path.isdir(item_path):
                folder_indexes[-1] = str(int(folder_indexes[-1]) + 1)
                print(f"{space}- {'#' * min(depth, 6)} 第{'-'.join(folder_indexes)}章 [{item}]({process_path(item_path)})",file=output)
                if depth < 9999:
                    dfs(item_path, output,folder_indexes + [str(folder_index)], depth + 1)
            else:
                title = f"{'-'.join(folder_indexes[:-1])}_**{idx:02d}**"
                print(f"{space}- {title} [{item}]({process_path(item_path)})",file=output)

    except OSError:
        print(f"Error reading files in directory: {directory}")


# 設置根目錄和輸出文件名
folder_name = os.path.abspath('.')
output_file_path = os.path.join(folder_name, 'demo.md')

# 開始生成文件夾結構
with open(output_file_path, "w", encoding="utf-8") as output_file:
    dfs(folder_name, output_file,['0'])