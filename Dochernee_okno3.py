import wx
import time


class OtherFrame(wx.Frame):
    """"""
    
    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, wx.ID_ANY, "Окно сканирования", size=wx.Size(600, 400))
        self.panel = wx.Panel(self)
        # Собственно меняющийся текст подсказка
        msg = "Кликните на кнопке запуска"
        self.instructions = wx.StaticText(self.panel, label=msg)
        
        self.msgTxt = wx.TextCtrl(self.panel, value="000")
        # self.posCtrl = wx.TextCtrl(self.panel, -1, "пусто", pos=(40, 10))
        closeBtn = wx.Button(self.panel, label="Запуск сканера")
        closeBtn.Bind(wx.EVT_BUTTON, self.Run_loop)
        self.panel.Bind(wx.EVT_LEFT_DOWN, self.onClick)
        self.SetTransparent(200)
        sizer = wx.BoxSizer(wx.VERTICAL)
        flags = wx.ALL | wx.CENTER
        sizer.Add(self.instructions, 0, flags, 2)
        sizer.Add(self.msgTxt, 0, flags, 2)  # тут у едита сайзер есть!
        # так что абсолютные значения позиционирования не нужны
        sizer.Add(closeBtn, 0, flags, 2)
        self.panel.SetSizer(sizer)
        
        self.coord_hlp = [0]*41
        
        self.coord_name =['icon','table','start','coin','0','1','2','3','4','5','6','7','8','9',
                          '10','11','12','13','14','15','16','17','18','19',
                          '20','21','22','23','24','25','26','27','28','29',
                          '30','31','32','33','34','35','36']
        self.coord = []
        self.i=0
    def onClick(self, event):
        # self.panel.BackgroundColour = wx.WHITE
      
        pos = event.GetPosition()
        self.msgTxt.SetValue("%s, %s" % (pos.x, pos.y))
        for i in range(len(self.coord_hlp)) :
            if self.coord_hlp[i]==0:
                x=pos.x
                y=pos.y
                list=[self.coord_name[i],(x,y)]
                self.coord.append(list)
                self.coord_hlp[i]=1
                print('coordinat_hlp','i=',i)
                
                self.i += 1
                if self.i <len(self.coord_hlp):
                     msg2 = "Кликните по координате %s" % self.coord_name[self.i]
                     self.instructions.SetLabel(msg2)
                #msg3 = "Кликните на кнопке запуска снова"
                #self.instructions.SetLabel(msg3)
                
                break
                time.sleep(0.01)
                
    # ----------------------------------------------------------------------
    def Run_loop(self, event):
        """
        Send a message and close frame
        """
        print(self.coord_hlp)
        
        
    
        if self.coord_hlp[self.i] == 0:
              msg2 = "Кликните по координате %s" % self.coord_name[self.i]
              
              self.instructions.SetLabel(msg2)
              print('i в лупе =',self.i)
              #time.sleep(2)
         #  my_string = "Я люблю %s" % "Python"
         #'%d %s, %d %s' % (6, 'bananas', 10, 'lemons')
        # msg = self.msgTxt.GetValue()
        
        # self.Close()


########################################################################
class MainPanel(wx.Panel):
    """"""
    
    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        self.frame = parent
        
        # Publisher().subscribe(self.showFrame, ("show.mainframe"))
        
        self.pubsubText = wx.TextCtrl(self, value="")
        hideBtn = wx.Button(self, label="Окно сканирования")
        hideBtn.Bind(wx.EVT_BUTTON, self.hideFrame)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.pubsubText, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(hideBtn, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(sizer)
    
    # ----------------------------------------------------------------------
    def hideFrame(self, event):
        """"""
        # self.frame.Hide()
        new_frame = OtherFrame()
        new_frame.Show()
    
    # ----------------------------------------------------------------------
    def showFrame(self, msg):
        """
        Shows the frame and shows the message sent in the
        text control
        """
        self.pubsubText.SetValue(msg.data)
        frame = self.GetParent()
        frame.Show()


########################################################################
class MainFrame(wx.Frame):
    # ----------------------------------------------------------------------
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, "Pubsub Tutorial")
        panel = MainPanel(self)


# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
