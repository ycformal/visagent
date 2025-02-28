Question: All seals are shown out of the water, and at least one is draped over a rock and reclining on its belly.

Reference Answer: True

Left image URL: http://thecraftycanvas.com/photography-portfolio/files/2013/05/lazy-sunbathing-seal-national-zoo.jpg

Right image URL: https://3.bp.blogspot.com/-F-bNL5Gk1M8/VeGZiloB7RI/AAAAAAAAAdk/yTWZf_AElR8By9-04XhyG-4ORoUdZsYiwCPcB/s1600/california_sea_lion_5_Big.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'All seals are shown out of the water, and at least one is draped over a rock and reclining on its belly.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'All seals are shown out of the water, and at least one is draped over a rock and reclining on its belly.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

