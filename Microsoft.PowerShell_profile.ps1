#base profile setting
$user = "Administrator"
$user_home = "C:\Users\$user"
$project = "C:\Projects"
$script_path = "$project\scripts"
$script = $script_path
$update_profile_script = "$script\update_profile.ps1"
$pfx86 = "C:\Program Files (x86)"
$pfx64 = "C:\Program Files"
$pfptb = "C:\Portable Application"
$app_data = "$user_home\AppData"
$app_local = "$app_data\Local"
$desktop = "$user_home\Desktop\"
$start_up = "$app_data\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\"

Function update-profile {
    .$update_profile_script
}

Function desktop{ cd $desktop ; }
Function project{ cd $project ;}

function global:prompt
{  
    $my_path = $(get-location).toString()  
    Write-Host ("PS ") -nonewline -foregroundcolor 'Green'
    Write-Host ($my_path) -nonewline -foregroundcolor 'Green' 
    Write-Host (">") -nonewline -foregroundcolor 'Green' 
    return " "  
}  

#shortcuts

Function ping-baidu {
    if($args){
        ping www.baidu.com $args
    }else{
        ping www.baidu.com -n 10
    }
}

Function ping-github {
    if($args){
        ping github.com $args
    }else{
        ping github.com -n 10
    }
    
}

Function list-path {
    $env:PATH.Split(";")
}

$qq_path = "$pfx86\Tencent\QQ\Bin\QQScLauncher.exe"
$wechat_path = "$pfx86\Tencent\WeChat\WeChat.exe"
$pycharm_path = "$pfx86\JetBrains\PyCharm Community Edition 5.0.4\bin\pycharm.exe"
$thunder_path = "$pfx86\Thunder Network\Thunder\Program\Thunder.exe"
$redis_gui_path = "$pfx86\RedisDesktopManager\rdm.exe"
$vs_path = "$pfx86\Microsoft Visual Studio 12.0\Common7\IDE\devenv.exe"
$firefox_path = "$pfx64\Mozilla Firefox\firefox.exe"
$sublime_path = "$pfptb\Sublime Text 2.0.2 x64\sublime_text.exe"
$ss_local_dir = "$pfptb\Shadowsocks-win\"
$proxifier_path = "$pfptb\\Proxifier PE\Proxifier.exe"
$youdao_path = "$app_local\Youdao\Dict\Application\YodaoDict.exe"
$github_dir = "$app_local\GitHub"
$github_path = "$github_dir\GitHub.appref-ms"
$ss_local_path = "$ss_local_dir\Shadowsocks.exe"
$ss_local_config = "$ss_local_dir\gui-config.json"
$iss_reconfig_script = "$script_path\iss_reconfig.py"

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

Function sublimep{
    If($args){
        $folder_path = "$project\$args"
        sublime $folder_path
    }else{
        sublime
    }
}

Function music{
    If($args){
        ."o:\Audio\Inventory\$args-playlist.dpl"
    }else{
        ."o:\Audio\Inventory\0-playlist.dpl"
    }
    
}


Function qq{ Start-Process -FilePath $qq_path ;}

Function github{ Start-Process -FilePath $github_path ;}

Function git-shell{."$github_dir\shell.ps1"}

Function wechat{ Start-Process -FilePath $wechat_path ;}

Function firefox{ Start-Process -FilePath $firefox_path -WindowStyle Maximized ;}

Function youdao{ Start-Process -FilePath $youdao_path ;}

Function fanyi { python "$script_path\stable\fanyi.py" $args ;}

Function xunlei { Start-Process -FilePath $thunder_path ;}

Function thunder { xunlei ;}

Function redis-gui { Start-Process -FilePath $redis_gui_path ;}

Function vs { Start-Process -FilePath $vs_path ;}

Function proxifier{Start-Process -FilePath $proxifier_path ;}

Function ss-global{
    If($args -eq "close"){
         Get-Process | Where-Object {$_.Path -like "*Proxifier*"} | Stop-Process
    }else{
         proxifier
    }
}

Function ss-local{
    If($args -eq "close"){
        Get-Process | Where-Object {$_.Path -like "*Shadowsocks*"} | Stop-Process
    }elseif ($args -eq "restart") {
        ss-local "close"
        ss-local         
    }else{
        Start-Process -FilePath $ss_local_path ;
    }   
}

Function ss-ping{
    ."$script\ping-ss-server.bat"
}

Function add-startup {
    copy $args $start_up
}