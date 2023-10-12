def Start_App_Update_Parts():
    #Clicks the 'DesktopWindowXamlSource' object.
    Aliases.explorer.wndShell_TrayWnd.DesktopWindowXamlSource.Click(1067, 24)
    #Clicks the '|Desktop|ProgramData' item of the 'tvNamespaceTreeControl' tree.
    Aliases.explorer.wndHome.Home.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.NamespaceTreeControl.tvNamespaceTreeControl.ClickItem("|Desktop|ProgramData")
    #Double-clicks the 'Name' object.
    Aliases.explorer.wndHome.Home.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink2.ShellView.Items_View.AutoSPRINK_2023.Name.DblClick(36, 5)
    #Clicks the 'Name' object.
    Aliases.explorer.wndHome.Home.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink2.ShellView.Items_View.Parts_mdb.Name.Click(26, 8)
    #Enters '[Del]' in the 'Parts_mdb' object.
    Aliases.explorer.wndHome.Home.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink2.ShellView.Items_View.Parts_mdb.Keys("[Del]")
    #Clicks the 'Name' object.
    Aliases.explorer.wndHome.Home.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink2.ShellView.Items_View.Parts_mdb.Name.Click(26, 8)
    #Enters '[Del]' in the 'Parts_mdb' object.
    Aliases.explorer.wndHome.Home.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink2.ShellView.Items_View.Parts_mdb.Keys("[Del]")
    #Closes the 'wndHome' window.
    Aliases.explorer.wndHome.Close()
    #Runs the "AutoSPRINKx64" tested application.
    TestedApps.AutoSPRINKx64.Run(1, True)
    #Delays the test execution for the specified time period.
    Delay(8000, "Wait for Update Parts Dialog")
    #Clicks the 'btnYes' button.
    Aliases.AutoSPRINKx64.dlgGridSystemIntroduction.btnYes.ClickButton()
    #Clicks the 'btnOK' button.
    Aliases.AutoSPRINKx64.dlgGridSystemIntroduction.btnOK.ClickButton()
