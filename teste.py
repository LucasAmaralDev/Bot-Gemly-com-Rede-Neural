divBuy = nav.driver.find_element(By.CLASS_NAME, 'item--info')
botao = divBuy.find_element(By.CLASS_NAME, 'buy')
divBuy.click()

collect = nav.driver.find_elements(By.XPATH, 'collect')
for element in collect:
    try:
        element.click()
        break
    except:
        pass