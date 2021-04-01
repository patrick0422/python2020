# 참고 링크
# https://greeksharifa.github.io/references/2020/10/30/python-selenium-usage/

#region Import
import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep
#endregion

#region 초기화
URL = 'https://hcs.eduro.go.kr/#/loginHome'

driver = webdriver.Chrome(executable_path='D:/Coding/python/AutoJindan/chromedriver')
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=0.5)
#endregion


#region 로그인
# 1. 초기 페이지에서 자가진단 참여하기 버튼 클릭
driver.find_element_by_id('btnConfirm2').click()



# 2. 학교 검색 버튼 클릭
driver.find_element_by_class_name('searchBtn').click()



# 3. 학교 검색
# 3-1. 시/도 선택
Select(driver.find_element_by_id('sidolabel')).select_by_visible_text('광주광역시')

# 3-2. 학교급 선택
Select(driver.find_element_by_id('crseScCode')).select_by_visible_text('고등학교')

# 3-3. 학교명 입력
driver.find_element_by_id('orgname').send_keys('광주소프트웨어마이스터고등학교')

# 3-4. 학교 검색
driver.find_element_by_class_name('searchBtn').click()

# 3-5. 학교 선택
try:
    # 검색 결과가 뜰때까지 최대 5초간 탐색
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a'))
    )
finally:
    # 선택
    driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a').click()
# 제출
driver.find_element_by_class_name('layerFullBtn').click()



# 4. 성명, 생년월일 선택
driver.find_element_by_id('user_name_input').send_keys('양태웅')
driver.find_element_by_id('birthday_input').send_keys('040422')
# 제출
driver.find_element_by_id('btnConfirm').click()
#비밀번호 입력 페이지로 넘어가는 동안 잠깐 멈춰줘야 하는데, 암묵적 대기가 먹지 않으니 그냥 sleep으로 멈춤
sleep(2)



# 5. 비밀번호 선택
password = driver.find_element_by_class_name('input_text_common')
password.send_keys('0422')

# 제출
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
#endregion


sleep(5)

# 브라우저 닫기
# driver.close()