Question: At least one image shows a canoe with no part touching the water and no water in the scene.

Reference Answer: False

Left image URL: http://www.fyneboatkits.co.uk/photos/products/flyfisher/flyfisher-wooden-canoe-plans.jpg

Right image URL: https://i.ytimg.com/vi/NdpT08rBU28/maxresdefault.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'At least one image shows a canoe with no part touching the water and no water in the scene.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one image shows a canoe with no part touching the water and no water in the scene.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

