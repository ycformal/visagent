Question: There are two small furry mammals facing opposite directions.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/8v0aC84E1_o/maxresdefault.jpg

Right image URL: http://3.bp.blogspot.com/_Xt_pAKD_KQs/TGQZsvXKlSI/AAAAAAAAAM4/_SrnLX__aUU/s1600/Marmot-edit1.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are two small furry mammals facing opposite directions.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are two small furry mammals facing opposite directions.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

