from selenium import webdriver
import time
import pandas as pd

driver = webdriver.Chrome("C:/Users/colin/Desktop/chromedriver")

data_csv=[]

# total page 62 

for i in range(1,63):
    
    driver.get('https://www.pilio.idv.tw/lto/list.asp?indexpage='+str(i)+'&orderby=new')
    
    # table 1  9 data    
    for i in range(2,2+9):
        row_data=[]
        
        date=driver.find_element_by_xpath('//*[@id="main"]/div/table[1]/tbody/tr['+str(i)+']/td[1]').text
        date=date.replace("\n", "") #replace \n

        data=driver.find_element_by_xpath('//*[@id="main"]/div/table[1]/tbody/tr['+str(i)+']/td[2]').text
        data=data.replace(",","") #replace ,

        second_data=driver.find_element_by_xpath('//*[@id="main"]/div/table[1]/tbody/tr['+str(i)+']/td[3]').text

        row_data.append(date)
        row_data.append(data[0:2])
        row_data.append(data[3:5])
        row_data.append(data[6:8])
        row_data.append(data[9:11])
        row_data.append(data[12:14])
        row_data.append(data[15:17])
        row_data.append(second_data)
        #print(date,data,second_data)    
        data_csv.append(row_data)
        
    # table 2 14 data
    for i in range(1,1+14):
        row_data=[]
        
        date=driver.find_element_by_xpath('//*[@id="ltotable"]/tbody/tr['+str(i)+']/td[1]').text
        date=date.replace("\n", "") #replace \n

        data=driver.find_element_by_xpath('//*[@id="ltotable"]/tbody/tr['+str(i)+']/td[2]').text
        data=data.replace(",","") #replace ,

        second_data=driver.find_element_by_xpath('//*[@id="ltotable"]/tbody/tr['+str(i)+']/td[3]').text


        row_data.append(date)
        row_data.append(data[0:2])
        row_data.append(data[3:5])
        row_data.append(data[6:8])
        row_data.append(data[9:11])
        row_data.append(data[12:14])
        row_data.append(data[15:17])
        row_data.append(second_data)
        #print(date,data,second_data)    
        data_csv.append(row_data)


driver.close()
lotto_csv=pd.DataFrame(data_csv)
lotto_csv.columns=['date','01_number_1','01_number_2','01_number_3','01_number_4','01_number_5','01_number_6','02_number']
lotto_csv.to_csv("C:/Users/colin/Desktop/lotto.csv",encoding='utf_8_sig',index=False)
