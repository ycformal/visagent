Question: One image shows multiple pandas on a structure made of wooden logs, and the other shows two pandas by something that extends from the bottom of the image.

Reference Answer: True

Left image URL: http://i.dailymail.co.uk/i/pix/2016/04/17/00/3340724500000578-0-image-a-38_1460850088277.jpg

Right image URL: http://p3.img.cctvpic.com/20111024/images/1319417953111_1319417953111_r.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows multiple pandas on a structure made of wooden logs, and the other shows two pandas by something that extends from the bottom of the image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows multiple pandas on a structure made of wooden logs, and the other shows two pandas by something that extends from the bottom of the image.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

