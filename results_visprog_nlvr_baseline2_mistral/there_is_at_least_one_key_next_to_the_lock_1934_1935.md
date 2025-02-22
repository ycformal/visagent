Question: there is at least one key next to the lock

Reference Answer: True

Left image URL: http://kingfisher.scene7.com/is/image/Kingfisher/3520190929686_01c

Right image URL: http://cdn.small.masterlock.com/product/orig/MLCOM_PRODUCT_22.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many keys are next to the lock?')
ANSWER1=VQA(image=RIGHT,question='How many keys are next to the lock?')
ANSWER2=EVAL(expr='{ANSWER0} >= 1 or {ANSWER1} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many keys are next to the lock?')
ANSWER1=VQA(image=RIGHT,question='How many keys are next to the lock?')
ANSWER2=EVAL(expr='{ANSWER0} >= 1 or {ANSWER1} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: true

