# iRCoDriver

This is a quick and dirty tool that I wrote for a fellow iRacer.
Feel free to improve it and do a pull request.


- You have to install python 3.5 and PyQt5

In the tracks folder is another folder called 249. This is the TrackID from the Nordschleife Industriefahrten.

A whole list of the tracks on iRacing and theyre ID can be found here:
https://docs.google.com/spreadsheets/d/1BRYuUOVDNYNzJsWrUz4hEt3PH9dgzuX7lK0487SdaTk/edit?usp=sharing

## How to add a track
- create a folder which name is the TrackID found in the GoogleDocs above.
- create a file with the name 'corners.txt' in it.
- in the corners.txt file write this:

    0,99999,First Corner
    
    99999,99999,EOF
- Now start iRacing with the track you want
- Start the Python script
- You can now go onto the track
  - Stop on the position where you want to hear the mp3 file and write down the integer that is displayed in the console.
  - do that for the entire track
- go into the corners.txt and write into the file the integers and cornernames that you wrote down earlier in the following way:

  [STARTCORNER],[ENDCORNER],[CORNERNAME(MP3FILENAME)]
  
- [ENDCORNER] has to be the [STARTCORNER] of the following corner. Take a look into the corners.txt in the 249 folder, you will get the idea ;-)

- record the soundfiles with for example Audacity and save them as [CORNERNAME].mp3 into the tracks/[TRACKID] folder.

That should be it.

### Have fun
