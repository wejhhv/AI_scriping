###scripe2の内容について、ＤＢへのアクセスはせずすべてtxtファイル上に書き込んだもの  ファイル入力の部分が未完成
#各ライブラリ読み込み
import selenium
import chromedriver_binary
from selenium import webdriver
import time
import filewrite

#DBアクセス用モジュール
#import access_db
#経過時間の取得
Start_Time=time.time()

#取得用の配列（リスト)作成
Subject_Number = []        # 科目ナンバー　
Faculty = []               # 学部
Subject_Name = []          # 科目名
Subject_URL = []           # 科目のURL
Professor = []             # 教授名
Location = []              # 校地　今出川or京田辺
Credit = []                # 取得できる単位数
Year = []                  # 年度

#使うブラウザの選択
driver = webdriver.Chrome()

#シラバス検索画面のURL
url = "https://syllabus.doshisha.ac.jp/"

#URLを開く、時間を考慮して5秒
driver.get(url)
time.sleep(5)

#検索枠の名前から要素の取得
#年度なども同じように設定できる
#YearName = driver.find_element_by_name("select_bussinessyear")
#CourseName = driver.find_element_by_name("courseid")
#SubjectName = driver.find_element_by_name("subjectcd")

KeyName = driver.find_element_by_name("keyword")
MaxName = driver.find_element_by_name("maxdisplaynumber")

#テキスト内の文字を消す、特に最大表示には最初から20が入っている
KeyName.clear()
MaxName.clear()

#テキスト内に空文字の入力、最大表示数を200に設定→送信
KeyName.send_keys("")
MaxName.send_keys("200")
KeyName.submit()


#時間を考慮
time.sleep(5)

##htmlのテーブルのtrタグ、tdタグ及びaタグから情報を取り出す
#シラバスのページでは８回目のtrタグから取得する範囲が始まる     tr>td>a:
#要素を確認してリストに追加するかしないかを判断するプログラムに変えるべき
for i in range(7,207,1):
    
    #各trタグにおいてすべての要素を取得
    en=driver.find_elements_by_tag_name("tr")[i]

    #各タグの要素からテキストの取得
    a=en.find_elements_by_tag_name("td")[0].text
    b=en.find_elements_by_tag_name("td")[1].text
    c=en.find_elements_by_tag_name("td")[2].find_element_by_tag_name("a").text
    d=en.find_elements_by_tag_name("td")[2].find_element_by_tag_name("a").get_attribute("href") #URLは要素のテキストではなく属性
    e=en.find_elements_by_tag_name("td")[3].text
    f=en.find_elements_by_tag_name("td")[4].text
    g=en.find_elements_by_tag_name("td")[5].text
    
    #同ディレクトリのpythonファイルからファイルへ読み込む関数を呼び出す
    filewrite.FileWrite(a,b,c,d,e,f,g)
    
    #長い文になるので取得と格納を別々にした
    Subject_Number.append(a)   
    Faculty.append(b)             
    Subject_Name.append(c)      
    Subject_URL.append(d)       
    Professor.append(e)      
    Location.append(f)          
    Credit.append(g)

#確認用
print(Subject_Number)
print(Faculty)
print(Subject_Name)
print(Subject_URL)
print(Professor)
print(Location)
print(Credit)

#時間取得 これから進捗状況を段階的に表示する
First_Time=time.time()
#計算して表示
print("途中経過"+1/94*100+"% 終了　経過時間"+(First_Time)-(Start_Time)+"秒")



##２ページ目以降のページ転移を繰り返しながらリストに格納
#最大表示が200の時のページ数は最大94なのでそれを超えれば終了するように
page=2

while page!=-1:  #絶対にとりえない値で回す

    #数を固定しているが終了判定のための要素の有無を取得できるメゾットが欲しい i＝95の時要素を返すかどうかを判定するものが存在するはず
    page = page + 1
    
    
    if  page==95:
        break

    
    ##２ページ目以降の情報について格納する
    for i in range(7,207,1):
    
        #各trタグにおいてすべての要素を取得
        en=driver.find_elements_by_tag_name("tr")[i]

        #各タグの要素からテキストの取得

        a=en.find_elements_by_tag_name("td")[0].text
        b=en.find_elements_by_tag_name("td")[1].text
        c=en.find_elements_by_tag_name("td")[2].find_element_by_tag_name("a").text
        d=en.find_elements_by_tag_name("td")[2].find_element_by_tag_name("a").get_attribute("href") #URLは要素のテキストではなく属性
        e=en.find_elements_by_tag_name("td")[3].text
        f=en.find_elements_by_tag_name("td")[4].text
        g=en.find_elements_by_tag_name("td")[5].text

        
        #テキストファイルへの書き込み
        filewrite.FileWrite(a,b,c,d,e,f,g)
        #長い文になるので取得と格納を別々にした
        Subject_Number.append(a)   
        Faculty.append(b)             
        Subject_Name.append(c)      
        Subject_URL.append(d)       
        Professor.append(e)      
        Location.append(f)          
        Credit.append(g)
    
    #ページ転移
    PageName = driver.find_element_by_name("selectNum")
    PageName.send_keys(i)
    PageName.submit()     


    #数秒待って情報の取得
    time.sleep(3)

    #実際にどれぐらい時間がかかるかわからないので経過時間を5pageごとに経過時間を表示させる   
    if i%5==0:
        #時間取得
        End_Time=time.time()
        #計算して表示
        print("途中経過"+i/94*100+"% 終了　経過時間"+(End_Time)-(Start_Time)+"秒")



#確認用
print("データの取得が終了しました")

#確認用  すべて2019年度の総授業数の18610になっていればよい
print(len(Subject_Number))
print(len(Faculty))
print(len(Subject_Name))
print(len(Subject_URL))
print(len(Professor))
print(len(Location))
print(len(Credit))

##データベース（mysql）へのアクセス
#access_db.pyのTOmysql関数を利用する
#access_db.Tomysql(Subject_Number,Faculty, Subject_Name, Subject_URL, Professor, Location,Credit)