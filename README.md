# insta_cap_generator
IMPORTANT
You need to customise your post by yourself. The program is designed to produce my post structure only!

The code you need to change is the file called "cap_generator.py", where there is a function called "main()". You can customise your post there.


This helps create a standard post for your instagram account.
The example of my structure is in the "post_example.txt" file.

---
First you can gather as many related hashtags as possible and just put it into a txt file with one tag in one line. (it can be slightly modified to parse a whole chunk of copy but for the simplicity i just manually do the "one tag one line" thing)

setOfTags function will parse the information and make sure there is no duplicate.

produceCsv function is literally produce a csv file as your database.

I use random choice to pick hashtags from my database (bird.csv, animal.csv)
so every post will have at least slightly different hashtags. 



