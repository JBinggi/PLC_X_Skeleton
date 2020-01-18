$sModuleName = "Contact"
$sModuleKey = "contact"
$sTargetDir = "C:\Users\Praesidiarius\PhpstormProjects\OS\PLC_X_Contact"

# Copy Skeleton
Copy-Item -Path "../*" -Destination "$sTargetDir" -recurse -Force

