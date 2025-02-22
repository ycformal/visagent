Question: The left and right image contains the same number of groundhog with at least one laying down.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/8v0aC84E1_o/maxresdefault.jpg

Right image URL: http://3.bp.blogspot.com/_Xt_pAKD_KQs/TGQZsvXKlSI/AAAAAAAAAM4/_SrnLX__aUU/s1600/Marmot-edit1.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many groundhogs are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many groundhogs are in the image?')
ANSWER2=VQA(image=LEFT,question='How many groundhogs are laying down?')
ANSWER3=VQA(image=RIGHT,question='How many groundhogs are laying down?')
ANSWER4=EVAL(expr='{ANSWER0} == {ANSWER1} and {ANSWER2} >= 1 and {ANSWER3} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER4)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many groundhogs are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many groundhogs are in the image?')
ANSWER2=VQA(image=LEFT,question='How many groundhogs are laying down?')
ANSWER3=VQA(image=RIGHT,question='How many groundhogs are laying down?')
ANSWER4=EVAL(expr='{ANSWER0} == {ANSWER1} and {ANSWER2} >= 1 and {ANSWER3} >= 1')
FINAL_ANSWER=RESULT(var=ANSWER4)
```
Answer: false

