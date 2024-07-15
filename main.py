import UI
import forecast
import wx

class MainFrame(UI.MainFrame):
    def __init__(self, parent):
        UI.MainFrame.__init__(self, parent)
        self.Panel = MainPanel(self)
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_close(self, event):
        app.Destroy()
        wx.Exit()

class MainPanel(UI.MainPanel):
    def __init__(self, parent):
        UI.MainPanel.__init__(self, parent)

    def PicPickerFunction( self, event ):
        self.Path1 = self.PicPicker.GetPath()
        img = wx.Image(self.Path1)
        self.originalPic.SetBitmap(img)
        self.originalPic.Update()
        self.originalPic.Refresh()

    def ComfirmbtnFunction(self, event):
        self.PrintTextCtrl.Clear()

        # 调用 forecast 方法并获取路径
        self.Path2 = forecast.forecast(self.Path1)

        # 检查 Path2 是否为 None
        if self.Path2 is not None:
            try:
                # 从给定路径加载图像
                img = wx.Image(self.Path2, wx.BITMAP_TYPE_ANY)
                self.detectedPic.SetBitmap(wx.Bitmap(img))
            except Exception as e:
                # 处理加载图像时可能发生的其他异常
                wx.MessageBox(f"加载图像失败: {e}", "错误", wx.ICON_ERROR)
        else:
            # 处理 Path2 为 None 的情况
            wx.MessageBox("未匹配到人脸！", "错误", wx.ICON_ERROR)

        self.detectedPic.Update()
        self.detectedPic.Refresh()


    def ExitbtnFunction( self, event ):
        app.Destroy()
        wx.Exit()


app = wx.App(False)
Frame = MainFrame(None)
Frame.Show(True)
app.MainLoop()
