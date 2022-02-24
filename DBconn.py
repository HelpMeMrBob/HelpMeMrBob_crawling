import cx_Oracle
import os

# 한글지원
# os.putenv('NLS_LANG', '.UTF8')
#os.environ["NLS_LANG"] = ".AL32UTF8"

# 함수 정의
def connect(idx,food,place,address,plcNum,menu,price,operTime):
    
    sql = "INSERT INTO restaurant(idx,food,place,address,plcNum,menu,price,operTime) VALUES (:idx,:food,:place,:address,:plcNum,:menu,:price,:operTime)"
    
    # path 설정
    # LOCATION = r"C:\01DevelopKits\InstantClient\instantclient_21_3"
    # os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"] #환경변수 등록
    
    try :    
        # 라이브러리 연결
        # cx_Oracle.init_oracle_client(lib_dir=r"C:\01DevelopKits\InstantClient\instantclient_21_3")
        # 연결에 필요한 기본 정보(유저, 비밀번호, 데이터베이스 서버 주소)  
        # con_ip = 'localhost:1521/xe'
        # con_id = 'final'
        # con_pw = '1234'
        # connection = cx_Oracle.connect(con_id, con_pw, con_ip)
        # print(connection.version)
        # cursor = connection.cursor()
        # cursor.execute(sql)
        
        with cx_Oracle.connect('final','1234','localhost:1521/xe',encoding='UTF-8') as connection:
            
            with connection.cursor() as cursor:
                cursor.execute(sql, [idx,food,place,address,plcNum,menu,price,operTime])
                print("@@@입력완료",str(cursor.rowcount)+"행 입력")
                connection.commit()
                
    except cx_Oracle.Error as error :
        print('!!!에러 발생 :', error)
    

    



