# --encoding:utf-8--
# @Time:2021/2/521:38
# @author:l_s
# @File:1st_by.py
from abc import abstractmethod



class By_1st:
    @abstractmethod
    def driver_ini(self):
        r'before test do sth'
        pass

    @abstractmethod
    def driver_quit(self):
        pass


    def driver_find_by_xpath(self):
        self.driver_ini()
        self.driver_find_by_xpath()
        self.driver_quit()

    @abstractmethod
    def driver_quit(self):
        r'this is a abstract method'
        pass


