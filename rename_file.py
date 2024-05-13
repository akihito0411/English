import os

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"ファイル名が '{old_name}' から '{new_name}' に変更されました。")
    except OSError as e:
        print(f"ファイル名の変更中にエラーが発生しました: {e}")

# 変更前のファイル名と変更後のファイル名を指定
old_name = "old_file.txt"
new_name = "new_file.txt"

# ファイル名を変更
rename_file(old_name, new_name)
