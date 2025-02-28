Question: Three or more humans are visible.

Reference Answer: True

Left image URL: http://namibianhuntingsafaris.com/wp-content/uploads/2014/12/hunting-namibia-077.jpg

Right image URL: http://www.namibiahuntingsafaris.com/wp-content/uploads/2012/03/cheetah-hunting.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Three or more humans are visible.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Three or more humans are visible.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

