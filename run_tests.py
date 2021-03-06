import time, sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader
from db_fixture import test_data


# 指定测试用例为当前文件夹下的interface目录
test_dir = './interface'
testsuit = defaultTestLoader.discover(test_dir,pattern='*_test.py')


if __name__ == '__main__':
    test_data.init_data()    # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = './report/'+now+'_result.html'
    fp = open(filename,'wb')

    # HTMLTestRunner为unittest单元测试框架的扩展，利用它提供的HTMLTestRunner()类来代替unittest单元测试框架的TestTestRunner()类，
    # 运行discover中匹配的测试用例，生成HTML格式的测试报告
    runner = HTMLTestRunner(stream=fp,title='发布会签到系统接口自动化测试',description='运行环境：MySQL(PyMySQL), Requests, unittest ')

    runner.run(testsuit,rerun=0,save_last_run=False)
    fp.close()