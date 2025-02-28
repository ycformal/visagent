Question: One image contains two bottles displayed side-by-side but not overlapping, and the other image contains a single water bottle with a black loop top.

Reference Answer: True

Left image URL: https://ssli.ebayimg.com/images/g/wX8AAOSw42JWEWBs/s-l640.jpg

Right image URL: https://sc02.alicdn.com/kf/HTB1Syt_mdbJ8KJjy1zjq6yqapXad/Aluminum-Alu-Metal-Magic-Sport-Water-Bottle.jpg_640x640xz.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One image contains two bottles displayed side-by-side but not overlapping, and the other image contains a single water bottle with a black loop top.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image contains two bottles displayed side-by-side but not overlapping, and the other image contains a single water bottle with a black loop top.' true or false?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>1</span></b></div><hr>

Answer: 1

