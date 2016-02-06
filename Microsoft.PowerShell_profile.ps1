#base profile setting
$script_path = "C:\Projects\scripts\"
$script = $script_path
$update_profile_script = "C:\Projects\scripts\update_profile.ps1"

Function update_profile {
    .$update_profile_script
}

Function desktop{ cd c:\Users\Administrator\Desktop\ ; }
Function project{ cd c:\Projects\ ;}

function prompt  
{  
    $my_path = $(get-location).toString()  
    Write-Host ("PS ") -nonewline -foregroundcolor 'Green'
    Write-Host ($my_path) -nonewline -foregroundcolor 'Green' 
    Write-Host (">") -nonewline -foregroundcolor 'Green'  
    return " "  
}  

#shortcuts

Function ping_baidu {
    if($args){
        ping www.baidu.com $args
    }else{
        ping www.baidu.com -n 10
    }
}

Function ping_github {
    if($args){
        ping github.com $args
    }else{
        ping github.com -n 10
    }
    
}

$qq_path = "C:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe"
$sublime_path = "c:\Portable Application\Sublime Text 2.0.2 x64\sublime_text.exe"
$github_path = "C:\Users\Administrator\AppData\Local\GitHub\GitHub.appref-ms"
$wechat_path = "C:\Program Files (x86)\Tencent\WeChat\WeChat.exe"
$firefox_path = "C:\Program Files\Mozilla Firefox\firefox.exe"
$youdao_path = "C:\Users\Administrator\AppData\Local\Youdao\Dict\Application\YodaoDict.exe"
$pycharm_path = "C:\Program Files (x86)\JetBrains\PyCharm Community Edition 5.0.4\bin\pycharm.exe"
$ss_local_dir = "C:\Portable Application\Shadowsocks-win\"
$ss_local_path = "$ss_local_dir\Shadowsocks.exe"
$ss_local_config = "$ss_local_dir\gui-config.json"
$iss_reconfig_script = "$script_path\iss_reconfig.py"
$thunder_path = "C:\Program Files (x86)\Thunder Network\Thunder\Program\Thunder.exe"

Function pycharm{
    If($args){
        Start-Process -FilePath $pycharm_path -WindowStyle Maximized -ArgumentList "$args"
    }else{
        Start-Process -FilePath $pycharm_path -WindowStyle Maximized
    }
}

Function sublime{   
    If($args){
        Start-Process -FilePath $sublime_path -WindowStyle Maximized -ArgumentList "$args"
    }else{
        Start-Process -FilePath $sublime_path -WindowStyle Maximized
    }
}

Function music{
    If($args){
        ."o:\Audio\Inventory\$args-playlist.dpl"
    }else{
        o:\Audio\Inventory\$args-playlist.dpl
    }
    
}

Function ss_local{
    Start-Process -FilePath $ss_local_path ;
}

Function kill_ss_local{
    Get-Process | Where-Object {$_.Path -like "*Shadowsocks*"} | Stop-Process
}

Function ss_local_restart{
    python $iss_reconfig_script $ss_local_config
    kill_ss_local
    ss_local
}


Function qq{ Start-Process -FilePath $qq_path ;}

Function github{ Start-Process -FilePath $github_path ;}

Function wechat{ Start-Process -FilePath $wechat_path ;}

Function firefox{ Start-Process -FilePath $firefox_path -WindowStyle maximized ;}

Function youdao{ Start-Process -FilePath $youdao_path ;}

Function fanyi {
    python "$script_path\stable\fanyi.py" $args
}

Function xunlei {
    Start-Process -FilePath $thunder_path
}

Function thunder {
    xunlei
}


