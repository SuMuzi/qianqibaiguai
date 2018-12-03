import smtplib
import random
import string
from email.mime.text import  MIMEText
from email.header import Header

def sendEmail(receivers):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    #print(ran_str)
    smtp_server='smtp.qq.com'
    sender = "1013719026@qq.com"
    password="lanutjsjnrinbcjd"
    receiver = receivers
    subject = "千奇百怪验证信息"
    content = "亲爱的用户，您好！您的验证码为%s" % ran_str
   # print(content)
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = Header('千奇百怪技术部', 'utf-8')
    msg['To'] = Header(receiver, 'utf-8')
    #subject = 'python SMTP 测试邮件'
    msg['Subject'] = Header(subject, 'utf-8')
    #try:
    smtp = smtplib.SMTP_SSL(smtp_server, 465)  # 实例化SMTP对象
    # smtp.connect()  # （缺省）默认端口是25 也可以根据服务器进行设定
    smtp.login(sender, password)  # 登陆smtp服务器
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
        #print("发送成功")
    #except smtplib.SMTPException as e:
        #print("发送失败",e)
    return ran_str
#sendEmail("1013719026@qq.com")
