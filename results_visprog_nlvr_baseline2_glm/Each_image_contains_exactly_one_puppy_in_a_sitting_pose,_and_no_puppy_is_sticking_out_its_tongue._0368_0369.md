Question: Each image contains exactly one puppy in a sitting pose, and no puppy is sticking out its tongue.

Reference Answer: True

Left image URL: https://www.pupcdn.com/photo/puppy/525026/59e11bb60aa39-3903729.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/736x/f3/bf/1f/f3bf1f00fc58be3e1460f49e206ef0c5.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains exactly one puppy in a sitting pose, and no puppy is sticking out its tongue.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains exactly one puppy in a sitting pose, and no puppy is sticking out its tongue.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

