$sModuleName = "Tag"
$sModuleKey = "tag"
$sTargetDir = "C:\Users\Praesidiarius\PhpstormProjects\OS\PLC_X_Tag_NoGIT"

# Copy Skeleton
Copy-Item -Path "..\*" -Destination "$sTargetDir" -recurse -Force