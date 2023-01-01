from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# #DBPL = Total number of main publication
# Author's Pub = Total number of publication for all field
# "Citations", "h-index", "i10-index", "email", = google scholer page
# ORCID = DBPL page

columns = ["Institution", "Count for ins", "Faculty", "Author's Pub", "Adj.#", "Field of Work", "Citations", "h-index", "i10-index", "ORCID", "HomePage"]

def main():
    url = "https://csrankings.org/#/index?graph&chi&robotics&bio&visualization&ecom&tr"

    driver = webdriver.Chrome('chromedriver')
    driver.get(url)

    rows = 1+len(driver.find_elements(By.XPATH, '//table[@id="ranking"]/tbody/tr'))
    print(rows)

    fac_pth = '//table[@id="ranking"]/tbody/tr[3]/td/div/div/table/tbody/tr[1]/td[2]/small/a[1]'

    fac_list = []
    cc = 0
    for r in range(1, rows, 3):
        pth = '//table[@id="ranking"]/tbody/tr['+str(r)+']/td[2]/span[2]'
        pth1 = '//table[@id="ranking"]/tbody/tr['+str(r)+']/td[3]'
        pth2 = '//table[@id="ranking"]/tbody/tr['+str(r)+']/td[4]'

        Fac_rows = 1+len(driver.find_elements(By.XPATH, '//table[@id="ranking"]/tbody/tr['+str(r+2)+']/td/div/div/table/tbody/tr'))
  
  
        for fr in range(1, Fac_rows, 2):
            all_fac = {}
    
            #Faculty First Page
            fac_pth = '//table[@id="ranking"]/tbody/tr['+str(r+2)+']/td/div/div/table/tbody/tr['+str(fr)+']/td[2]/small/a[1]'
            fac_pubs = '//table[@id="ranking"]/tbody/tr['+str(r+2)+']/td/div/div/table/tbody/tr['+str(fr)+']/td[3]/small/a'
            fac_adj = '//table[@id="ranking"]/tbody/tr['+str(r+2)+']/td/div/div/table/tbody/tr['+str(fr)+']/td[4]'

            x = driver.find_element(By.XPATH, fac_pth).get_attribute("text")
            y = driver.find_element(By.XPATH, fac_pubs).get_attribute("text")
            z = driver.find_element(By.XPATH, fac_adj).get_attribute('innerText')

            #Faculty second Page
            area_rows = 1+len(driver.find_elements(By.XPATH, '//table[@id="ranking"]/tbody/tr['+str(r+2)+']/td/div/div/table/tbody/tr['+str(fr)+']/td[2]/small/span[1]/span'))
            area = ''

            for ar in range(1, area_rows):
                fac_area = '//table[@id="ranking"]/tbody/tr['+str(r+2)+']/td/div/div/table/tbody/tr['+str(fr)+']/td[2]/small/span[1]/span['+str(ar)+']'
                a = driver.find_element(By.XPATH, fac_area).get_attribute('innerText').capitalize()
                if(area==''):
                    area=area+a
                else:
                    area=area+", "+a

            #Faculty Googler Scholer page
            google_url = '//table[@id="ranking"]/tbody/tr['+str(r+2)+']/td/div/div/table/tbody/tr['+str(fr)+']/td[2]/small/a[3]'
            nurl = driver.find_element(By.XPATH, google_url).get_attribute("href")
            ndriver = webdriver.Chrome('chromedriver')
            ndriver.get(nurl)

            try:
                Tcitation = ndriver.find_element(By.XPATH, '//table[@id="gsc_rsb_st"]/tbody/tr[1]/td[2]').get_attribute("innerText")
                hindex = ndriver.find_element(By.XPATH, '//table[@id="gsc_rsb_st"]/tbody/tr[2]/td[2]').get_attribute("innerText")
                i10_index = ndriver.find_element(By.XPATH, '//table[@id="gsc_rsb_st"]/tbody/tr[3]/td[2]').get_attribute("innerText")
                homepage = ndriver.find_element(By.XPATH, '//div[@id="gsc_prf_ivh"]/a').get_attribute("href")
            except:
                Tcitation = ''
                hindex = ''
                i10_index = ''
                homepage = ''
      

            #DBPL Page
            dbplurl = driver.find_element(By.XPATH, fac_pubs).get_attribute("href")
            dbpldriver = webdriver.Chrome('chromedriver')
            try:
                dbpldriver.get(dbplurl)
            except:
                continue


            #data binding
            all_fac["Name"] = x
            all_fac["Author's Pub"] = y
            all_fac["Adj.#"] = z
            all_fac["Field of Work"] = area
            all_fac["Citations"] = Tcitation
            all_fac["h-index"] = hindex
            all_fac["i10-index"] = i10_index
            all_fac["HomePage"] = homepage
            try:
                dbpl = dbpldriver.find_element(By.XPATH, '//header[@id="headline"]/nav/ul/li/div/a').get_attribute("href")
                remove = "https://orcid.org/"
                all_fac["ORCID"] = dbpl.replace(remove, '')
            except:
                print("No ORCID")
            all_fac["Institution"] = driver.find_element(By.XPATH, pth).text
            all_fac["Count for ins"] = driver.find_element(By.XPATH, pth1).text
            all_fac["Faculty"] = driver.find_element(By.XPATH, pth2).text

            fac_list.append(all_fac)
            cc+=1
            print(cc)
    
        fac_list
    
        dbpldriver.close()
        ndriver.close()
    driver.close()

    df = pd.DataFrame(data=fac_list, columns=columns)
    df.to_csv("Researchers.csv", index=False)

    return

if __name__ == '__main__':
    main()