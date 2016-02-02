Set-ExecutionPolicy RemoteSigned
(new-object Net.WebClient).DownloadString("http://psget.net/GetPsGet.ps1") | iex
Install-Module PSReadLine
./update_profile.ps1
