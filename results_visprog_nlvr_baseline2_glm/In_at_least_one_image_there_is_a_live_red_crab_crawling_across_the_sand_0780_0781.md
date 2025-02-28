Question: In at least one image there is a live red crab crawling across the sand

Reference Answer: False

Left image URL: https://i.warosu.org/data/ck/img/0041/88/1359341966652.jpg

Right image URL: http://ww1.hdnux.com/photos/41/76/07/8905152/15/920x920.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there is a live red crab crawling across the sand' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there is a live red crab crawling across the sand' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

