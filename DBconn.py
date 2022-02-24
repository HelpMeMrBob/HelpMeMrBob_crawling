import cx_Oracle
import os

# 한글지원
os.putenv('NLS_LANG', '.UTF8')
#os.environ["NLS_LANG"] = ".AL32UTF8"

# path 설정
LOCATION = r"C:\01DevelopKits\InstantClient\instantclient_21_3"
os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"] #환경변수 등록
connect = cx_Oracle.connect("")


# 함수 정의
def connect():
    # path 설정
    LOCATION = r"C:\01DevelopKits\InstantClient\instantclient_21_3"
    os.environ["PATH"] = LOCATION + ";" + os.environ["PATH"] #환경변수 등록
    
	#라이브러리 연결
    #cx_Oracle.init_oracle_client(lib_dir=r"C:\01DevelopKits\InstantClient\instantclient_21_3")
         
    con_ip='localhost:1521/final'
    con_id='final'
    con_pw='1234'
 
    #연결에 필요한 기본 정보(유저, 비밀번호, 데이터베이스 서버 주소)
    connection = cx_Oracle.connect(con_id, con_pw, "jdbc:oracle:thin:@localhost:1521:xe")
    cursor = connection.cursor()
    cursor.execute("")

    for list in cursor:
        print(list)

    cursor.close()
    connection.close()
    
# 함수 실행    
connect()



