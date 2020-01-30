#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import shutil
import glob
import errno, stat

"""  
createmodulefromskeleton.py - Create your own module form a oneplace Skeleton
 Renames all modules and cleanup code structure
 Usage: createmodulefromskeleton.py path/to/module modulename

 @author Verein onePlace
 @copyright (C) 2020  Verein onePlace <admin@1plc.ch>
 @license https://opensource.org/licenses/BSD-3-Clause
 @version 1.0.1
 @since 1.0.0
"""

# Remove Files and Folders (wildcard only for files)
aToDelFiles = []
aToDelFiles.append("/data/*.sh")
aToDelFiles.append("/data/*.ps1")
aToDelFiles.append("/data/*.py")
aToDelFiles.append("/view/layout/*default.phtml")
aToDelFiles.append("/CHANGELOG.md")
aToDelFiles.append("/mkdocs.yml")

aToDelDirs = []
aToDelDirs.append("/.git")
aToDelDirs.append("/docs/book")

# Whitelist from renaming
aWhiteList = []
aWhiteList.append("/language/")

sSkeletonName = "Skeleton"
sVersionFile = "Module.php"

def printHelp():
  print("Create a new Module based on the current PLC_X_Skeleton")
  print("Run it directly inside /data/")
  print("Using:")
  print(sys.argv[0] + " path/to/module modulename")
  exit(1)


def remove_readonly(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    import stat
    if not os.access(path, os.W_OK):
        # Is the error an access error ?
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

# Convert Module Name for Skeleton to skeleton or vs
def getModulname(name, upper = True):
  if(name[0].islower() and upper):
    name = name[0].upper() + name[1:]
  if(name[0].isupper() and not upper): 
    name = name[0].lower()+ name[1:]
  return name
  

# check if module name is provided
if len(sys.argv) < 2 :
  printHelp()

sScriptPath = os.path.realpath(__file__)
sModulePath = sys.argv[1]
sModuleName = sys.argv[2]

# check if path is occupied
if os.path.exists(sys.argv[1]):
  print("Module exists, move ,delete or rename your Module")
  #print(sModulePath)
  #shutil.rmtree(sModulePath, ignore_errors=False, onerror=remove_readonly)
  exit(1)
  
#check if the context is right
try:
  f = open("../src/Module.php", "r")
except IOError:
  print("Error wrong context " + sModulePath + "\n")
  printHelp()




print("Creating oneplace module at " + sModulePath + "\n")
# copy skeleton
try:
  shutil.copytree("../", sModulePath)
except IOError as err:
  print("Cant create module "+ "\n" + format(err))



# Remove folders
for dir in aToDelDirs:
  try:
    print("delete " + sModulePath+dir)
    shutil.rmtree(sModulePath+dir, ignore_errors=False, onerror=remove_readonly)
  except:
    print("Error while deleting file : ", sModulePath+dir)

# delete files
for fileList in aToDelFiles:
  for filePath in glob.glob(sModulePath+fileList):
    try:
      print("delete " + filePath)
      os.remove(filePath)
    except:
      print("Error while deleting file : ", filePath)
    
sSkel_s = getModulname(sSkeletonName,False)
sSkel_S = getModulname(sSkeletonName,True)

sModul_s = getModulname(sModuleName,False)
sModul_S = getModulname(sModuleName,True)

# this while loop is only for folder recursive renaming issue
bFinish = False
while not bFinish:
  bFinish = True
  # rename all folders
  for root, dirs, files in os.walk(sModulePath):
    path = root.split(os.sep)
    for dir in dirs:
      sSource = dir
      # rename all Folders from skeleton to moduleName
      if sSkel_s in dir:
        sDest = dir.replace(sSkel_s,sModul_s)
        print("rename  " + os.path.join(root,sSource) + " to " + os.path.join(root,sDest))
        os.rename(os.path.join(root,sSource), os.path.join(root,sDest))
        bFinish = False # dirty solution
        break
      # rename all Folders from Skeleton to ModuleName
      if sSkel_S in dir:
        sDest = dir.replace(sSkel_S,sModul_S)
        print("rename" +  sSource + " to " + sDest)
        bFinish = False # dirty solution
        os.rename(sSource, sDest)
        break

#rename all files
ignore=False
for root, dirs, files in os.walk(sModulePath):
  # rename all Files from Skeleton to ModuleName
  for file in files:
    sSource = file
    # ignore whitelisted files
    for url in aWhiteList:
      path = os.path.join(root,sSource)
      if path.find(url) > 0:
        print("ignore " + path)
        ignore = True

    if ignore:
      ignore=False
      continue

    if sSkel_s in file:
      sDest = file.replace(sSkel_s, sModul_s)
      print("rename  " + os.path.join(root,sSource) + " to " + os.path.join(root,sDest))
      os.rename(os.path.join(root,sSource), os.path.join(root,sDest))

      # rename all Folders from Skeleton to ModuleName
    if sSkel_S in file:
      sDest = file.replace(sSkel_S, sModul_S)
      print("rename  " + os.path.join(root,sSource) + " to " + os.path.join(root,sDest))
      os.rename(os.path.join(root,sSource), os.path.join(root,sDest))

# all renaming inside files happens here:
for root, dirs, files in os.walk(sModulePath):
  # rename all Files from Skeleton to ModuleName
  for file in files:
    sSource = os.path.join(root,file)
    sSourceTemp = os.path.join(root,file + "_temp")

    # ignore whitelisted files
    for url in aWhiteList:
      if sSource.find(url) > 0:
        ignore = True

    if ignore:
      ignore = False
      continue

    fp = open(sSource,"r")
    fpW = open(sSourceTemp,"w")
    try:
      for line in fp:
        # set Version to default 1.0.0
        #
        #print(sSource.find(sVersionFile))
        if sSource.find(sVersionFile) > 0 and line.find("VERSION") > 0:
          print("set module version to 1.0.0")
          fpW.write("    const VERSION = '1.0.0';")
        else:
          # replace skeleton name
          line = line.replace(sSkel_S, sModul_S)
          line = line.replace(sSkel_s, sModul_s)
          fpW.write(line)
    except:
      print("Error while renaming file : ", sModulePath + dir)


    fp.close()
    os.remove(sSource)
    fpW.close()
    os.rename(sSourceTemp, sSource)

