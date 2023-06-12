from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

chrome_driver_path = "C:\\proj\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://10.118.249.228:5002/login.html")

username_field = driver.find_element(By.ID, "User_Name")
password_field = driver.find_element(By.ID, "Password")

username_field.send_keys("natasha.lasrado@dell.com")
password_field.send_keys("3487405@Dell")

time.sleep(3)
submit_button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Cust_name']")))

try:
    submit_button.click()

    time.sleep(3)  

    if "Home Page Prototype has been added" in driver.page_source:
        time.sleep(1) 
        print("Login successful!!")
    else:
        error_message = driver.switch_to.alert.text
        print("Login failed. Error message:", error_message)

except UnexpectedAlertPresentException as e:
    error_message = e.alert_text
    print("Login failed!. Error message:", error_message)

#=====Configurator======

def add_values():
    
    cust_name_field = driver.find_element(By.ID, "Cust_name")
    op_name_field = driver.find_element(By.ID, "Op_name")
    cust_name1_field = driver.find_element(By.ID, "Cust_name1")
    op_name1_field = driver.find_element(By.ID, "Op_name1")
    bus_case_dur_field = driver.find_element(By.ID, "Bus_case_dur")
    currency_field = driver.find_element(By.ID, "Currency")
    start_date_field = driver.find_element(By.ID, "start_date")

    dropdown = driver.find_element(By.ID, "Cust_name")

  
    select = Select(dropdown)
    select.select_by_value("Vourne")

    #cust_name_field.send_keys("ABC")
    time.sleep(2)
    #op_name_field.send_keys("Developer")
    #time.sleep(2)
    #cust_name1_field.send_keys("ABC")
    #time.sleep(2)
    op_name1_field.send_keys("ABC")
    #time.sleep(2)
    bus_case_dur_field.send_keys("24")
    time.sleep(2)
    #currency_field.send_keys("USD")
    #time.sleep(2)
    start_date_field.send_keys("2023-05-24")  # Date format: YYYY-MM-DD

    submit_button = driver.find_element(By.ID, "Cust_name_button")
    submit_button.click()

    time.sleep(3)  

    # Check if the form submission was successful
    if "success" in driver.page_source:
        print("Form submitted successfully!")
    else:
        print("Form submission failed.")

  
try:
    iframe = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//iframe[@src='./index.html']")))

   
    driver.switch_to.frame(iframe)
    configurator_element = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Configurator')]")))
    configurator_element.click()
    
    print("Clicked on Configurator")
    time.sleep(5)
    add_values()

except UnexpectedAlertPresentException as e:
    error_message = e.alert_text
    print("Login failed!. Error message:", error_message)
    #driver.quit()
    
    
#========Technology===========


def adding_values():
   # driver = webdriver.Chrome()    
    solution_select = driver.find_element(By.ID, "Solution1")

   
    select = Select(solution_select)
    select.select_by_visible_text("BACKUP")
    time.sleep(2)
    

    ramp_up_volume_input = driver.find_element(By.ID,"Ramp_Up_Volume1")
    ramp_up_volume_input.send_keys("10")
    time.sleep(2)
    
  
    annual_growth_input = driver.find_element(By.ID,"Annual_Growth1")
    action = ActionChains(driver)

    action.click_and_hold(annual_growth_input).move_by_offset(annual_growth_input.size['width'] // 4, 0).release().perform()
    time.sleep(2)
    
    type_select = Select(driver.find_element(By.ID,"type11"))

 
    type_select.select_by_value("Appliance Only")
    time.sleep(2)
    

   #unit_select = Select(driver.find_element(By.ID,"unit1"))


    #unit_select.select_by_value("Back End TiBu")
   # input_element = driver.find_element(By.ID,"Ramp_Up_Month1")
    #driver.execute_script("arguments[0].setAttribute('max', '10');", input_element)

    #input_element.click()
    time.sleep(2)
    
    try:
        alert = Alert(driver)
        alert.accept()
        print("Alert Accepted")
        time.sleep(5)
        # or alert.dismiss() to dismiss the alert
    except:
        pass
    
    submit_button2 = driver.find_element(By.ID,"submit_data")

    submit_button2.click()
    time.sleep(10)

adding_values()
#driver.quit()


#=======Consolidate======

table = driver.find_element(By.ID, "consolidate_table")

rows = table.find_elements(By.TAG_NAME, "tr")


for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    

    if len(cells) >= 12:
        # Extract the data
        options = cells[0].text
        tier = cells[1].text
        solution = cells[2].text
        classification = cells[3].text
        description = cells[4].text
        technology = cells[5].text
        target_amount = cells[6].text
        target_month = cells[7].text
        annual_growth = cells[8].text
        unit = cells[9].text
        units_per_config = cells[10].text
        tier_name = cells[11].text
        
        # Print the extracted data
        print(f"Options: {options}")
        print(f"Tier: {tier}")
        print(f"Solution: {solution}")
        print(f"Classification: {classification}")
        print(f"Description: {description}")
        print(f"Technology: {technology}")
        print(f"Target Amount: {target_amount}")
        print(f"Target Month: {target_month}")
        print(f"Annual Growth: {annual_growth}")
        print(f"Unit: {unit}")
        print(f"Units per Config: {units_per_config}")
        print(f"Tier Name: {tier_name}")
        print("----------")
        
   
        submit_button3 = driver.find_element(By.ID,"Cust_name")
        submit_button3.click()
        time.sleep(10)


#driver.quit()


#==========Summary========

#print_button = driver.find_element(By.ID, "Final_Report_Submit")
detailed_summary_button = driver.find_element(By.ID, "toggle-Page")
save_report_button = driver.find_element(By.ID, "Save_Report")
additional_button = driver.find_element(By.ID, "submit_Yes")


#print_button.click()
detailed_summary_button.click()
detailed_summary_button.click()
time.sleep(10)
save_report_button.click()
time.sleep(20)
if additional_button.is_enabled():
    additional_button.click()
    print("Summary saved")


#=======Saved Business========

iframe = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//iframe[@src='./index.html']")))


driver.switch_to.frame(iframe)


header_tag_element = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Saved Business Cases')]")))
header_tag_element.click()

cust_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Cust_name")))
cust_name_input.send_keys("Vanguard")

current_value = cust_name_input.get_attribute("value")
print("Current value:", current_value)
op_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Op_name")))


op_name_input.send_keys("Vanguard Pricing 202352")

current_value = op_name_input.get_attribute("value")
print("Current value:", current_value)
time.sleep(10)
driver.quit()


