#!/usr/bin/python

# bitmap.py

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (370, 370))
        self.panel = wx.Panel(self, -1)
        self.bitmap = wx.Bitmap('myImage17.bmp')
        #wx.EVT_PAINT(self, self.OnPaint)
        self.panel.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Centre()

    def OnPaint(self, event):
        dc = wx.PaintDC(self.panel)
        # wdx, wdy = self.panel.GetSize()
        # ox = (wdx - self._dx) / 2
        # oy = (wdy - self._dy) / 2
        # print(ox, oy)
        dc.DrawBitmap(self.bitmap,  50, 60)


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'Memento')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop()