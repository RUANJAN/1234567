import tkinter as tk
from tkinter import ttk
from tkinter import Button
from datasoerce import CarbonFootPrint


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_add('*font',('verdana', 12, 'bold'))
        self.title("碳排放量")

        Button(self, text='石油').pack(side=LEFT)
        Button(self, text='煤炭').pack(side=LEFT)
        Button(self, text='天然氣').pack(side=LEFT)

if __name__ == "__main__":
    window = Window()
    window.mainloop()
    '''
娟娟的按鈕
'''


# 主程式
def main():

    try:
        aqi_list = CarbonFootPrint.download_aqi()
        print(type(aqi_list))

    except Exception as err:
        print(str(err))
        return

    window = Window()
    window.title("碳足跡CarbonFootPrint改一次title")
    window.mainloop()


# 啟動點
if __name__ == "__main__":
    main()
