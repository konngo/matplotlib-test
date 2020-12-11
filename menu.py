from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

class views (object):
    def __init__(self, master=None):
        self.window = master
        self.window.title("菜单")
        self.window.geometry('%dx%d' % (300, 300))
        self.draw()

    def draw(self):
        self.page = Frame(self.window)  # 创建Frame
        self.page.pack()
        # 1. 指定学生信息统计
        Button(self.page, text='学生信息统计', command=self.student).grid(row=1,column=1, stick=E, pady=10)
        # 2. 指定课程信息统计
        Button(self.page, text='课程信息统计', command=self.course).grid(row=2,column=1, stick=E, pady=10)        # 2. 指定课程信息统计
        # 3. 课程成绩
        Button(self.page, text='课程成绩分布', command=self.scores).grid(row=3,column=1, stick=E, pady=10)        # 2. 指定课程信息统计

    def student(self):
        self.show_student(1)

    def show_student(self,stu):
        matplotlib.rcParams['font.family'] = 'Simhei'
        radar_labels = np.array(['数学', '语文', '英语', '化学', '物理', '地理'])
        data = np.array([55, 78, 12, 74, 23, 86])
        angles = np.linspace(0, 2 * np.pi, 6, endpoint=False)
        fig = plt.figure(facecolor="white")
        plt.subplot(111, polar=True)
        plt.plot(angles, data, 'o-', linewidth=1, alpha=0.2)
        plt.fill(angles, data, alpha=0.25)
        plt.thetagrids(angles * 180 / np.pi, radar_labels)
        plt.grid(True)
        plt.savefig('holland_radar.jpg')
        plt.show()

    def course(self):
        print("student1")
        self.show_course(1)

    def show_course(self,course):
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        labels = ['娱乐', '育儿', '饮食', '房贷', '交通', '其它']
        sizes = [2, 5, 12, 70, 2, 9]
        explode = (0, 0, 0, 0.1, 0, 0)
        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
        plt.title("饼图示例-8月份家庭支出")
        plt.show()

    def scores(self):
        print("student2")
