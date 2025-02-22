Question: In at least one image there is a sailfish mounted on the wall.

Reference Answer: False

Left image URL: http://hgtvhome.sndimg.com/content/dam/images/hgrm/fullset/2014/4/8/0/hgtv-01-sh14-great-room_h.jpg.rend.hgtvcom.231.174.suffix/1405468842791.jpeg

Right image URL: http://hgtvhome.sndimg.com/content/dam/images/hgtv/fullset/2013/3/4/0/sh13_22-living-room-EPP7953_4x3.jpg.rend.hgtvcom.616.462.suffix/1400953040850.jpeg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

