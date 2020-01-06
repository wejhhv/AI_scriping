###DBへのアクセス及び挿入するための関数

#DBは作成されているものとする
#科目コードは文字列で定義している
#SQLアクセス用のモジュールを追加
import MySQLdb
##引数をそれぞれ、授業コード　学部　授業名　授業のURL　教授　校地　単位数とする　科目コードのみ
def Tomysql(num,name1,name2,name3,name4,name5,name6):
    connection =MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="5152wejhhv",
        #予め作ってい置いたDBの名前
        db="python_db",
    #DBに日本語を使う場合のため
        charset="utf8"
    )

    #DB要素の取得
    cursor=connection.cursor()

    #確認用
    print("接続成功")

    #テーブル及びフィールドの作成　変数を使わないver
    """cursor.execute("create table sirabasu3(number varchar(15),name1 varchar(10)\
        ,name2 varchar(300),name3 varchar(300),name4 varchar(10)\
            ,name5 varchar(10),name6 varchar(10))")    """

    #引数の配列の長さを取得
    k=len(name1)
    
    #確認用
    print(k)
    
    #INSERTで配列の値をテーブルに入れる　　変数を使う場合ver
    for i in range(0,k,1):
        cursor.execute("insert into sirabasu3\
            (number,name1,name2,name3,name4,name5,name6)\
                values(%s,%s,%s,%s,%s,%s,%s)",(num[i],name1[i],name2[i],name3[i],name4[i],name5[i],name6[i]))
        
    #更新の確定
    connection.commit()

    #接続を閉じる
    connection.close()
    
    #確認用
    print("接続終了")