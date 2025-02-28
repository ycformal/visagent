Question: Each image shows one beetle with a ridged wing segment posed on some type of textured surface.

Reference Answer: True

Left image URL: http://bugguide.net/images/raw/7Q3/RQQ/7Q3RQQJR7QTR0Q00E0L0W00020DQZQ1RRQCQ80YQW0Z00Q007QR020S060DRW0R0X0OQG0UR40TQP0.jpg

Right image URL: http://www.entomart.be/nouveaux/NEO-0045-Aphodiusrufipes.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows one beetle with a ridged wing segment posed on some type of textured surface.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows one beetle with a ridged wing segment posed on some type of textured surface.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

