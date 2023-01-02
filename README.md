![alt text](https://mastercourse.site/wp-content/uploads/2020/12/cropped-Mastercourseweblogo-07-1-e1615404376389-300x38.png)  

Dokkho Data Science C1: Capstone Project 1
## Problem Statement
➔ Dynamic Web Scraping using Selenium  
➔ Data Processing, Transformation, Manipulation  
➔ Visualization and Analytics in Tableau Public  
➔ Interesting Findings from Tableau Dashboard  
➔ Setting Up the project in GitHub
## How to scrape
I have used google colab and local desktop both for scrapping data. Scrapping using google colab was challenging for lack of documentation so I am giving  a few starter think which can just boost your scrapping using google colab.
* Make sure selenium is there
```
!pip install selenium
```
* Install Chromium Chromedriver
```
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin
```
* Import the Path
```
import sys
sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
```
* Import webdriver and manage options
```
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
```
* Import others
```
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
```
* Find Full Code  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yFqo2udmTfEW0KWYdiJGo33RrhwKoyGP?usp=sharing)
## Scraped Data
* [Faculty Data](https://github.com/KsLimon/MasterCourse.P01/blob/master/McProject01/Faculty.csv)  
The data is collected from [CSRankings: Computer Science Rankings](https://csrankings.org/#/fromyear/2012/toyear/2022/index?graph&chi&robotics&bio&visualization&ecom&world) based on Interdisciplinary Areas. In this datset there are 2266 faculty information like name, research areas, total publication, citations, institution etc.
## Analytics
* [Tableau Analysis](https://public.tableau.com/app/profile/md.kamrus.samad/viz/Book1_16723265509720/Dashboard1)  
  
  
  
![alt text](https://github.com/KsLimon/MasterCourse.P01/blob/master/McProject01/Dashboard%201.png)
