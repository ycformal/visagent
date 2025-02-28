Question: The right image shows a lion interacting with at least one hyena in a scene with clouds of raised dust, and the left image shows only hyena.

Reference Answer: False

Left image URL: http://3.bp.blogspot.com/-9ueVTEWqLpk/UimcvPPgIgI/AAAAAAAAAsw/1t3PXNXkFGQ/s1600/CLOV-5.jpg

Right image URL: http://1.bp.blogspot.com/-uOCrXA5heY4/U0o2UJD51WI/AAAAAAAABDU/RWibUiADynI/s640/IMG_6333.JPG

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
ANSWER0=VQA(image=IMAGE,question="Is 'The right image shows a lion interacting with at least one hyena in a scene with clouds of raised dust, and the left image shows only hyena.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image shows a lion interacting with at least one hyena in a scene with clouds of raised dust, and the left image shows only hyena.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

