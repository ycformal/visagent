Question: One image shows various fragrance bottles displayed on a mirrored tray, and the other shows rows of fragrance bottles on at least one wooden shelf.

Reference Answer: True

Left image URL: https://scentsofself.files.wordpress.com/2014/01/image.jpg

Right image URL: https://boisdejasmin.com/images/2014/11/chanel-tray.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows various fragrance bottles displayed on a mirrored tray, and the other shows rows of fragrance bottles on at least one wooden shelf.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows various fragrance bottles displayed on a mirrored tray, and the other shows rows of fragrance bottles on at least one wooden shelf.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

