import imp
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
os.environ["NLS_LANG"] = ".AL32UTF8"

driver.get("https://map.kakao.com/")
# search = 카카오맵의 검색창
search = driver.find_element_by_name("q")
search.clear()
search.send_keys("금천구 식당")
search.send_keys(Keys.ENTER)
sleep(2)

b = 1 #무한루프 확인용 리스트 블록 인덱스

# 1페이지부터 34페이지까지 크롤링
# 이렇게 하면 종료될때 프로그램이 뻗으면서 하드랜딩하게 되는데 소프트랜딩할 방법을 생각해보자.
while b<=7 :
        
    sleep(2)
    
    #리스트 블록 안에서 1페이지~5페이지까지 돌면서 크롤링해옴
    l = 1 #'리스트' 페이지를 위한 인덱스
    while l<=5 :    
        sleep(2)
        
        # 리스트 한페이지의 업체'상세보기'(15개)를 차례대로 들어가면서 크롤링해옴
        i = 1 #'상세보기' 요소를 위한 인덱스
        while i<=16:    
            # detail_page = 상세보기 요소
            # li 태그 안에 상세보기 요소가 없다면 예외처리(광고로 판정)
            detail_page_xpath = '//*[@id="info.search.place.list"]/li['+str(i)+']/div[5]/div[4]/a[1]'
            try:
                detail_page = driver.find_element_by_xpath(detail_page_xpath)
            except Exception:
                i = i+1
                continue
            
            # idx = 상세보기에 링크된 주소
            idx = detail_page.get_attribute("href")
            #print("#링크된 주소#", idx)
            lIdx = str(idx).split('/')
            #print("/로 split", lIdx)
            idx = lIdx[-1].strip() # 공백제거
            #print(idx)
            print("###idx 파싱완료###", idx)
            # 최종적으로 idx가 식당 인덱스
            
            detail_page.send_keys(Keys.ENTER)
            # 새 탭 열림
            driver.switch_to.window(driver.window_handles[1])
            sleep(2)
            
            # place = 식당 이름
            place_xpath = '//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/h2'
            place = driver.find_element_by_xpath(place_xpath).get_attribute("textContent")
            place = str(place).strip() # 공백제거
            print("###식당이름 파싱완료###", place) #### place 파싱할 예정
            # 최종적으로 place가 식당 이름
            
            # address = 식당 주소
            addr_xpath = '//*[@id="mArticle"]/div[1]/div[2]/div[1]/div/span[1]'
            address = driver.find_element_by_xpath(addr_xpath).get_attribute("innerText")
            #print("#식당주소#", address)
            iAddr = str(address).find('(우)') #우편번호를 제거하기 위해 (우)를 찾음
            if iAddr != -1:
                address = str(address)[0:iAddr]
            address = address.strip() #공백제거
            print("###식당주소 파싱완료###", address)            
            
            # plcNum = 식당 전화번호
            # 식당 전화번호 없을 시 예외처리(null값 입력)
            try :
                plcNum_xpath = '//*[@id="mArticle"]/div[1]/div[2]/div[4]/div/div/span/span[1]'
                plcNum = driver.find_element_by_xpath(plcNum_xpath).get_attribute("innerText")
                plcNum = str(plcNum).strip() #공백제거
                print("###식당전화번호 파싱완료###", plcNum) #### plcNum 파싱할 예정
            except Exception :
                plcNum = "null"
                print("###식당전화번호 없는 경우###", plcNum)

            ################### 영업시간 ###################

            # 영업날짜(요일)&시간
            # 영업시간 없을시 예외처리(null값 입력)
            try :
                operTime_xpath = '//*[@id="mArticle"]/div[1]/div[2]/div[2]/div/div[1]/ul/li/span'
                operTime = driver.find_element_by_xpath(operTime_xpath).get_attribute("textContent")
                operTime = str(operTime).strip()
                print('###영업날짜(요일)&시간 파싱완료###', operTime)
            except Exception :
                operTime = "null"
                print('###영업시간,요일 없는 경우###', operTime)

            # 휴무일
            # 영업시간 더보기 버튼이 존재하지 않을경우 예외처리(null값 입력)
            # 안나오거나 규격에 맞지 않는 업체가 많아 뺌
            # try:        
            #     dayOff_xpath = '//*[@id="mArticle"]/div[1]/div[2]/div[2]/div/div[2]/div/ul[2]/li'
            #     dayOff = driver.find_element_by_xpath(dayOff_xpath).get_attribute("innerText")
            #     print('#휴무일#', dayOff)
            # except Exception :
            #     dayOff = "null"
            #     print('###휴무일 값 없음###', dayOff)

            #################### 메뉴 가져오기 ####################

            m = 1 #xpath를 사용하므로 li태그를 1번부터 마지막까지 무한루프 돌리기위함
            menus = "" #메뉴만 파싱해서 쭉 연결할 예정
            prices = "" #가격만 파싱해서 쭉 연결할 예정
            while True :    
                #menu_xpath = '//*[@id="mArticle"]/div[3]/ul/li[1]/div'
                # 메뉴를 끝까지 크롤링하면 탈출
                try :
                    #메뉴이름+가격 통째로
                    #menu_xpath = '//*[@id="mArticle"]/div[3]/ul/li['+str(m)+']/div'
                    #menu = driver.find_element_by_xpath(menu_xpath).get_attribute("innerText") 
                    #print('#메뉴'+str(m)+'#', menu)
                    
                    # 메뉴 이름
                    menuName_xpath = '//*[@id="mArticle"]/div[3]/ul/li['+str(m)+']/div/span'
                    menuName = driver.find_element_by_xpath(menuName_xpath).get_attribute("innerText")
                    menuName = str(menuName).strip() #공백제거
                    #print('#메뉴이름#', menuName)
                    menus = menus + menuName + '|'
                    try :
                        # 메뉴 가격
                        price_xpath = '//*[@id="mArticle"]/div[3]/ul/li['+str(m)+']/div/em[2]'
                        price = driver.find_element_by_xpath(price_xpath).get_attribute("innerText")
                        price = str(price).strip() #공백제거
                        price = price.split('\n')[1] #가격:\n18,000 에서 순수한 가격만 추출
                        #print('#메뉴가격#', price)
                        prices = prices + price + '|'
                    except Exception :
                        prices = "null|"
                    
                except Exception :
                    menus = menus[:-1] #마지막 파이프(|)를 제거
                    prices = prices[:-1] #마지막 파이프(|)를 제거
                    break
                m = m+1
            print('###메뉴 이름을 문자열로 연결###', menus)
            print('###메뉴 가격을 문자열로 연결###', prices)
                
            # 창닫기
            driver.close()
            # 첫번째 탭으로 이동
            driver.switch_to.window(driver.window_handles[0])
            # 상세보기 버튼요소의 인덱스 증가
            i = i+1    
        
        # 지도 리스트의 더보기 버튼 누르기(2페이지로 자동이동)
        # 없으면 3,4,5,... 페이지로 이동
        
        l = l+1
        try :
            moreList_xpath = '//*[@id="info.search.place.more"]'
            moreList = driver.find_element_by_xpath(moreList_xpath).send_keys(Keys.RETURN)
            print(str(l)+"페이지 이동")
            continue
        except Exception :
            print(str(l)+"페이지 이동")
        try :
            nextList_xpath = '//*[@id="info.search.page.no'+str(l)+'"]'
            nextList = driver.find_element_by_xpath(nextList_xpath).send_keys(Keys.RETURN)
            continue
        except Exception : #블록내에 다음(6번째) 페이지번호가 없음            

            print(str(b)+"번째 블록 완료")
            b = b+1         
            break

    nextBlock_xpath = '//*[@id="info.search.page.next"]'
    nextBlock = driver.find_element_by_xpath(nextBlock_xpath).send_keys(Keys.RETURN)

print("크롤링 종료.")