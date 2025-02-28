Question: There are exactly three empty containers in the image on the left.

Reference Answer: False

Left image URL: https://image.dhgate.com/0x0/f2/albu/g1/M01/FA/F9/rBVaGVZ-qTeAD8bDAAJ3687Dn84349.jpg

Right image URL: https://image.dhgate.com/0x0/f2/albu/g1/M00/A9/F1/rBVaGFn2sySANL4CAALt6SIAKf0404.jpg

Original program:

```
The program is asking if there are exactly three empty containers in the image on the left. The program does this by asking the user how many empty containers are in the image on the left and then evaluating the expression '{ANSWER0} == 3'. If the user answers that there are three empty containers in the image on the left, then the program will return True. If the user answers that there are not three empty containers in the image on the left, then the program will return False.
####
True
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are exactly three empty containers in the image on the left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are exactly three empty containers in the image on the left.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

