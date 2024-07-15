# -*- coding: utf-8 -*-
import sys

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"人脸识别"), pos = wx.DefaultPosition, size = wx.Size( 300,330 ), style = wx.DEFAULT_FRAME_STYLE^wx.TAB_TRAVERSAL^wx.RESIZE_BORDER^wx.MAXIMIZE_BOX )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )


        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class MainPanel
###########################################################################

class MainPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 300,300 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        MainPanelSizer1 = wx.BoxSizer( wx.VERTICAL )

        MainPanelSizer1_1 = wx.BoxSizer( wx.HORIZONTAL )


        MainPanelSizer1_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.originalPic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 92,112 ), 0 )
        MainPanelSizer1_1.Add( self.originalPic, 0, wx.ALL, 5 )


        MainPanelSizer1_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.detectedPic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 92,112 ), 0 )
        MainPanelSizer1_1.Add( self.detectedPic, 0, wx.ALL, 5 )


        MainPanelSizer1_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


        MainPanelSizer1.Add( MainPanelSizer1_1, 1, wx.EXPAND, 5 )

        self.PrintTextCtrl = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,120 ), wx.TE_MULTILINE)
        MainPanelSizer1.Add( self.PrintTextCtrl, 0, wx.ALL, 5 )

        MainPanelSizer1_2 = wx.BoxSizer( wx.VERTICAL )

        MainPanelSizer1_2_1 = wx.BoxSizer( wx.HORIZONTAL )

        self.PicPicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, 0 )
        MainPanelSizer1_2_1.Add( self.PicPicker, 0, wx.ALL, 5 )


        MainPanelSizer1_2_1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

        self.Comfirmbtn = wx.Button( self, wx.ID_ANY, _(u"识别"), wx.DefaultPosition, wx.DefaultSize, 0 )
        MainPanelSizer1_2_1.Add( self.Comfirmbtn, 0, wx.ALL, 5 )

        self.Exitbtn = wx.Button( self, wx.ID_ANY, _(u"退出"), wx.DefaultPosition, wx.DefaultSize, 0 )
        MainPanelSizer1_2_1.Add( self.Exitbtn, 0, wx.ALL, 5 )


        MainPanelSizer1_2.Add( MainPanelSizer1_2_1, 1, wx.EXPAND, 5 )


        MainPanelSizer1.Add( MainPanelSizer1_2, 1, wx.EXPAND, 5 )


        self.SetSizer( MainPanelSizer1 )
        self.Layout()

        # Connect Events
        self.PicPicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.PicPickerFunction )
        self.Comfirmbtn.Bind( wx.EVT_BUTTON, self.ComfirmbtnFunction )
        self.Exitbtn.Bind( wx.EVT_BUTTON, self.ExitbtnFunction )

        reprint = RedirectTextCtrl(self.PrintTextCtrl)
        sys.stdout = reprint

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def PicPickerFunction( self, event ):
        event.Skip()

    def ComfirmbtnFunction( self, event ):
        event.Skip()

    def ExitbtnFunction( self, event ):
        event.Skip()

class RedirectTextCtrl(object):
    def __init__(self,aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)

