Question: Each image shows a corgi dog in a sitting pose, and the dog on the right has an open mouth while the dog on the left does not.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/f7/8f/f6/f78ff6c0b7e574dc219948efe5ef6bde--seasons-welsh-corgi.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/e6/44/67/e644672a224f3dd77e340bfefe8fb631.jpg

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

