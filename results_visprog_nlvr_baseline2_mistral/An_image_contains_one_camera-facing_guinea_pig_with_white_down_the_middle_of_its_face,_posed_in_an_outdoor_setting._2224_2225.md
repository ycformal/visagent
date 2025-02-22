Question: An image contains one camera-facing guinea pig with white down the middle of its face, posed in an outdoor setting.

Reference Answer: True

Left image URL: http://4.bp.blogspot.com/-DTYSe0PT_uU/UdHZvW-gBdI/AAAAAAAAIEY/HsybyKYU58M/s800/Cletus2.jpg

Right image URL: http://2.bp.blogspot.com/-V8_JBZHaqzc/UJ_IobDqNQI/AAAAAAAAAB0/DvdNlDxtaqI/s1600/3750_301320176640289_1603454502_n.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Does the image contain one camera-facing guinea pig?')
ANSWER1=VQA(image=RIGHT,question='Does the image contain one camera-facing guinea pig?')
ANSWER2=VQA(image=LEFT,question='Does the guinea pig have white down the middle of its face?')
ANSWER3=VQA(image=RIGHT,question='Does the guinea pig have white down the middle of its face?')
ANSWER4=VQA(image=LEFT,question='Is the guinea pig posed in an outdoor setting?')
ANSWER5=VQA(image=RIGHT,question='Is the guinea pig posed in an outdoor setting?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER
```
Answer: True

