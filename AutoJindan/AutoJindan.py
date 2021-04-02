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



#region Initialize
URL = 'https://hcs.eduro.go.kr/#/loginHome'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(executable_path='D:/Coding/python/AutoJindan/chromedriver', options=options)
driver.get(url=URL)
# 최대 대기 시간
driver.implicitly_wait(time_to_wait=5)
TIME = 2

NAME = '양태웅'
DAY_OF_BIRTH = '040422'
PASSWORD = '0422'

#endregion



#region Login
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
driver.find_element_by_id('user_name_input').send_keys(NAME)
driver.find_element_by_id('birthday_input').send_keys(DAY_OF_BIRTH)
# 제출
driver.find_element_by_id('btnConfirm').click()
#비밀번호 입력 페이지로 넘어가는 동안 잠깐 멈춰줘야 하는데, 암묵적 대기가 먹지 않으니 그냥 sleep으로 멈춤
sleep(TIME)



# 5. 비밀번호 선택
driver.find_element_by_class_name('input_text_common').send_keys(PASSWORD)
# 제출
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

sleep(TIME)

#endregion



#region 자가진단
#학생 리스트 가져오기
items = driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul').find_elements_by_tag_name('li')
print(f'확인된 학생 수 : {len(items)}명')






#region SAVED
# 학생 수 만큼 루프
# for item in items:
#     sleep(3)
#     # 자가진단 진입
#     try:
#         name = item.find_element_by_class_name('name').get_attribute('innerHTML')
#         item.find_element_by_class_name('name').click()
        
#         # 학생이 이미 참여 했을 경우 발생하는 경고창 처리
#         try:
#             print(f'{name}(은)는 이미 참여하였습니다')
#             driver.switch_to.alert().dismiss()
#         except:
#             pass

#         sleep(3)

#         # 조사 응답
#         driver.find_element_by_xpath('//*[@id="survey_q1a1"]').click()
#         driver.find_element_by_xpath('//*[@id="survey_q2a1"]').click()
#         driver.find_element_by_xpath('//*[@id="survey_q3a1"]').click()

#         sleep(1)

#         # 응답 제출
#         driver.find_element_by_id('btnConfirm').click()

#         sleep(3)
#         # 처음으로 버튼 클릭
#         driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[1]/ul/li/a').click()
#     except selenium.common.exceptions.StaleElementReferenceException as err:
#         print(f'[StaleElementReferenceException] Passing {name}')
#         pass
#endregion





i = 0

for i in range(0, len(items)):
    print(f'확인된 학생 수 : {len(items)}명')
    sleep(3)
    try:
        i += 1
        # 자가진단 진입
        name = items[i].find_element_by_class_name('name').get_attribute('innerHTML') 
        items[i].find_element_by_class_name('name').click()
        
        # 학생이 이미 참여 했을 경우 발생하는 경고창 처리
        try:
            driver.switch_to.alert.dismiss()
            print(f'{i}.{name}(은)는 이미 자가진단이 완료되었습니다.')
        except:
            sleep(3)

            # 조사 응답
            driver.find_element_by_xpath('//*[@id="survey_q1a1"]').click()
            driver.find_element_by_xpath('//*[@id="survey_q2a1"]').click()
            driver.find_element_by_xpath('//*[@id="survey_q3a1"]').click()

            sleep(1)

            # 응답 제출
            driver.find_element_by_id('btnConfirm').click()

            print(f'{name} 제출 완료')

            sleep(3)
            # 처음으로 버튼 클릭
            driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[1]/ul/li/a').click()

    except selenium.common.exceptions.StaleElementReferenceException as err:
        print(f'[StaleElementReferenceException] Passing {name}')
        pass




#endregion



sleep(TIME)



# 브라우저 닫기
print('\nTERMINATING!!')
driver.close()