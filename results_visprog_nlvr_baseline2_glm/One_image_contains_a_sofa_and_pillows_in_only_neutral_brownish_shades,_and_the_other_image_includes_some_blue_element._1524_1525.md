Question: One image contains a sofa and pillows in only neutral brownish shades, and the other image includes some blue element.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/d0/bc/8e/d0bc8ec4c9e13e45162ca313071d02c9--decorative-accents-accent-pillows.jpg

Right image URL: https://i5.walmartimages.com/asr/782c597d-83a7-4d94-bde8-492d5285dc6a_1.2b4e8ee562119efce221fc7e7755b605.jpeg

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
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

