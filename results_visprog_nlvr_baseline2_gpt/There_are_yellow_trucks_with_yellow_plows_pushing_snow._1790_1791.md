Question: There are yellow trucks with yellow plows pushing snow.

Reference Answer: False

Left image URL: http://2.bp.blogspot.com/-3V7UdTSZLw4/VLf7lzdSAqI/AAAAAAAAVAQ/iZ1mlgjF54M/s1600/Salt%2Bwaste.jpg

Right image URL: http://media.nj.com/hunterdonnews_impact/photo/county-salt-truckwebjpg-9cea388b3e1c5149.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many yellow trucks are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many yellow trucks are in the image?')
ANSWER2=VQA(image=LEFT,question='Are there yellow plows pushing snow?')
ANSWER3=VQA(image=RIGHT,question='Are there yellow plows pushing snow?')
ANSWER4=EVAL(expr='{ANSWER0} > 0 and {ANSWER1} > 0 and {ANSWER2} and {ANSWER3}')
FINAL_ANSWER=RESULT(var=ANSWER4)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='How many yellow trucks are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many yellow trucks are in the image?')
ANSWER2=VQA(image=LEFT,question='Are there yellow plows pushing snow?')
ANSWER3=VQA(image=RIGHT,question='Are there yellow plows pushing snow?')
ANSWER4=EVAL(expr='{ANSWER0} > 0 and {ANSWER1} > 0 and {ANSWER2} and {ANSWER3}')
FINAL_ANSWER=RESULT(var=ANSWER4)
```
Answer: true

