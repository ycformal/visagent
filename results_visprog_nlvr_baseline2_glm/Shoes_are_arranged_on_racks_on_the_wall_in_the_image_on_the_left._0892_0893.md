Question: Shoes are arranged on racks on the wall in the image on the left.

Reference Answer: False

Left image URL: https://cdn.runblogger.com/images/2014/01/new-balance-890v4-sole.jpg

Right image URL: https://s3-media3.fl.yelpcdn.com/bphoto/yUWrSQqan7gzqLUwIMfygw/ls.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'Shoes are arranged on racks on the wall in the image on the left.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Shoes are arranged on racks on the wall in the image on the left.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

