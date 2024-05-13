import os

def search_files_by_name(directory, filename):
    found_files = []
    for file in os.listdir(directory):
        if filename in file:
            found_files.append(os.path.join(directory, file))
    return found_files

# 検索を行うディレクトリと検索するファイル名を指定
directory = "/path/to/search"
filename = "example.txt"

# 指定されたディレクトリ内でファイル名を含むファイルを検索
result = search_files_by_name(directory, filename)
print("Found files:")
for file in result:
    print(file)
