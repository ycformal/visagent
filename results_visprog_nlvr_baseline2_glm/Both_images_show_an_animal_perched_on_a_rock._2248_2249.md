Question: Both images show an animal perched on a rock.

Reference Answer: False

Left image URL: https://get.pxhere.com/photo/cute-wildlife-mammal-squirrel-rodent-fauna-whiskers-friends-animals-vertebrate-marmot-prairie-dog-fox-squirrel-1405114.jpg

Right image URL: https://i.pinimg.com/originals/59/3f/45/593f45c4a8d8dbf5ca860edabcafb304.jpg

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

