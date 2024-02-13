import win32gui
import win32con


# 定义窗口类
class MyWindowClass:
    def __init__(self):
        self.hinst = win32gui.InitCommonControls()
        message_map = {
            win32con.WM_DESTROY: self.OnDestroy,
        }
        wc = win32gui.WNDCLASS()
        wc.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        wc.lpfnWndProc = message_map  # could also specify a wndproc.
        wc.cbClsExtra = 0
        wc.cbWndExtra = 0
        wc.hInstance = self.hinst
        wc.hIcon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
        wc.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
        wc.hbrBackground = win32con.COLOR_WINDOW + 1
        wc.lpszMenuName = 0  # 无菜单
        wc.lpszClassName = "MyWindowClass"
        self.classAtom = win32gui.RegisterClass(wc)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        win32gui.PostQuitMessage(0)  # 结束消息循环

    def Run(self):
        hwnd = win32gui.CreateWindow(
            self.classAtom,
            "My Python Windows API Window",
            win32con.WS_OVERLAPPEDWINDOW,
            0, 0, 400, 300,
            0, 0, self.hinst, None
        )

        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        win32gui.UpdateWindow(hwnd)

        # 进入消息循环
        win32gui.PumpMessages()


if __name__ == "__main__":
    app = MyWindowClass()
    app.Run()
