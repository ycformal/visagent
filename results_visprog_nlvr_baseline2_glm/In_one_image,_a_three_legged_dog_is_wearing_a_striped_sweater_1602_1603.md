Question: In one image, a three legged dog is wearing a striped sweater

Reference Answer: True

Left image URL: http://i.dailymail.co.uk/i/pix/2015/07/21/17/2AB8F4DB00000578-3169708-image-m-91_1437495054991.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/85/fb/93/85fb939294692bafefefada37f1853ec.jpg

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

