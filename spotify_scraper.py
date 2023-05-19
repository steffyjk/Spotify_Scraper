import time


def spotify_scraper():
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    driver = webdriver.Chrome()
    driver.get("https://open.spotify.com/")

    # THIS IS MAIN OUTPUT OF SPOTIFY
    spotify_output = [
        {
            "without_login": {},
            "with_login": {}
        }

    ]

    # SIDEBAR MANU DATA
    sidebar = []
    upper_sidebar = driver.find_elements(By.CLASS_NAME, "RSg3qFREWrqWCuUvDpJR")
    for data in upper_sidebar:
        sidebar.extend(data.text.splitlines())

    lower_sidebar = driver.find_elements(By.CLASS_NAME, "LKgm9fCDTO7wqig_5U1q")
    for data in lower_sidebar:
        sidebar.extend(data.text.splitlines())

    time.sleep(2)
    other_policies = driver.find_elements(By.CLASS_NAME, "eRmZIa")
    for data in other_policies:
        sidebar.extend(data.text.splitlines())

    english_world_logo = driver.find_element(By.CLASS_NAME, "cXJiiS")
    sidebar.append(english_world_logo.text)

    main_categories = driver.find_elements(By.CLASS_NAME, "MfVrtIzQJ7iZXfRWg6eM")
    main_page = [{"main_categories": [i.text for i in main_categories]}]
    # PRIMARILY WE HAVE 3 CATEGORIES IN INDIA [FOCUS, SPOTIFY PLAYLIST, SOUND OF INDIA]
    # 1 Focus data
    focus_btn = driver.find_element(By.CLASS_NAME, "pudHk .MfVrtIzQJ7iZXfRWg6eM")

    # Click on the element using JavaScript
    driver.execute_script("arguments[0].click();", focus_btn)
    # focus_btn.click()
    time.sleep(2)


    driver.save_screenshot("page.png")

    print(main_page)


if __name__ == "__main__":
    try:
        spotify_scraper()
    except Exception as err:
        print(f"There is some error regarding {err}")

    # TO GO ONTO NEW PAGE
    # Open a new tab using JavaScript

    # driver.execute_script("window.open('about:blank', '_blank');")
    #
    # # Switch to the newly opened tab
    # driver.switch_to.window(driver.window_handles[-1])
    # driver.get("https://www.youtube.com/")
    # time.sleep(2)
    # driver.save_screenshot("123.png")
