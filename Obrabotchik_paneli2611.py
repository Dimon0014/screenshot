#!/usr/bin/env python
import wx
import wx.lib.buttons as buttons


class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "My Frame", size=(500, 300))
		self.panel = wx.Panel(self,
							  -1)  # панель на которой распалагаются элементы управления, Frame - это просто рамка,
		#  -1 это индификатор через который панель и фрейм соеденяются
		# лучше привязать панель через self. с переди панели, тогда она будет принадлежать классу
		self.panel.SetBackgroundColour('#FF6400')
		self.panel.SetBackgroundColour(wx.WHITE)
		self.panel.Bind(wx.EVT_MOTION, self.OnMove)  # связываем панель и событие MOTION(движение мыши по панели)
		# с обработчиком OnMove()
		wx.StaticText(self.panel, -1, "Pos:", pos=(10, 12))  # label статичный текст - "Pos:"
		self.posCtrl = wx.TextCtrl(self.panel, -1, "333", pos=(40, 10))  # создаем атрибут - окно Edit - текстовое
		# окошко и называем его posCtrl
		# https://www.youtube.com/watch?v=cp1ZeMisTNo&list=PLejTrt5hn2r1uzZ53GDeUElXRkRFbUmQd&index=2
		button = wx.Button(self.panel, label='Exit', pos=(170, 10), size=(60, 30))  # создали кнопку
		
		self.SetTransparent(150)
		self.panel.Bind(wx.EVT_LEFT_DOWN, self.onClick)
	
	# self.panel.BackgroundColour = wx.RED
	# self.panel.Bind(wx.EVT_LEFT_UP, self.onClick)
	def onClick(self, event):
		#self.panel.BackgroundColour = wx.WHITE
	
		pos = event.GetPosition()
		self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))
	
	
	def OnMove(self, event):  # Передаем функции событие(event) в данном случае wx.EVT_MOTION
		pos = event.GetPosition()
	
	# self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))


if __name__ == '__main__':
	app = wx.App()
	frame = MyFrame()
	frame.Show(True)
	app.MainLoop()