import tkinter as tk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import tkinter.simpledialog as simpledialog

from dbutil import db

# 显示成绩柱状图
def show_score():
    plt.rcParams['font.sans-serif'] = ['SimHei']
    sql = "select course from scores group by course order by course "
    labels = []
    for i in db().select(sql): labels.append(i[0])
    print(labels)
    sql="select max(score) from scores group by course order by course "
    high =[]
    for i in db().select(sql): high.append(i[0])
    print(high)
    sql="select cast(avg(score) as int) from scores group by course order by course "
    medium = []
    for i in db().select(sql): medium.append(i[0])
    print(medium)
    sql="select min(score) from scores group by course order by course "
    low =  []
    for i in db().select(sql): low.append(i[0])
    print(low)
    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width*2/3, high, width  , label='最高分')
    rects2 = ax.bar(x, medium, width , label='平均分')
    rects3 = ax.bar(x + width*2/3 , low, width, label='最低分')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('成绩')
    ax.set_title('成绩信息统计')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    fig.tight_layout()
    plt.show()

def show_course(course):
    scores=[0,0,0,0,0]
    for s in course:
        if s[3]<=60: scores[0]=scores[0]+1
        if s[3]<=70 and s[3]>61: scores[0]=scores[0]+1
        if s[3]<=80 and s[3]>71: scores[1]=scores[1]+1
        if s[3]<=90 and s[3]>81: scores[2]=scores[2]+1
        if s[3]<=100 and s[3]>90: scores[3]=scores[3]+1

    labels = '90~100', '81~90', '71~80', '61~70', '60以下'
    sizes = scores

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()

def show_student(stu):
    matplotlib.rcParams['font.family'] = 'Simhei'
    course=[]
    scores=[]
    for s in stu:
        course.append(s[2])
        scores.append(s[3])
    radar_labels = np.array(course)
    data = np.array(scores)
    angles = np.linspace(0, 2 * np.pi, len(course), endpoint=False)
    fig = plt.figure(facecolor="white")
    plt.subplot(111, polar=True)
    plt.plot(angles, data, 'o-', linewidth=1, alpha=0.2)
    plt.fill(angles, data, alpha=0.25)
    plt.thetagrids(angles * 180 / np.pi, radar_labels)
    plt.grid(True)
    plt.savefig('holland_radar.jpg')
    plt.show()

# 菜单类
class menu (object):
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

    # 学生按钮点击
    def student(self):
        # 输入学号
        stu=simpledialog.askstring('学号','请输入学号')
        sql="select * from scores where stu='"+stu+"'"
        result=db().select(sql)
        show_student(result)

    # 课程按钮点击
    def course(self):
        course = simpledialog.askstring('课程', '请输入课程名')
        sql="select * from scores where course='"+course+"'"
        result=db().select(sql)
        show_course(result)

    # 成绩按钮点击
    def scores(self):
        show_score()



class view():
    def __init__(self):
        # 启动登录界面
        root= tk.Tk()
        root.title('数据查看')
        menu(root)
        root.mainloop()

view()
