Question: four bottles total

Reference Answer: False

Left image URL: http://www.weimax.com/images/Ellen's-2010_Bday_La-Ciccia_Santandi-Vermentino.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/236x/b6/ae/40/b6ae40ad2cbb68bc8ffb3872c04d0ad1.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'four bottles total' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'four bottles total' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

