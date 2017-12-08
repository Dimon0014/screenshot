# Создание простого окна только из  Frame
import wx
filenames = ["full_snap__1510576882.png"]
class MyFrame(wx.Frame):

 def __init__(self):
               wx.Frame.__init__(self, None, -1, "My Frame", size=(300, 300))

               self.panel = wx.Panel(self, -1) # панель на которой распалагаются элементы управления, Frame - это просто рамка, -1 это индификатор через который панель и фрейм соеденяются
               self.sizer = wx.BoxSizer(wx.VERTICAL)
               img1 = wx.Image(filenames[0], wx.BITMAP_TYPE_ANY)



               self.imageBitmap = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap(img1),(30,40))
               self.sizer.Add(self.imageBitmap, 1, wx.ALIGN_RIGHT, 4)

               # w = img1.GetWidth()
               # h = img1.GetHeight()
               # # масштабируем изображения
               # img2 = img1.Scale(w / 2, h / 2)
               #
               # # делаем из изображений bitmap
               # sb1 = wx.StaticBitmap(panel, -1, wx.Bitmap(img1))
               # sb2 = wx.StaticBitmap(panel, -1, wx.Bitmap(img2))
               #
               # panel.Add(sb1)
               # panel.Add(sb2)

               self.panel.SetBackgroundColour('#FF6400')
               self.panel.SetBackgroundColour(wx.WHITE)
               self.panel.Bind(wx.EVT_MOTION, self.OnMove) # связываем панель и событие MOTION(движение мыши по панели)
                                                      # с обработчиком OnMove()
               wx.StaticText(self.panel, -1, "Pos:", pos=(10, 12)) # label статичный текст - "Pos:"
               self.posCtrl = wx.TextCtrl(self.panel, -1, "333", pos=(40, 10)) # создаем атрибут - окно Edit - текстовое
                                                                          # окошко и называем его posCtrl
#https://www.youtube.com/watch?v=cp1ZeMisTNo&list=PLejTrt5hn2r1uzZ53GDeUElXRkRFbUmQd&index=2
               button=wx.Button(self.panel, label='Exit',pos=(170,10), size=(60,30)) # создали кнопку

              # self.SetTransparent(150)
 def OnMove(self, event): # Передаем функции событие(event) в данном случае wx.EVT_MOTION
              pos = event.GetPosition()
              self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))

if __name__ == '__main__':
           app = wx.App()
           frame = MyFrame()
           frame.Show(True)
           app.MainLoop()