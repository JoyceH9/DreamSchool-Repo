from selenium import webdriver
from selenium.webdriver.common.by import By

# 定义函数AskPrice_SpotCurrency，用于获取指定日期和货币的现汇卖出价
def AskPrice_SpotCurrency(date, currency):
    try:
        # 启动 Chrome 浏览器
        driver = webdriver.Chrome()

        # 打开中国银行外汇牌价页面
        driver.get('https://www.boc.cn/sourcedb/whpj/')

        # 清空搜索框并输入开始日期
        search_input = driver.find_element(By.ID, "erectDate")
        search_input.clear()
        search_input.send_keys(date)

        # 清空搜索框并输入结束日期
        search_input = driver.find_element(By.ID, "nothing")
        search_input.clear()
        search_input.send_keys(date)

        # 选择货币种类
        currency_dropdown = driver.find_element(By.ID, "pjname")
        currency_dropdown.send_keys(currency)

        # 运行搜索函数
        driver.execute_script("executeSearch();")

        # 提取这一天更新的最后一条现汇卖出价
        Last_time = driver.find_element(By.XPATH, "/html/body/div/div[4]/table/tbody/tr[2]")
        price = Last_time.find_element(By.XPATH, "/html/body/div/div[4]/table/tbody/tr[2]/td[4]")
        price_text = price.text.strip()

        if price_text:
            # 写入文件
            with open('result.txt', 'w') as file:
                file.write(f"日期: {date}\n")
                file.write(f"币种: {currency}\n")
                file.write(f"现汇卖出价: {price_text}\n")
            print("已将日期、币种和现汇卖出价写入 result.txt 文件")
        else:
            # 现汇卖出价为空值
            print("错误：现汇卖出价为空值")

    except Exception as e:
        # 程序异常
        print("发生异常:", e)
    finally:
        # 关闭浏览器
        driver.quit()

# 用户输入想要查询的日期
desired_date = input("请输入想要查询的日期（例如 '20211231'）: ")

# 定义一个字典，将货币符号映射到其对应的名称
symbol_to_currency = {
    'GBP': '英镑',
    'HKD': '港币',
    'USD': '美元',
    'CHF': '瑞士法郎',
    'DEM': '德国马克',
    'FRF': '法国法郎',
    'SGD': '新加坡元',
    'SEK': '瑞典克朗',
    'DKK': '丹麦克朗',
    'NOK': '挪威克朗',
    'JPY': '日元',
    'CAD': '加拿大元',
    'AUD': '澳大利亚元',
    'EUR': '欧元',
    'MOP': '澳门元',
    'PHP': '菲律宾比索',
    'THB': '泰国铢',
    'NZD': '新西兰元',
    'KRW': '韩国元',
    'RUB': '卢布',
    'MYR': '林吉特',
    'TWD': '新台币',
    'ESP': '西班牙比塞塔',
    'ITL': '意大利里拉',
    'NLG': '荷兰盾',
    'BEF': '比利时法郎',
    'FIM': '芬兰马克',
    'INR': '印度卢比',
    'IDR': '印尼卢比',
    'BRL': '巴西里亚尔',
    'AED': '阿联酋迪拉姆',
    'ZAR': '南非兰特',
    'SAR': '沙特里亚尔',
    'TRY': '土耳其里拉',
}

# 用户输入货币的符号
currency_symbol = input("请输入货币的符号（例如 'USD'）: ")

# 使用字典获取货币对应的名称
if currency_symbol in symbol_to_currency:
    currency_name = symbol_to_currency[currency_symbol]
    # 调用函数获取该日期和货币的现汇卖出价
    AskPrice_SpotCurrency(desired_date, currency_name)
else:
    # 如果输入的货币符号在字典中找不到对应的货币名称
    print("输入的货币符号无效")
