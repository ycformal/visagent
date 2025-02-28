Question: Each image shows a corgi dog in a sitting pose, and the dog on the right has an open mouth while the dog on the left does not.

Reference Answer: True

Left image URL: https://i.pinimg.com/236x/fb/14/80/fb148068aed5f38357678593a1a0a456--pembroke-welsh-corgi-corgi-puppies.jpg

Right image URL: http://www.smalldogplace.com/images/Pembroke-Welsh-Corgi.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows a corgi dog in a sitting pose, and the dog on the right has an open mouth while the dog on the left does not.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows a corgi dog in a sitting pose, and the dog on the right has an open mouth while the dog on the left does not.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

