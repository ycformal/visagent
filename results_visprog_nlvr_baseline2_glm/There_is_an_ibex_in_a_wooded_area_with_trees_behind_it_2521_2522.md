Question: There is an ibex in a wooded area with trees behind it

Reference Answer: True

Left image URL: https://i.pinimg.com/474x/41/27/59/4127596d95cd52f06ba067ee4958b023--pyrenean-ibex-jpg.jpg

Right image URL: https://i.pinimg.com/originals/2d/7d/b5/2d7db570b8cd3223ed06de74d3eaf126.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There is an ibex in a wooded area with trees behind it' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is an ibex in a wooded area with trees behind it' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

