# Media - Video Serien Benennung Generator

#### Die Namensgebung und Ordnerstruktur für Filme und Serien in [Emby](https://emby.media/support/articles/TV-Naming.html#episode-naming-conventions), [Plex](https://support.plex.tv/articles/naming-and-organizing-your-tv-show-files/#toc-0) und [Jellyfin](https://jellyfin.org/docs/general/server/media/shows) wird durch bestimmte Konventionen geregelt. Der erstellte Generator ermöglicht es, diese Konventionen für ihre Media Datei einzuhalten und somit die korrekte Benennung der Videodateien sicherzustellen. Die Ausgabedatei kann in der Serienordnerstruktur genutzt werden, um die richtigen Ordner und Dateien anzulegen. 
## Screenshot
![media_generator.gif](https://github.com/Morpheus2018/media_generator/blob/main/media_generator.gif)


### Optional den gewünschten [Ausgabepfad](#L65) ändern
```
base_dir = ""#"/<pfad>/<zum>/<öffnen>" # Optional den gewünschten Pfad ändern.

def ordner_offnen(self):
    folder_path = self.season_dir
    folder_path2 = ""#"/<pfad>/<zum>/<öffnen>" # Optional den gewünschten Pfad ändern.
```
***

#### [output]()

```
Show.Name.Test.S01E01.Optional.1.Info.Episode.Text.1080p.Stereo
Show.Name.Test.S01E02.Optional.2.Info.Episode.Text.1080p.Stereo
Show.Name.Test.S01E03.Optional.3.Info.Episode.Text.1080p.Stereo
Show.Name.Test.S01E04.Optional.4.Info.Episode.Text.1080p.Stereo

Show Name Test: Season 1 (2023): Episode 1 - Optional 1 Info Episode Text
Show Name Test: Season 1 (2023): Episode 2 - Optional 2 Info Episode Text
Show Name Test: Season 1 (2023): Episode 3 - Optional 3 Info Episode Text
Show Name Test: Season 1 (2023): Episode 4 - Optional 4 Info Episode Text
```
