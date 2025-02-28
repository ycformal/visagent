Question: The balloon in the left image contains a teddy bear, the balloon in the right image contains smaller balloons.

Reference Answer: True

Left image URL: https://i.pinimg.com/originals/ef/e6/37/efe637a745d176d07d9d7efdf5bc40d7.jpg

Right image URL: http://www.balloon-decoration-guide.com/images/best-way-to-stuff-6inch-balloons-into-3ft-explosing-balloons-21739910.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'The balloon in the left image contains a teddy bear, the balloon in the right image contains smaller balloons.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The balloon in the left image contains a teddy bear, the balloon in the right image contains smaller balloons.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

