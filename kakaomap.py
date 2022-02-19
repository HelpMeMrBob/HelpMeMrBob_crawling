from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')


driver.get("https://map.kakao.com/")
# search = 카카오맵의 검색창
search = driver.find_element_by_name("q")
search.clear()
search.send_keys("금천구 식당")
search.send_keys(Keys.ENTER)
sleep(1)
# detail_page = 상세보기 요소
detail_page_xpath = '//*[@id="info.search.place.list"]/li[1]/div[5]/div[4]/a[1]'
detail_page = driver.find_element_by_xpath(detail_page_xpath)
# addr = 상세보기에 링크된 주소
addr = detail_page.get_attribute("href")
print("##링크된 주소##", addr) #### idx 파싱할 예정
detail_page.send_keys(Keys.ENTER)

#### 파싱할때 없는 항목을 대비해서 조건문을 작성할것.

# 새 탭 열림
driver.switch_to.window(driver.window_handles[-1])
sleep(1)
# place = 식당 이름
place_xpath = '//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/h2'
place = driver.find_element_by_xpath(place_xpath).get_attribute("textContent")
print("##식당이름##", place) #### place 파싱할 예정
# address = 식당 주소
addr_xpath = '//*[@id="mArticle"]/div[1]/div[2]/div[1]/div/span[1]'
address = driver.find_element_by_xpath(addr_xpath).get_attribute("innerText")
print("##식당주소##", address) #### address 파싱할 예정
# plcNum = 식당 전화번호
plcNum_xpath = '//*[@id="mArticle"]/div[1]/div[2]/div[4]/div/div/span/span[1]'
plcNum = driver.find_element_by_xpath(plcNum_xpath).get_attribute("innerText")
print("##식당전화번호##", plcNum) #### plcNum 파싱할 예정


################### 영업시간, 메뉴 크롤링 실패 ####################
# operTime = 운영 시간
# 더보기 버튼 요소
more_view = '//*[@id="mArticle"]/div[1]/div[2]/div[2]/div/div[1]/ul/li/a/span'
driver.find_element_by_xpath(more_view).click()
sleep(1)
# 영업날짜(요일)
operDay_xpath = '//*[@id="mArticle"]/div[1]/div[2]/div[2]/div/div[2]/div/ul[1]/li/text()'
operDay = driver.find_element_by_xpath(operDay_xpath).get_attribute("wholeText")
print('##영업날짜(요일)##', operDay)
# 영업시간
operTime_xpath = '//*[@id="mArticle"]/div[1]/div[2]/div[2]/div/div[2]/div/ul[1]/li/span'
operTime = driver.find_element_by_xpath(operTime_xpath).get_attribute("innerText")
print('##영업시간##', operTime)
# 휴무일
dayOff_xpath = '//*[@id="mArticle"]/div[1]/div[2]/div[2]/div/div[2]/div/ul[2]/li'
dayOff = driver.find_element_by_xpath(dayOff_xpath).get_attribute("innerText")
print('##휴무일##', dayOff)


### 메뉴 가져오기 ###

# 메뉴이름과 가격 가져오는 함수
# def getMenuInfo(menu):
#     menuName = menu.select('.info_menu > .loss_word')[0].text
#     menuPrices = menu.select('.info_menu > .price_menu')
#     menuPrice = ''
    
#     if len(menuPrices) !=0:
#         menuPrice = menuPrices[0].text.split(' ')[1]
        
#     return [menuName, menuPrice]

# menuInfos = []
# menu_xpath = '//*[@id="mArticle"]/div[3]/ul/li'
# menu = driver.find_element_by_xpath(menu_xpath) 

# for m in menu:
#     menuInfos.append(getMenuInfo(m))
        
# print("##메뉴명과 가격##", menuInfos) #### menu, price 파싱할 예정
        
        




# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()