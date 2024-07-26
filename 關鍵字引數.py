#Python 的關鍵字參數 (keyword Arguments)

def Hello(greeting,title,first_name,last_name):
    print(f"{greeting},{title},{first_name}{last_name}")
    
Hello("你好!","Mr","Orange","蔡")
Hello(greeting="你好!",title="Mr",first_name="Banana",last_name="陳")

###############################################################################################
def get_phone(country_code,area_code,first,last):
    return  f"{country_code}-{area_code}-{first}-{last}"

str=get_phone(country_code="886",area_code="02",first="1234",last="5678")
print(str)