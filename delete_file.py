import os

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"ファイル '{filename}' が削除されました。")
    except OSError as e:
        print(f"ファイルの削除中にエラーが発生しました: {e}")

# 削除するファイルのパスを指定
filename = "file_to_delete.txt"

# ファイルを削除
delete_file(filename)
