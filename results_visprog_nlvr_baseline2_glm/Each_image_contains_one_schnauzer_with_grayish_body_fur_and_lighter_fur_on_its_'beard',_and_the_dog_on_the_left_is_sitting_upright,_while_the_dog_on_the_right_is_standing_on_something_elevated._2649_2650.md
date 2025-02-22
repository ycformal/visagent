Question: Each image contains one schnauzer with grayish body fur and lighter fur on its 'beard', and the dog on the left is sitting upright, while the dog on the right is standing on something elevated.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/bb/55/ba/bb55bafe1500ac3cb67f3c8ca9d93766--hair-chalk-hair-dye.jpg

Right image URL: http://4.bp.blogspot.com/-tFguWHwTEZw/U2QLL9VtnAI/AAAAAAAAAd4/mTwrCpnj8DE/s1600/miniature-schnauzer+another+pets.jpg

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

