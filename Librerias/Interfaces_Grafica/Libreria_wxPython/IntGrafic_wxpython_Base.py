import wx

class myFrame(wx.Frame):
     def _init_(self,parent,title):
          wx.Frame._int_(self,parent,title)

app = wx.App() # Crea un objeto de la clase App
frame = wx.Frame(None, title = "IntGrafic_wxpython_Base", size = (300,200)) # Crea un cuadro,con --size = (ancho,alto)-- podemos cambiar el tamaño del cuadro
frame.Center() # Centra el cuadro en la pantalla
frame.Show() # Muestra el cuadro

app.MainLoop() # Abre o ejecuta la ventana