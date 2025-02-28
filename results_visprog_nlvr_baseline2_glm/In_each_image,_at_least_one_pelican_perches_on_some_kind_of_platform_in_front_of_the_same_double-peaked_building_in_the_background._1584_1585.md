Question: In each image, at least one pelican perches on some kind of platform in front of the same double-peaked building in the background.

Reference Answer: False

Left image URL: https://rossmansloop.files.wordpress.com/2013/02/53-best-pelican-shot.jpg

Right image URL: https://t3.ftcdn.net/jpg/01/54/35/16/240_F_154351680_rrzO7oPrLHQcksyTX8R2SCzhPfn9iXtQ.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In each image, at least one pelican perches on some kind of platform in front of the same double-peaked building in the background.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In each image, at least one pelican perches on some kind of platform in front of the same double-peaked building in the background.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

