#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
# 导入ttk
from tkinter import ttk
# 导入filedialog
from tkinter import filedialog

from tkinter import messagebox as msgbox
import codecs
import chardet



class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()



    def initWidgets(self):
        self.labelDest = Label(self)
        self.labelDest["text"] = '编码:'
        self.cmb = ttk.Combobox(self.master)
        self.cmb.pack()
        # 设置下拉菜单中的值
        self.cmb['value'] = ('utf-8', 'GBK')
        # 创建按钮，并为之绑定事件处理函数
        ttk.Button(self.master, text='Open File',
                   command=self.open_file  # 绑定open_file方法
                   ).pack(side=BOTTOM, ipadx=150, ipady=100)

    def open_file(self):
        # 调用askopenfile方法获取单个打开的文件
        file_path = filedialog.askopenfilename(title='打开单个文件',
                                               filetypes=[("文本文件", "*.txt"), ('csv', '*.csv')],
                                               # 只处理的文件类型
                                               initialdir='./')  # 初始目录
        msgbox.showinfo(title='提示', message="文件路径:"+file_path+"要转换的格式："+self.cmb.get())
        print("文件路径:"+file_path)
        print("要转换的格式："+self.cmb.get())
        self.convert(file_path,self.cmb.get())
        msgbox.showinfo(title='提示', message='处理完成')

    def convert(self,file_name, out_code="UTF-8"):
        """
        该程序用于将目录下的文件从指定格式转换到指定格式，默认的是GBK转到UTF-8
        :param file:    文件路径
        :param in_code:  输入文件格式
        :param out_code: 输出文件格式
        :return:
        """
        # !!! does not backup the origin file
        content = codecs.open(file_name, 'rb').read()
        in_code = chardet.detect(content)['encoding']
        print("源文件格式："+in_code)
        out_path = './'
        try:
            with codecs.open(file_name, 'r', in_code) as f_in:
                new_content = f_in.read()
                f_out = codecs.open(file_name, 'w', out_code)
                f_out.write(new_content)
                f_out.close
        except IOError as err:
            print("I/O error: {0}".format(err))

    def convert_file_to_utf8(self, filename, out_code="UTF-8"):


        # !!! does not backup the origin file
        content = codecs.open(filename, 'rb').read()
        print(content)
        source_encoding = chardet.detect(content)['encoding']
        print(source_encoding)
        if source_encoding == None:
            print("encoding is None: %s" % filename)
            return
        print("[%s]--->[%s]: %s" % (filename, source_encoding, out_code))
        if source_encoding != out_code:
            codecs.open(filename, 'w', encoding=out_code).write(content)


root = Tk()
root.title("文件编码转换")
App(root)
root.mainloop()
