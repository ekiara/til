Downloading "bestquality" often ends up with downloading an MP4 video
container, and a WEBM audio container. This is unplayable in VLC with an error
saying something similar to "Cannot play UNDF format, UNDF is Undefined". So
to fix this you need to force-download MP4 formats.


To do this you need to first list the formats with:
`python youtube-dl -F https://[YOUTUBE-LINK]`

Then you download the best quality MP4 format or just get the audio-only MP4
format (for example):
`python youtube-dl -f 140 https://[YOUTUBE-LINK]`
