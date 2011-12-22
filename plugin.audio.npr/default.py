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


import sys,urlparse,xbmc,xbmcaddon,xbmcplugin,xbmcgui

__XBMC_Revision__ = xbmc.getInfoLabel('System.BuildVersion')
__settings__      = xbmcaddon.Addon(id='plugin.audio.npr')
__language__      = __settings__.getLocalizedString
__version__       = __settings__.getAddonInfo('version')
__cwd__           = __settings__.getAddonInfo('path')
__addonname__     = "NPR - National Public Radio"
__addonid__       = "plugin.audio.npr"
__author__        = "Stieg,Fisslefink"


_IDS = [
  1,
  2,
  151,
]

_ID_INFO = {
  1 : {
    'name' : __language__(30090),
    'url'  : 'http://npr.ic.llnwd.net/stream/npr_live24',
    },
  2 : {
    'name' : __language__(30091),
    'url'  : 'http://sc9.sjc.llnw.net:80/stream/npr_music2',
    },
  151 : {
    'name' : __language__(30092),
    'url'  : 'http://www.kqed.org/radio/listen/kqedradio.pls',
    },
}

def play_station_id(sid):
  station = _ID_INFO.get(int(sid))
  print ("Playing %s at %s" % (station.get('name'), station.get('url')))
  xbmc.Player().play(station['url'])


def url_query_to_dict(url):
  ''' Returns the URL query args parsed into a dictionary '''
  param = {}
  if url:
    u = urlparse.urlparse(url)
    for q in u.query.split('&'):
      kvp = q.split('=')
      param[kvp[0]] = kvp[1]

  return param


def main():
  params = url_query_to_dict(sys.argv[2])
  station_id = params.get('id')

  if station_id:
    print("Station #%s selected" % station_id)
    play_station_id(station_id)
  else:
    print("No station selected.")
    for i in _IDS:
      u = sys.argv[0] + "?id=" + str(i)
      station = _ID_INFO.get(i)
      liz = xbmcgui.ListItem(station.get('name'),
                             iconImage="DefaultPlaylist.png",
                             thumbnailImage="")
      xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]),
                                  url = u,listitem = liz,
				  isFolder = False)

    xbmcplugin.endOfDirectory(int(sys.argv[1]))


# Enter here.
main()
