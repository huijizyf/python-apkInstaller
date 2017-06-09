#-*- coding: UTF-8 -*- 
from Tkinter import *
import os
import commands
import tkMessageBox

class Application(Frame):
    apk_list=list()
    listbox=''
    logbox=''
    def __init__(self, master=None):
        self.init_apk_list()
        Frame.__init__(self, master,height=80,width=80)
        self.listbox  = Listbox(self,width=50,selectmode=MULTIPLE) 
        self.logbox=Listbox(self,width=50,height=20)
        self.pack()
        self.init_ui()

    def init_apk_list(self):
        pathDir =  os.listdir("./apk")
        for sub_file in pathDir:
            print sub_file
            if(sub_file.endswith('.apk')):
                self.apk_list.append(sub_file)
    
    def init_ui(self):
        for apk_name in self.apk_list:
            self.listbox.insert(END,apk_name)
        self.listbox.pack()
        selectAllBtn=Button(self,text="全部选中",command=self.selectAll)
        selectAllBtn.pack()
        install_btn=Button(self,text="开始安装",command=self.start_install_apk)
        install_btn.pack()
        self.logbox.pack()

    def selectAll(self):
        self.listbox.selection_set(0,self.listbox.size())


    def start_install_apk(self):
        successed=0
        failed=0
        selected=self.listbox.curselection()
        self.logbox.insert(END,"准备安装apk")
        self.logbox.insert(END,"共有"+str(self.listbox.size())+"个应用，将有"+str(len(selected))+"个应用被安装")
        self.logbox.insert(END,"")
        self.logbox.insert(END,"--------------------------------------------")
        self.logbox.insert(END,"")
        for index in selected:
            apk=self.apk_list[index]
            self.logbox.insert(END,"准备安装: "+apk)
            (status, output) = commands.getstatusoutput('adb install -r ./apk/'+apk)
            print status,output
            if status==0 and ("Success" in output):
                self.logbox.insert(END,"安装成功: "+apk)
                successed=successed+1
            else:
                self.logbox.insert(END,"安装失败: "+apk)
                self.logbox.insert(END,"失败信息:"+output)
                failed=failed+1
            self.logbox.insert(END,"")
            self.update_idletasks()
        self.logbox.insert(END,"--------------------------------------------")
        self.logbox.insert(END,"应用安装结束！！")
        self.logbox.insert(END,"--------------------------------------------")
        self.logbox.insert(END,"安装成功："+str(successed)+"个,安装失败："+str(failed)+"个，请查看上方日志")
            


app = Application()
app.master.title('APK安装器')
app.mainloop()