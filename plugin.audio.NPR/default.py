#/*
# *      Copyright (C) Fisslefink
# *
# *
# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with this program; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *
# */

import urllib2,string,xbmc,xbmcaddon,xbmcplugin,xbmcgui
from xml.dom import minidom
from urllib import quote_plus
import unicodedata

__XBMC_Revision__ = xbmc.getInfoLabel('System.BuildVersion')
__settings__      = xbmcaddon.Addon(id='plugin.audio.NPR')
__language__      = __settings__.getLocalizedString
__version__       = __settings__.getAddonInfo('version')
__cwd__           = __settings__.getAddonInfo('path')
__addonname__    = "NPR"
__addonid__      = "plugin.audio.NPR"
__author__        = "Fisslefink"


def PLAY():
  url = "http://npr.ic.llnwd.net/stream/npr_live24"
  xbmc.Player().play(url)
  

def get_params():
  param=[]
  paramstring=sys.argv[2]
  if len(paramstring)>=2:
    params=sys.argv[2]
    cleanedparams=params.replace('?','')
    if (params[len(params)-1]=='/'):
      params=params[0:len(params)-2]
    pairsofparams=cleanedparams.split('&')
    param={}
    for i in range(len(pairsofparams)):
      splitparams={}
      splitparams=pairsofparams[i].split('=')
      if (len(splitparams))==2:
        param[splitparams[0]]=splitparams[1]
  return param
  
params=get_params()
try:
  initial = params["initial"]
except:
  initial = "0";

iinitial = len(initial)

if iinitial > 1:
  PLAY()
  
else:
  u = "%s?initial=play" % (sys.argv[0],)
  liz=xbmcgui.ListItem(__language__(30090), iconImage="DefaultPlaylist.png", thumbnailImage="")
  ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
  xbmcplugin.endOfDirectory(int(sys.argv[1]))
