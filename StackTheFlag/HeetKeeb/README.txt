I first looked through the files provided. I noticed that accounts tokens were created using the random library but with using a seed.
The seed being the time the account waas being made. With this information I copied how the token was made in run.py and set the time 
to the time the account we want was created. I then entered that result into the website. The website has a feature where it records the key strokes 
of the input the user gave through a keyboard heat map. I looked at the previous heat map of the account in question and found the keys 
"asertghnil" were pressed. I ran it through an online descrambler and found that the word was earthlings. When entered into the enter word page
it gives you the flag. Website layout and where the flag could be was found by looking through the templetes.

Steps:
1) Run run.py
2) Use the generated token as the input for the website
3) View the previous heat map (under view your latest heatmap in the main menu), it shows the word we should enter on the text page
4) Try the words that could have been entered
	In my case the heat map given was asertghnil
5) Once the correct word was entered it should give you the flag
	In my case earthling
Flag:
STF22{h34t_k3yb04rD}