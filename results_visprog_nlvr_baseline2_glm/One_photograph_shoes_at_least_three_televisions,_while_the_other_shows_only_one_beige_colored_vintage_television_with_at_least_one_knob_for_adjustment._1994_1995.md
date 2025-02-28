Question: One photograph shoes at least three televisions, while the other shows only one beige colored vintage television with at least one knob for adjustment.

Reference Answer: False

Left image URL: http://2.bp.blogspot.com/_5vAL3VdNeUQ/TBxwnBnnNeI/AAAAAAAAAxE/ksah2dHOkYI/s1600/P6190002.JPG

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/7e/61/aa/7e61aa64b86debe7ca04ab974b770233.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'One photograph shoes at least three televisions, while the other shows only one beige colored vintage television with at least one knob for adjustment.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One photograph shoes at least three televisions, while the other shows only one beige colored vintage television with at least one knob for adjustment.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

