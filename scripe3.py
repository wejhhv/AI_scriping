###シラバスの最初のページのみ情報を配列に格納し、データベースにアクセス
#各ライブラリ読み込み
import selenium
import chromedriver_binary
from selenium import webdriver
import time
#DBに接続するためのモジュール
import access_db

#取得用の配列（リスト)作成　二次元配列でもいいけど後々ややこしくなりそうなので
Subject_Number = []        # 科目ナンバー　
Faculty = []               # 学部
Subject_Name = []          # 科目名
Subject_URL = []           # 科目のURL
Professor = []             # 教授名
Location = []              # 校地の場所　
Credit = []                # 取得できる単位数
Year = []                  # 年度

#使うブラウザの選択
driver = webdriver.Chrome()

#シラバス検索画面のURL
url = "https://syllabus.doshisha.ac.jp/"

#URLの取得、時間がかかる事を考慮して5秒
driver.get(url)
time.sleep(5)

#検索枠の名前から要素の取得
#年度なども同じように設定できる
#YearName = driver.find_element_by_name("select_bussinessyear")
#CourseName = driver.find_element_by_name("courseid")
#SubjectName = driver.find_element_by_name("subjectcd")

KeyName = driver.find_element_by_name("keyword")
MaxName = driver.find_element_by_name("maxdisplaynumber")

#テキスト内の文字を消す、特に最大表示には最初から20が入っているため
KeyName.clear()
MaxName.clear()

#テキスト内に空文字の入力、最大表示数を１０に⇒送信
KeyName.send_keys("")
MaxName.send_keys("50")
KeyName.submit()

#時間をおく
time.sleep(3)

##hHmlのテーブルのtrタグ、tdタグ及びaタグから情報を取り出す
#シラバスのページでは８回目のtrタグから取得する範囲が始まる     tr>td>a:
#要素を確認してリストに追加するかしないかを判断するプログラムに変えるべき
for i in range(7,57,1):
    
    #各trタグにおいてすべての要素を取得　ずっと使うので関数で書いといてもいいかも
    en=driver.find_elements_by_tag_name("tr")[i]

    #各タグの要素からテキストの取得
    a=en.find_elements_by_tag_name("td")[0].text
    b=en.find_elements_by_tag_name("td")[1].text
    c=en.find_elements_by_tag_name("td")[2].find_element_by_tag_name("a").text
    d=en.find_elements_by_tag_name("td")[2].find_element_by_tag_name("a").get_attribute("href") #URLは要素のテキストではなく属性
    e=en.find_elements_by_tag_name("td")[3].text
    f=en.find_elements_by_tag_name("td")[4].text
    g=en.find_elements_by_tag_name("td")[5].text

    #長い文になるので取得と格納を別々にした
    Subject_Number.append(a)   
    Faculty.append(b)             
    Subject_Name.append(c)      
    Subject_URL.append(d)       
    Professor.append(e)      
    Location.append(f)          
    Credit.append(g)

#確認用
"""　　
print(Subject_Number)
print(Faculty)
print(Subject_Name)
print(Subject_URL)
print(Professor)
print(Location)
print(Credit)

リストを表示させる際に\nや\u3000が表示されるが、リスト表示の問題なので単体としてみたときには問題はない
"""

#確認用
print(len(Subject_Number))
print(len(Faculty))
print(len(Subject_Name))
print(len(Subject_URL))
print(len(Professor))
print(len(Location))
print(len(Credit))


#sqlにアクセスして値をDBに入れる
access_db.Tomysql(Subject_Number,Faculty, Subject_Name, Subject_URL, Professor, Location,Credit)

