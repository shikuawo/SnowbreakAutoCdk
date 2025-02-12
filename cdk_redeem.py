from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyboardController
import time
import tkinter as tk
from tkinter import messagebox, scrolledtext

# 初始化鼠标和键盘控制
mouse = Controller()
keyboard = KeyboardController()

# 移动并点击鼠标的函数
def move_and_click(x, y, delay=0.5):
    mouse.position = (x, y)  # 移动鼠标到指定位置
    time.sleep(delay)
    mouse.click(Button.left, 1)  # 左键点击
    time.sleep(1)  # 等待 1 秒

# 兑换 CDK
def redeem_cdk():
    cdk_text = cdk_entry.get("1.0", tk.END).strip()  # 获取用户输入的CDK（多行）
    cdk_list = [cdk.strip() for cdk in cdk_text.split("\n") if cdk.strip()]  # 按行分割，并去掉空白行

    if not cdk_list:
        messagebox.showerror("错误", "请输入至少一个 CDK！")
        return

    # **1. 先进行初始化点击**
    move_and_click(2481, 39)   # 点击顶部区域
    move_and_click(213, 1002)  # 点击底部区域
    time.sleep(2)  # 稍作延迟，确保初始化完成

    # **2. 开始兑换 CDK**
    for cdk in cdk_list:
        print(f"正在兑换：{cdk}")  # 控制台输出，方便调试

        # 1. 点击 "前往兑换"
        move_and_click(2111, 770)

        # 2. 点击 "兑换码" 输入框
        move_and_click(1268, 662)

        # 3. 输入 CDK
        keyboard.type(cdk)
        time.sleep(1)

        # 4. 点击 "确认" 按钮
        move_and_click(1795, 999)
        time.sleep(2)  # 防止兑换太快

    messagebox.showinfo("完成", f"{len(cdk_list)} 个 CDK 兑换完成！")

# 创建 UI
root = tk.Tk()
root.title("自动兑换 CDK")
root.geometry("400x300")  # 窗口大小

# CDK 输入框（多行，可滚动）
tk.Label(root, text="请输入 CDK（一行一个，兄弟别当伪人）").pack(pady=5)
cdk_entry = scrolledtext.ScrolledText(root, width=50, height=8, wrap=tk.WORD)
cdk_entry.pack(pady=5)

# 开始按钮
start_button = tk.Button(root, text="开始兑换", command=redeem_cdk, height=2, width=20)
start_button.pack(pady=10)

# 运行 Tkinter 主循环
root.mainloop()
