import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib


def changeSection(userid,passwd,coursecode,changeSection):
    url="https://register.metu.edu.tr/"
    logData={"textUserCode":userid,"textPassword":passwd,"selectProgType": "1","submitLogin": "Login"}
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36"}
    log2Data={
        "textChangeCourseSection": changeSection,
        "selectChangeCourseCategory": "1",
        "submitChangeSection": "Change Section",
        "selectAddCourseCategory": "1",
        }
    

if __name__=='__main__':
    userid=''
    passwd=''
    coursecode=''
    changeSection=''
    changeSection(userid,passwd,coursecode,changeSection)
