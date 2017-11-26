import wx
def show_other(evt):
    f2 = wx.Frame(None,-1)
    c = wx.Choice(f2,-1,choices=['red','blue','green'])
    f2.Show()

a = wx.App(redirect = False)


f = wx.Frame(None,-1)
b = wx.Button(f,wx.ID_OK)
b.Bind(wx.EVT_BUTTON,show_other)
f.Show()
a.MainLoop()