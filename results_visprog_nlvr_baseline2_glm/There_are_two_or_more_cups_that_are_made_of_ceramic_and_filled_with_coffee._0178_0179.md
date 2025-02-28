Question: There are two or more cups that are made of ceramic and filled with coffee.

Reference Answer: True

Left image URL: http://www.izocleanse.com/wp-content/uploads/2014/01/bright-eyed-bushy-tailed-coffee-loving.jpeg

Right image URL: https://s-media-cache-ak0.pinimg.com/736x/88/53/fe/8853fe7c9c65d7d1e8ed95e7b7c6cf88.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'There are two or more cups that are made of ceramic and filled with coffee.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are two or more cups that are made of ceramic and filled with coffee.' true or false?')=<b><span style='color: green;'>2</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>2</span></b></div><hr>

Answer: 2

