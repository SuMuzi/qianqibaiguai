import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DBHelper.MysqldbHelper import mysqlhelper
from Judge.Judge_id import Isid
from Judge.Judge_psword import IsPaaword
from Judge.Judge_emil import Isemail
from EmailSender.Judge_Email import sendEmail
from DBHelper.Insert_new import insert_new
from DBHelper.Update_password import update_password
#from Shop_main import *
class denglu(QWidget):
    """
    登录窗口 ：程序的入口
    登录窗口的内容包括两个tabel标签："账号"、"密码"，两个输入框分别用来输入账号及密码
    两个按钮：确定和退出，一个radiobutton用来设置密码的显示格式，一个显示标签用来创建新的账号
    密码在输入时应该默认为掩码输入，点击radiobutton时可以切换密码显示格式
    点击显示标签"创建新用户"时弹出创建窗口
    创建新账号时应该进行核查：账号不许为空不许重复，密码不许为空
    创建完成时把账号及密码存储在本地文件中：账号.txt、密码.txt  并退出关闭创建窗口
    登录时应核查账号与密码的匹配，并根据各种出错情况给出相应的提示信息
    登陆成功时进入主页面并自动退出关闭登录窗口
    """
    def __init__(self):
        super(denglu, self).__init__()
        self.setGeometry(300, 300, 400, 247)
        self.setWindowTitle('千奇百怪')
        self.setWindowIcon(QIcon("C:\\Users\\Suxiansheng\\Desktop\\logo.png"))
        #登录窗口无边界
       # self.setWindowFlags(Qt.FramelessWindowHint)
        #登录窗口透明
       # self.setAttribute(Qt.WA_TranslucentBackground, True)
        #定义多个空label
        self.label_null1 = QLabel()
        self.label_null2 = QLabel("账号：")
        self.label_null3 = QLabel("密码：")
        self.label_null4 = QLabel()
        self.label_new = QLabel()
        self.label_new1=QLabel()
        #定义创建新账户标签并设置信号槽绑定事件
        self.label_new.setText("<a href='#'>注册新用户</a>")
        self.label_new.setStyleSheet('''color: rgb(253,129,53);''')
        self.label_new.linkActivated.connect(self.idnew)
        self.label_new1.setText("<a href='#'>忘记密码？</a>")
        self.label_new1.setStyleSheet('''color: rgb(253,129,53);''')
        self.label_new1.linkActivated.connect(self.changePassword)
        #设置隐藏密码RadioButton
        self.btn_check = QRadioButton("显示密码")
        self.btn_check.setStyleSheet('''color: rgb(253,129,53);;''')
        self.btn_check.clicked.connect(self.yanma)
        #登录与退出按钮，设置按钮颜色及事件绑定
        self.btn_denglu = QPushButton("登录")
        self.btn_quxiao = QPushButton("退出")
        self.btn_denglu.setStyleSheet('''color: white;
                        background-color: rgb(218,181,150);''')
        self.btn_quxiao.setStyleSheet('''color: white;
                        background-color: rgb(218,181,150);''')
        self.btn_denglu.clicked.connect(self.check)
        self.btn_quxiao.clicked.connect(self.quxiao)
        #账号和密码
        self.lineedit_id = QLineEdit()
        self.lineedit_id.setPlaceholderText("账号")
        self.lineedit_password = QLineEdit()
        self.lineedit_password.setEchoMode(QLineEdit.Password)
        self.lineedit_password.setPlaceholderText("密码")
        #布局设置
        layout = QHBoxLayout(self)
        wid_denglu_right = QWidget()
        wid_denglu_left = QLabel()
        g = QGridLayout()
        g.addWidget(self.lineedit_id, 1, 1, 1, 2)
        g.addWidget(self.lineedit_password, 2, 1, 1, 2)
        g.addWidget(self.btn_check, 3, 1)
        g.addWidget(self.btn_denglu, 6, 1)
        g.addWidget(self.btn_quxiao, 6, 2)
       # g.addWidget(self.label_null1, 5, 1)
        g.addWidget(self.label_null2, 1, 0)
        g.addWidget(self.label_null3, 2, 0)
        #g.addWidget(self.label_null2, 6, 1)
        #g.addWidget(self.label_null3, 7, 1)
       # g.addWidget(self.label_null4, 8, 1)
        g.addWidget(self.label_new, 7, 1 )
        g.addWidget(self.label_new1, 7, 2)
        wid_denglu_right.setLayout(g)
        layout.addWidget(wid_denglu_left)
        layout.addWidget(wid_denglu_right)
        self.setLayout(layout)
    #密码隐藏
    def yanma(self):
        if self.btn_check.isChecked():
            self.lineedit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineedit_password.setEchoMode(QLineEdit.Password)
    #登录时核查账号及密码是否正确
    def check(self):
        if self.lineedit_id.text()=="":
            QMessageBox.warning(self, "!", "账号不能为空！", QMessageBox.Yes)
        else:
            if Isid(self.lineedit_id.text()):
               QMessageBox.warning(self, "!", "账号不存在！", QMessageBox.Yes)
            else:
                psword=IsPaaword(self.lineedit_id.text())
                if psword==self.lineedit_password.text():
                    QMessageBox.warning(self, "!", "登录成功！", QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, "!", "账号或密码错误！", QMessageBox.Ok)
                    #QMessageBox.setIconPixmap("C:\\Users\\Suxiansheng\\Desktop\\logo.png")
        '''
        temp = False
        self.id_password = {}
        id = open("账号.txt")
        password = open("密码.txt")
        i = 0
        for line1 in id:
            m = i+1
            for line2 in password:
                i = i+1
                if i == m:
                    self.id_password[line1]=line2
                    break
                if i < m:
                    continue
                    #如果输入账号不在账号表文件中，则推送消息框提醒
        if self.lineedit_id.text()+"\n" not in self.id_password:
            replay = QMessageBox.warning(self, "!", "账号或密码输入错误", QMessageBox.Yes)
        else:
            if self.id_password[self.lineedit_id.text()+"\n"] == self.lineedit_password.text()+"\n":
                #账号密码验证成功，创建主界面，进入信息管理程序,并关闭登录窗口
                self.shop = Shopmain()
                self.shop.show()
                self.close()
            else:
                replay = QMessageBox.warning(self, "!", "账号或密码输入错误", QMessageBox.Yes)
        id.close()
        password.close()
        '''
        #创建新的账号
    def idnew(self):
        self.label_idnew_id = QLabel("昵    称:")
        self.label_idnew_password = QLabel("密    码:")
        self.label_idnew_qrpassword = QLabel("确认密码:")
        self.btn_idnew_yzm = QPushButton("获取验证码")
        self.btn_idnew_yzm.clicked.connect(self.Abtainyzm)
        self.label_idnew_email = QLabel("Email:")
        self.label_idnew_phonenumber = QLabel("手机号码:")
        self.lineedit_idnew_id = QLineEdit()
        self.lineedit_idnew_password = QLineEdit()
        self.lineedit_idnew_password.setPlaceholderText("请输入新密码！")
        self.lineedit_idnew_qrpassword = QLineEdit()
        self.lineedit_idnew_qrpassword.setPlaceholderText("请再次输入密码！")
        self.lineedit_idnew_phonenumber = QLineEdit()
        self.lineedit_idnew_email = QLineEdit()
        self.lineedit_idnew_email.setPlaceholderText("请输入邮箱地址！")
        self.lineedit_idnew_yzm = QLineEdit()
        self.lineedit_idnew_yzm.setPlaceholderText("请输入验证码")
        self.btn_idnew_quren = QPushButton("注册")
        self.btn_idnew_quren.clicked.connect(self.idnewqueren)
        self.btn_idnew_quxiao = QPushButton("取消")
        self.btn_idnew_quxiao.clicked.connect(self.idnewclose)
        self.idnew = QWidget()
        layout_idnew = QGridLayout()
        layout_idnew.addWidget(self.label_idnew_id, 1, 0)
        layout_idnew.addWidget(self.label_idnew_password, 2, 0)
        layout_idnew.addWidget(self.label_idnew_qrpassword, 3, 0)
        layout_idnew.addWidget(self.label_idnew_email, 4, 0)
        layout_idnew.addWidget(self.label_idnew_phonenumber, 5, 0)
        layout_idnew.addWidget(self.btn_idnew_yzm, 6, 0)
        layout_idnew.addWidget(self.lineedit_idnew_id, 1, 1, 1, 2)
        layout_idnew.addWidget(self.lineedit_idnew_password, 2, 1, 1, 2)
        layout_idnew.addWidget(self.lineedit_idnew_qrpassword, 3, 1, 1, 2)
        layout_idnew.addWidget(self.lineedit_idnew_email, 4, 1, 1, 2)
        layout_idnew.addWidget(self.lineedit_idnew_phonenumber, 5, 1, 1, 2)
        layout_idnew.addWidget(self.lineedit_idnew_yzm, 6, 1, 1, 2)
        layout_idnew.addWidget(self.btn_idnew_quren, 8, 0)
        layout_idnew.addWidget(self.btn_idnew_quxiao, 8, 2)
        self.idnew.setLayout(layout_idnew)
        self.idnew.move(self.pos())
        self.idnew.resize(200, 133)
        self.idnew.setWindowTitle('千奇百怪')
        self.idnew.setWindowIcon(QIcon("C:\\Users\\Suxiansheng\\Desktop\\logo.png"))
        #self.idnew.setWindowFlags(Qt.FramelessWindowHint)
        #self.paintEvent(self)
        self.idnew.setStyleSheet("background-color :rgb(253,216,174)")
        self.idnew.show()
        #新账号注册的确认
    def Abtainyzm(self):
        if self.lineedit_idnew_email.text() == "":
            QMessageBox.warning(self, "!", "邮箱地址不能为空！", QMessageBox.Yes)
        elif Isemail(self.lineedit_idnew_email.text()):
            QMessageBox.warning(self, "!", "该email已注册！", QMessageBox.Yes)
        else:
            self.yzm = sendEmail(self.lineedit_idnew_email.text())
            return self.yzm
    def AbtainyamChange(self):
        if self.lineedit_change_email.text() == "":
            QMessageBox.warning(self, "!", "邮箱地址不能为空！", QMessageBox.Yes)
        elif Isemail(self.lineedit_change_email.text()):
            QMessageBox.warning(self, "!", "该email已注册！", QMessageBox.Yes)
        else:
            self.yzm1 = sendEmail(self.lineedit_change_email.text())
            return self.yam1
    def idnewqueren(self):

        if self.lineedit_idnew_id.text()=="":
            QMessageBox.warning(self, "!", "昵称不能为空！", QMessageBox.Yes)
        else:
            if Isid(self.lineedit_idnew_id.text()):
                if self.lineedit_idnew_password.text() == "":
                    QMessageBox.warning(self, "!", "密码不能为空！", QMessageBox.Yes)
                else:
                    if self.lineedit_idnew_qrpassword.text() == self.lineedit_idnew_password.text():
                        # print(self.yzm)
                        if self.yzm == self.lineedit_idnew_yzm.text():
                            insert_new((self.lineedit_idnew_id.text(), self.lineedit_idnew_password.text(), self.lineedit_idnew_email.text(), self.lineedit_idnew_phonenumber.text()), self.lineedit_idnew_email.text())
                            QMessageBox.warning(self, "!", "注册成功！", QMessageBox.Yes)
                            self.idnew.close()
                            #else:
                            # QMessageBox.warning(self, "!", "该email已注册", QMessageBox.Yes)
                            #self.lineedit_idnew_email.clear()
                        else:
                            QMessageBox.warning(self, "!", "验证码错误！", QMessageBox.Yes)
                            self.lineedit_idnew_yzm.clear()
                    else:
                        QMessageBox.warning(self, "!", "前后密码不一致！", QMessageBox.Yes)
                        self.lineedit_idnew_password.clear()
                        self.lineedit_idnew_qrpassword.clear()
            else:
                QMessageBox.warning(self, "!", "该用户名已存在，请更换！", QMessageBox.Yes)
                self.lineedit_idnew_id.clear()

        '''id = open("账号.txt", "r+")
        password = open("密码.txt", "r+")
        self.id_password = {}
        i = 0
        for line1 in id:
            m = i+1
            for line2 in password:
                i = i+1
                if i == m:
                    self.id_password[line1]=line2
                    break
                if i < m:
                    continue
        if  self.lineedit_idnew_id.text() == "":
            replay = QMessageBox.warning(self, "!", "账号不准为空", QMessageBox.Yes)
        else:
            if self.lineedit_idnew_id.text()+"\n" in self.id_password:
                replay = QMessageBox.warning(self, "!", "账号已存在", QMessageBox.Yes)
            else:
                if self.lineedit_idnew_password.text() == "":
                    replay = QMessageBox.warning(self, "!", "密码不准为空", QMessageBox.Yes)
                else:
                    id.write(self.lineedit_idnew_id.text()+"\n")
                    password.write(self.lineedit_idnew_password.text()+"\n")
                    replay = QMessageBox.warning(self, "!", "注册成功！", QMessageBox.Yes)
                    self.idnew.close()
        id.close()
        password.close()'''
    #添加背景图片C:\\Users\\Suxiansheng\\Desktop\\logo.png
    def changePassword(self):
        self.label_change_email = QLabel("E-mail：")
        self.label_change_password = QLabel("新 密 码：")
        self.label_change_qrpassword = QLabel("确认密码：")
        self.label_change_null1 = QLabel()
        self.label_change_null2 = QLabel()
        self.btn_change_yzm = QPushButton("获取验证码")
        self.btn_change_yzm.clicked.connect(self.AbtainyamChange)
        self.lineedit_change_email = QLineEdit()
        self.lineedit_change_email.setPlaceholderText("请输入您的email！")
        self.lineedit_change_password = QLineEdit()
        self.lineedit_change_password.setPlaceholderText("请输入新密码！")
        self.lineedit_change_qrpassword = QLineEdit()
        self.lineedit_change_qrpassword.setPlaceholderText("请再次输入密码!")
        self.lineedit_change_yzm = QLineEdit()
        self.lineedit_change_yzm.setPlaceholderText("请输入验证码！")
        self.btn_change_quren = QPushButton("确定")
        self.btn_change_quren.clicked.connect(self.idchangeQueren)
        self.btn_change_quxiao = QPushButton("取消")
        self.btn_change_quxiao.clicked.connect(self.idnewclose)
        self.change = QWidget()
        layout_change = QGridLayout()
        layout_change.addWidget(self.label_change_email, 1, 0)
        layout_change.addWidget(self.label_change_password, 2, 0)
        layout_change.addWidget(self.label_change_qrpassword, 3, 0)
        layout_change.addWidget(self.btn_change_yzm, 4, 0)
        layout_change.addWidget(self.label_change_null1, 5, 0)
        layout_change.addWidget(self.label_change_null1, 6, 0)
        layout_change.addWidget(self.lineedit_change_email, 1, 1, 1, 2)
        layout_change.addWidget(self.lineedit_change_password, 2, 1, 1, 2)
        layout_change.addWidget(self.lineedit_change_qrpassword, 3, 1, 1, 2)
        layout_change.addWidget(self.lineedit_change_yzm, 4, 1, 1, 2)
        #layout_change.addWidget(self.lineedit_idnew_phonenumber, 5, 1, 1, 2)
        #layout_change.addWidget(self.lineedit_idnew_yzm, 6, 1, 1, 2)
        layout_change.addWidget(self.btn_change_quren, 7, 0)
        layout_change.addWidget(self.btn_change_quxiao, 7, 2)
        self.change.setLayout(layout_change)
        self.change.move(self.pos())
        self.change.resize(240, 200)
        self.change.setWindowTitle('千奇百怪')
        self.change.setWindowIcon(QIcon("C:\\Users\\Suxiansheng\\Desktop\\logo.png"))
        # self.idnew.setWindowFlags(Qt.FramelessWindowHint)
        self.paintEvent(self)
        self.change.setStyleSheet("background-color :rgb(253,216,174)")
        self.change.show()

    def idchangeQueren(self):
        if self.lineedit_change_email.text() == "":
            QMessageBox.warning(self, "!", "Email不能为空！", QMessageBox.Yes)
        elif Isemail(self.lineedit_change_email.text()) :
            QMessageBox.warning(self, "!", "该账号不存在！", QMessageBox.Yes)
        else:
            if self.lineedit_change_password.text() == self.lineedit_change_qrpassword.text():
                if self.lineedit_change_yzm == self.yzm1:
                    if update_password((self.lineedit_change_password,self.lineedit_change_email)):
                        QMessageBox.warning(self, "!", "密码更改成功！", QMessageBox.Yes)
                    else:
                        QMessageBox.warning(self, "!", "密码更改失败！", QMessageBox.Yes)
                else:
                    QMessageBox.warning(self, "!", "验证码错误！", QMessageBox.Yes)
            else:
                QMessageBox.warning(self, "!", "前后密码不一致！", QMessageBox.Yes)





    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("")
        painter.drawPixmap(self.rect(), pixmap)
    #关闭创新账号窗口
    def idnewclose(self):
        self.idnew.close()
    #取消创建新账号，并退出创建窗口vvzadqtyfrmwbdjd
    def quxiao(self):
        sys.exit()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = denglu()
    d.show()
    sys.exit(app.exec())