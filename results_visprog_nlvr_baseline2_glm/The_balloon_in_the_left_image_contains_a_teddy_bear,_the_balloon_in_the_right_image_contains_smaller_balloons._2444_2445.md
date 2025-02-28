Question: The balloon in the left image contains a teddy bear, the balloon in the right image contains smaller balloons.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/236x/59/f4/6e/59f46ededc9242053281dcaac60c7bf6--balloon-ideas--i.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/e3/ea/f0/e3eaf0c3eeee479a750b168714af4ddd.jpg

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

