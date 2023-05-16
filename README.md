# Media - Video Serien Benennungs Generator

#### Die Namensgebung und Ordnerstruktur für Filme und Serien in [Emby](https://emby.media/support/articles/TV-Naming.html#episode-naming-conventions), [Plex](https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/#toc-0) und [Jellyfin](https://jellyfin.org/docs/general/server/media/shows) wird durch bestimmte Konventionen geregelt. Der erstellte Generator ermöglicht es, diese Konventionen für ihre Media Datei einzuhalten und somit die korrekte Benennung der Videodateien sicherzustellen. Die Ausgabedatei kann in der Serienordnerstruktur genutzt werden, um die richtigen Ordner und Dateien anzulegen. 
## Screenshot
![media_generator_gui.gif](https://github.com/Morpheus2018/media_generator/blob/main/media_generator_gui.gif)

#### [Python GUI](https://github.com/Morpheus2018/media_generator/blob/main/GUI/media_generator_gui.py)
```
$ sudo apt-get install python3-tk
$ python3 media_generator_gui.py
$ python3 media_generator.py
```
```
Wie lautet der Name der TV-Serie? Show Name Test
Welches 'Season' ist das? 3
Wie ist die Qualität? 1080p Stereo
Welches Jahr? 2023
Wie viele Episoden sollen erstellt werden? 4
Wie lautet der Name der Episode 1? Optional 1 Info Episode Text
Wie lautet der Name der Episode 2? Optional 2 Info Episode Text
Wie lautet der Name der Episode 3? Optional 3 Info Episode Text
Wie lautet der Name der Episode 4? Optional 4 Info Episode Text
Weitere Episoden erstellen? (Ja/Nein) 
```
#### [output](https://github.com/Morpheus2018/media_generator/blob/main/Show%20Name%20Test%20(2023)/Staffel%203/Show.Name.Test.S03.txt)
```
Show.Name.Test.S03E01.Optional.1.Info.Episode.Text.1080p.Stereo
Show.Name.Test.S03E02.Optional.2.Info.Episode.Text.1080p.Stereo
Show.Name.Test.S03E03.Optional.3.Info.Episode.Text.1080p.Stereo
Show.Name.Test.S03E04.Optional.4.Info.Episode.Text.1080p.Stereo
```
***
#### [Combi GUI](https://github.com/Morpheus2018/media_generator/blob/main/GUI/media_combi_generator_gui.py)
```
$ python3 media_combi_generator.py
$ python3 media_combi_generator_gui.py
```
#### [output](https://github.com/Morpheus2018/media_generator/blob/main/GUI/Show%20Name%20Test%20(2023)/Staffel%203/Show.Name.Test.S03.txt)

```
Show.Name.Test.S03E01.Optional.1.Info.Episode.Text.1080p.Stereo
Show.Name.Test.S03E02.Optional.2.Info.Episode.Text.1080p.Stereo
Show.Name.Test.S03E03.Optional.3.Info.Episode.Text.1080p.Stereo
Show.Name.Test.S03E04.Optional.4.Info.Episode.Text.1080p.Stereo

Show Name Test: Season 3 (2023): Episode 1 - Optional 1 Info Episode Text
Show Name Test: Season 3 (2023): Episode 2 - Optional 2 Info Episode Text
Show Name Test: Season 3 (2023): Episode 3 - Optional 3 Info Episode Text
Show Name Test: Season 3 (2023): Episode 4 - Optional 4 Info Episode Text
```
***
```
$ python3 media_generator.v2.py
```
```
Show Name Test: Season 3 (2023): Episode 1 - Optional 1 Info Episode Text
Show Name Test: Season 3 (2023): Episode 2 - Optional 2 Info Episode Text
Show Name Test: Season 3 (2023): Episode 3 - Optional 3 Info Episode Text
Show Name Test: Season 3 (2023): Episode 4 - Optional 4 Info Episode Text
```