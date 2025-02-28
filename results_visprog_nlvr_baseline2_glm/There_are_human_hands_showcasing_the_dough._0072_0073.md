Question: There are human hands showcasing the dough.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/736x/2d/18/a5/2d18a557ac70d3e2e8664bcfbea599a1.jpg

Right image URL: http://4.bp.blogspot.com/-REFgCJU_yR4/VNiqMbGanDI/AAAAAAAAIvw/8eLTlTBWBpE/s1600/Napoleonthreeside.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are human hands showcasing the dough.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are human hands showcasing the dough.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

