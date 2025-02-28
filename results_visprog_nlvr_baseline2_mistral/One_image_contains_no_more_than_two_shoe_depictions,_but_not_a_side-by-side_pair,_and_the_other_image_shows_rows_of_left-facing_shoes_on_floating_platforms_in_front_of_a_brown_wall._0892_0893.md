Question: One image contains no more than two shoe depictions, but not a side-by-side pair, and the other image shows rows of left-facing shoes on floating platforms in front of a brown wall.

Reference Answer: True

Left image URL: https://cdn.runblogger.com/images/2014/01/new-balance-890v4-sole.jpg

Right image URL: https://s3-media3.fl.yelpcdn.com/bphoto/yUWrSQqan7gzqLUwIMfygw/ls.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='How many shoes are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many shoes are in the image?')
ANSWER2=VQA(image=LEFT,question='Are there any side-by-side pairs of shoes?')
ANSWER3=VQA(image=RIGHT,question='Are there any side-by-side pairs of shoes?')
ANSWER4=VQA(image=LEFT,question='Are there rows of left-facing shoes on floating platforms in front of a brown wall?')
ANSWER5=VQA(image=RIGHT,question='Are there rows of left-facing shoes on floating platforms in front of a brown wall?')
ANSWER6=EVAL(expr='{ANSWER0} <= 2 and not {ANSWER2}')
ANSWER7=EVAL(expr='{ANSWER1} <= 2 and not {ANSWER3}')
ANSWER8=EVAL(expr='{ANSWER4} xor {ANSWER5}')
ANSWER9=EVAL(expr='{ANSWER6
```
Answer: True

