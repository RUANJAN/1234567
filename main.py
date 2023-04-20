import tkinter as tk
from tkinter import ttk
from datasoerce import CarbonFootPrint


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        root = tk.Tk()
        root.title('碳排放的窗口')
        root.geometry('200x200')

        btn = tk.Button(root,
                        text='石油',
                        font=('Arial', 30, 'bold'),
                        padx=10,
                        pady=10,
                        activeforeground='#f00'
                        )

        root.mainloop()
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
