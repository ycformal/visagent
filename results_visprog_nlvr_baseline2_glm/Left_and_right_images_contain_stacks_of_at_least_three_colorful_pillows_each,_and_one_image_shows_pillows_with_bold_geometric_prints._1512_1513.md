Question: Left and right images contain stacks of at least three colorful pillows each, and one image shows pillows with bold geometric prints.

Reference Answer: True

Left image URL: https://st2.depositphotos.com/4278641/11848/i/450/depositphotos_118484108-stock-photo-stack-of-colorful-pillows.jpg

Right image URL: https://st2.depositphotos.com/1177973/7215/i/950/depositphotos_72153041-stock-photo-stack-of-colorful-pillows.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Left and right images contain stacks of at least three colorful pillows each, and one image shows pillows with bold geometric prints.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Left and right images contain stacks of at least three colorful pillows each, and one image shows pillows with bold geometric prints.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

