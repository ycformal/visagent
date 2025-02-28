Question: There is at least one multi product set in the images.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/39/19/51/39195133f1aaf8a152f0996fd32037d2--victoria-secret-love-spell-love-spells.jpg

Right image URL: http://img.auctiva.com/imgdata/1/6/5/4/2/6/6/webimg/653365538_o.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There is at least one multi product set in the images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is at least one multi product set in the images.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

