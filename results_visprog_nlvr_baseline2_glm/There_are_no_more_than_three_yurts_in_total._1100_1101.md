Question: There are no more than three yurts in total.

Reference Answer: True

Left image URL: http://cdn.newsapi.com.au/image/v1/40bb1907830629019edf4cb6ec65b4a0

Right image URL: https://i.pinimg.com/736x/c0/91/c1/c091c19020089cf50c0545df02ae253b--yurts-equestrian.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are no more than three yurts in total.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are no more than three yurts in total.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

