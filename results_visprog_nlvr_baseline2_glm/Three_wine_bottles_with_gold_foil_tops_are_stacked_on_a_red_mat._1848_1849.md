Question: Three wine bottles with gold foil tops are stacked on a red mat.

Reference Answer: False

Left image URL: https://i.ebayimg.com/images/g/XHkAAOSwDNdVmHmW/s-l300.jpg

Right image URL: http://img.auctiva.com/imgdata/1/9/0/7/5/2/4/webimg/843289095_tp.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Three wine bottles with gold foil tops are stacked on a red mat.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Three wine bottles with gold foil tops are stacked on a red mat.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

