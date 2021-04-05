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


# 자가진단에 쓸 계정 정보
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
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a'))
    )
except:
    print('응답 없음')
    quit()

# 선택
driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/a').click()

# 제출
driver.find_element_by_class_name('layerFullBtn').click()



# 4. 성명, 생년월일 선택
driver.find_element_by_id('user_name_input').send_keys(NAME)
driver.find_element_by_id('birthday_input').send_keys(DAY_OF_BIRTH)

# 제출
driver.find_element_by_id('btnConfirm').click()

# 비밀번호 입력 페이지로 넘어가는 동안 명시적 대기 사용
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'input_text_common')))

# 5. 비밀번호 선택
sleep(0.5)
driver.find_element_by_class_name('input_text_common').send_keys(PASSWORD)

# 제출
driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
print('로그인 완료')
#endregion



#region 자가진단

# 학생 리스트 가져오기
sleep(1)

items = driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul').find_elements_by_tag_name('li')

print(f'확인된 총 학생 수 : {len(items)}명')

while True:
    # 자가진단 완료하지 않은 학생만 가져오기
    items = driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul').find_elements_by_css_selector('item:not(.active)')

    print(f'자가진단이 되지 않은 학생 수 : {len(items)}명')
    if len(items) == 0:
        print('자가진단이 모두 완료되었습니다.')
        break

    item = items[0]
    name = item.get_attribute('innerHTML')

    #region 자가진단
    item.find_element_by_class_name('name').click()
    print(f'{name}학생의 자가진단을 시작합니다.')
    
    # 학생이 자가진단에 참여한지 3분이 지나지 않았을 경우 발생하는 메세지 처리
    # try:
    #     driver.switch_to.alert.dismiss()
    #     print(f'{name}(은)는 자가진단을 완료한지 3분이 지나지 않았습니다.')
    #     continue
    # except:
    #     pass
    
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="survey_q1a1"]')))
    except:
        print('응답 없음')
        quit()

    # 조사 응답
    driver.find_element_by_xpath('//*[@id="survey_q1a1"]').click()
    driver.find_element_by_xpath('//*[@id="survey_q2a1"]').click()
    driver.find_element_by_xpath('//*[@id="survey_q3a1"]').click()
    
    print('질문 답변 선택 완료')

    # 응답 제출
    driver.find_element_by_id('btnConfirm').click()

    print(f'{name} 제출 완료')

    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/div[1]/div[1]/ul/li/a')))
    except:
        print('응답 없음')
        quit()
    # 처음으로 버튼 클릭
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[1]/ul/li/a').click()
    #endregion

#endregion
    


# 브라우저 닫기
sleep(TIME)
print('프로그램을 종료합니다.')
driver.close()