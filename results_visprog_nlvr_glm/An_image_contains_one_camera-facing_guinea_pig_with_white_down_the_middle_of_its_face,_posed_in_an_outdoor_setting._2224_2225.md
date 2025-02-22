Question: An image contains one camera-facing guinea pig with white down the middle of its face, posed in an outdoor setting.

Reference Answer: True

Left image URL: http://4.bp.blogspot.com/-DTYSe0PT_uU/UdHZvW-gBdI/AAAAAAAAIEY/HsybyKYU58M/s800/Cletus2.jpg

Right image URL: http://2.bp.blogspot.com/-V8_JBZHaqzc/UJ_IobDqNQI/AAAAAAAAAB0/DvdNlDxtaqI/s1600/3750_301320176640289_1603454502_n.jpg

Program:

```
ANSWER0=VQA(image=LEFT,question='How many guinea pigs are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many guinea pigs are in the image?')
ANSWER2=VQA(image=LEFT,question='Is the guinea pig camera-facing?')
ANSWER3=VQA(image=RIGHT,question='Is the guinea pig camera-facing?')
ANSWER4=VQA(image=LEFT,question='Is the guinea pig white down the middle of its face?')
ANSWER5=VQA(image=RIGHT,question='Is the guinea pig white down the middle of its face?')
ANSWER6=VQA(image=LEFT,question='Is the guinea pig posed in an outdoor setting?')
ANSWER7=VQA(image=RIGHT,question='Is the guinea pig posed in an outdoor setting?')
ANSWER8=EVAL(expr='{ANSWER0} == 1 and {ANSWER2} and {ANSWER4} and {ANSWER6}')
ANSWER9=EVAL(expr='{ANSWER1} == 1 and {ANSWER3} and {ANSWER5} and {ANSWER7}')
ANSWER10=E
```
Answer: Runtime error: 'E'

