import pymysql
import requests
import random

def get_token():
    get_param_data = {
        'grant_type': 'client_credential',
        'appid': 'wx116dfe67cf36b5db',
        'secret': '4fa8e58c98667a8f5cdb1f397d0290d1'

    }
    response = requests.get(url='https://api.weixin.qq.com/cgi-bin/token', params=get_param_data)

    return response.json()['access_token']



# def setup_case(case_name):
#     print('测试用例%s开始执行'%case_name)
#
# def teardown_case(case_name):
#     print('测试用例%s结束执行'%case_name)
#
# def setup_step(case_step):
#     print('测试步骤%s开始执行'%case_step)
#
# def teardown_step(case_step):
#     print('测试步骤%s结束执行'%case_step)


def get_random_int():
    random_list =[]
    random_list.append(random.randint(1,10))
    random_list.append(random.randint(1,10))
    return random_list

def get_random_ints(min,max,count=10):
    random_list =[]
    for i in range(count):
        random_list.append(random.randint(min, max))
    return random_list

def get_str(randomlength=18,count=3):
    base_str='0123456789'
    length = len(base_str)-1
    for i in range(count):
        ran_str =''
        for j in range(randomlength):
            ran_str += base_str[random.randint(0,length)]
    return ran_str

def get_random_mobilenumber(count=3):
    phone_list=[]
    for i in range(count):
        start_phone = random.choice(['130', '131', '132', '133', '134', '135', '136', '156', '177', '188'])
        end_phone = ''.join(random.sample('0123456789', 8))  # 从0～9找到8个数字,join 将一个字符列表转换成字符串
        phone_list.append(start_phone+end_phone)
    return phone_list

def decode_iso88591(string):
    return string.encode('utf8').decode('iso8859-1')


def decode_utf8(string):
    return string.encode('iso8859-1').decode('utf8',"ignore")

if __name__=='__main__':
    # print(get_random_ints(min=1,max=100))
    # print(get_random_mobilenumber())
    # print(get_random_int())
    # print(get_random_mobilenumber())
    # print(get_str())
    # print('端午'.encode('utf8').decode('iso8859-1'))
    # print('ç«¯å'.encode('iso8859-1').decode('utf8',"ignore"))
    connect =pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',
        database='easybuy',
        charset='utf8',
        cursorclass =pymysql.cursors.DictCursor
    )

    cur =connect.cursor(pymysql.cursors.DictCursor)
    cur.execute("select  * from esaybuy_user;")
    value1 =cur.fetchone()   # 取某一行值
    value2 = cur.fetchmany(4)    #取4行值
    value3 = cur.fetchall()    #取所有行
    print(value1)
    print(value2)
    print(value3)
    cur.execute("update %s set userName=%s where loginName=%s;%('esaybuy_user','浙江'，'szz')")
    connect.commit()
    connect.close()







