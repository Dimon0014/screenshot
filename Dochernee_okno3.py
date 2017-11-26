import wx

class OtherFrame(wx.Frame):
	""""""
	
	# ----------------------------------------------------------------------
	def __init__(self):
		"""Constructor"""
		wx.Frame.__init__(self, None, wx.ID_ANY, "Secondary Frame",size=wx.Size(600, 400) )
		self.panel = wx.Panel(self)
		   # Собственно меняющийся текст подсказка
		msg = "Кликните на первой координате"
		self.instructions = wx.StaticText(self.panel, label=msg)
		
		#self.msgTxt = wx.TextCtrl(panel, value="")
		closeBtn = wx.Button(self.panel, label="Запуск сканера")
		closeBtn.Bind(wx.EVT_BUTTON, self.Run_loop)
		self.SetTransparent(200)
		sizer = wx.BoxSizer(wx.VERTICAL)
		flags = wx.ALL | wx.CENTER
		sizer.Add(self.instructions, 0, flags, 5)
		#sizer.Add(self.msgTxt, 0, flags, 5)
		sizer.Add(closeBtn, 0, flags, 5)
		self.panel.SetSizer(sizer)
	
	# ----------------------------------------------------------------------
	def Run_loop(self, event):
		"""
		Send a message and close frame
		"""
		
		msg2 = "Кликните по второй координате"
		self.instructions.SetLabel(msg2)
		
		#msg = self.msgTxt.GetValue()
		
		#self.Close()


########################################################################
class MainPanel(wx.Panel):
	""""""
	
	# ----------------------------------------------------------------------
	def __init__(self, parent):
		"""Constructor"""
		wx.Panel.__init__(self, parent=parent)
		self.frame = parent
		
		#Publisher().subscribe(self.showFrame, ("show.mainframe"))
		
		self.pubsubText = wx.TextCtrl(self, value="")
		hideBtn = wx.Button(self, label="Hide")
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