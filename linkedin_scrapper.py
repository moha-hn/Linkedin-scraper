from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Set up your LinkedIn job search URL
linkedin_url = "https://www.linkedin.com/jobs/search/?keywords=intern%20computer%20science&location=Montreal"

# Set your ChromeDriver path
chromedriver_path = r"C:\Users\mhano\Desktop\application automatisation\chromedriver-win64"

# Set up Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

# Open LinkedIn Jobs Page
driver.get(linkedin_url)
time.sleep(5)  # Wait for page to load

# Scroll down to load more jobs
for _ in range(3):  
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(2)

# Extract job postings
jobs = driver.find_elements(By.CLASS_NAME, "base-search-card__info")

job_list = []
for job in jobs:
    try:
        title = job.find_element(By.CLASS_NAME, "base-search-card__title").text
        company = job.find_element(By.CLASS_NAME, "base-search-card__subtitle").text
        link = job.find_element(By.TAG_NAME, "a").get_attribute("href")

        job_list.append({"Title": title, "Company": company, "Link": link})
    except Exception as e:
        print("Error:", e)

# Save to Excel
df = pd.DataFrame(job_list)
df.to_excel("Montreal_CS_Internships.xlsx", index=False)

print("working")
driver.quit()
