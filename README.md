# Onmyoji
Repo for my 3 years' life


## 多开方法
取消UAC，主窗口以管理员启动，其余窗口正常启动即可。
修改注册表
'''
1: reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers" /v "C:\Program Files (x86)\Onmyoji\Launch.exe" /t REG_SZ /d RunAsInvoker
'''
其中'''C:\Program Files (x86)\Onmyoji\Launch.exe'''改为阴阳师的启动程序路径，保存为bat文件，点击即可。
参考自nga，https://bbs.nga.cn/read.php?tid=16564444&fav=a70d2ec0