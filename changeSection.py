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
    check=1

    with requests.Session() as s:

        r=s.get(url,headers=headers)
        soup=BeautifulSoup(r.content,'html.parser')
        logData['hidden_redir']=soup.find("input",attrs={"name":"hidden_redir"})['value']
        logData['hidden_form_id']=soup.find("input",attrs={"name":"hidden_form_id"})['value']
        r=s.post(url+"main.php",data=logData,headers=headers)
        soup=BeautifulSoup(r.content,'html.parser')
        log2Data['hidden_redir']=soup.find("input",attrs={"name":"hidden_redir"})['value']
        log2Data['hidden_form_id']=soup.find("input",attrs={"name":"hidden_form_id"})['value']
        a=r.text
        ind=a.find(coursecode)
        typefi=a.find('"',ind)
        rad=a[ind:typefi]
        log2Data["radio_courseList"]= rad
        while check>0:
            r=s.post(url+"main.php",data=log2Data,headers=headers)
            a=r.text
            check=a.find("font color=")
        print('Course Added')

if __name__=='__main__':
    userid=''
    passwd=''
    coursecode=''
    changeSection=''
    changeSection(userid,passwd,coursecode,changeSection)
