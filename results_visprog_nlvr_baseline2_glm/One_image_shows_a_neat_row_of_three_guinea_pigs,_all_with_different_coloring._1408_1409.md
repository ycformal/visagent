Question: One image shows a neat row of three guinea pigs, all with different coloring.

Reference Answer: False

Left image URL: https://i.pinimg.com/236x/30/ab/00/30ab00468a7bddbceaf9796ee00bcce3--mike-dantoni-hamsters.jpg

Right image URL: https://laughingsquid.com/wp-content/uploads/2015/01/three-little-hamsters-live-in-a.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a neat row of three guinea pigs, all with different coloring.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a neat row of three guinea pigs, all with different coloring.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

