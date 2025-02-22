Question: There are three Collies in the right image.

Reference Answer: False

Left image URL: http://d121tcdkpp02p4.cloudfront.net/clim/143056/ayrton-senna.jpg

Right image URL: https://i.pinimg.com/736x/e0/50/4b/e0504b32aa26e840a06e7e92746bfddd--holiday-lights-a-holiday.jpg

Original program:

```
The program will ask the user how many Collies are in the right image. If the user answers 3, the program will return True. If the user answers anything other than 3, the program will return False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

