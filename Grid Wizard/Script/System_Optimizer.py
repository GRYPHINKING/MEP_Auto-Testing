def System_Optimizer():
    #Clicks the 55097 item of the 'Main' toolbar.
    Aliases.AutoSPRINKx64.wndAfx.Afx.Main.ClickItem(55097, False)
    #Clicks the 37537 item of the 'Wizards' toolbar.
    Aliases.AutoSPRINKx64.wndAfx.Afx2.Wizards.ClickItem(37537, False)
    #Clicks the 'btnFinish' button.
    Aliases.AutoSPRINKx64.dlgGridSystemIntroduction.btnFinish.ClickButton()
    #Compares the Grid_Check Stores item with the image of the Regions.CreateRegionInfo(Aliases.AutoSPRINKx64.wndAfx, 29, 79, 1781, 274, False) object.
    Regions.Grid_Check.Check(Regions.CreateRegionInfo(Aliases.AutoSPRINKx64.wndAfx, 29, 79, 1781, 274, False))
    #Clicks the 37140 item of the 'Wizards' toolbar.
    Aliases.AutoSPRINKx64.wndAfx.Afx2.Wizards.ClickItem(37140, False)
    #Clicks the 'btn' button.
    Aliases.AutoSPRINKx64.dlgGridSystemIntroduction.btn.ClickButton()
    #Compares the SystemOptimizer_dialog Stores item with the image of the Aliases.AutoSPRINKx64.dlgGridSystemIntroduction object.
    Regions.SystemOptimizer_dialog.Check(Aliases.AutoSPRINKx64.dlgGridSystemIntroduction, False, False, 23967)
    #Closes the 'dlgGridSystemIntroduction' window.
    Aliases.AutoSPRINKx64.dlgGridSystemIntroduction.Close()
