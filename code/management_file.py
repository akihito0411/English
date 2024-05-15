import sqlite3
import glob
import os

#file_name.dbを作成する
def create_file(file_path):
    #データベース接続
    conn = sqlite3.connect(file_path)
    #カーソル取得
    cursor = conn.cursor()
    #テーブル作成のコード
    create_file = """
    CREATE TABLE IF NOT EXISTS file_name(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
    );
    """
    #テーブルの作成
    cursor.execute(create_file)
    #コミット
    conn.commit()
    #接続を閉じる
    conn.close()
    #データベースファイルのパス
    #file_path = "path/to/your/database.db"
    #データベース作成
    #create\file(file_paht)

def upload_file(file_path,user_id,new_name,new_age):
    try:
        #データベース接続
        conn = sqlite3.connect(file_path)
        #カーソル取得
        cursor = conn.corsor()
        #更新のSQLのコード
        upload_sql = """
        UPDATE file_name
        SET name = ?,
            age = ?
        WHERE id = ?
        """
        #?には更新したい値が入る

        #パラメータを指定してSQL文を実行
        cursor.execute(upload_sql,(new_name,new_age,user_id))
        #コミット
        conn.commit()
        #接続を閉じる
        conn.close()
        print("データをを更新しました")
    except Exception as e:
        print(f"データの更新中にエラーが発生しました:{e}")

        #データベースファイルのパス
        #file_path = "path/to/your/database.db"
        #更新するユーザーのIDと新しい乗
        #user_id_to_update = 1
        #new_name = "Bob"
        #new_age = 25
        #データの更新
        #upload_file(file_path,user_id_to_update,new_name,new_age)

def search_file(file_name):
    #現在のディレクトリを取得
    current_dir = os.getcwd()
    #DBファイルのパスを取得
    file_path = os.path.join(current_dir,file_name)
    return file_path
    #DBファイルの名前
    #file_name = "example.db"
    #DBファイルのパスを取得
    #file_path = search_file(file_name)
    #print(f"DBファイルのパス:{file_path}")

def delete_file(file_path):
    try:
        #ファイルが存在するかチェック
        if os.path.exists(file_path):
            #ファイルの削除
            os.remove(file_path)
            print(f"ファイル '{file_path}'を削除しました")
        else:
            print(f"ファイル '{file_path}'は存在しません")
    except Exception as e: #エラー検出
        print(f"ファイルの削除中にエラーが発生しました: {e}")

    #データベースファイルのパス
    #file_path = "path/to/your/database.db"
    #delete_file(file_path)

def main():
    file_path = "\English\homework\TEST.db"
    create_file(file_path)

if (__name__ == "__main__"):
    main()