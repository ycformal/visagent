Question: There are two white cups with handles next to each other.

Reference Answer: False

Left image URL: https://i.ebayimg.com/images/g/d8cAAOSw4GVYUrLW/s-l300.jpg

Right image URL: https://img0.etsystatic.com/160/0/13290615/il_340x270.1108380758_ha22.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are two white cups with handles next to each other.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are two white cups with handles next to each other.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

