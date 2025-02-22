Question: An image shows a large silver-framed sliding glass door that is open, revealing swivel office chairs around a table on brown carpeting.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/50/41/08/5041087941fa825ec2bd4223f819917a.jpg

Right image URL: https://i.pinimg.com/originals/64/40/d9/6440d94b3932b0239ff6965380dda9f6.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Does the image show a large silver-framed sliding glass door?')
ANSWER1=VQA(image=RIGHT,question='Does the image show a large silver-framed sliding glass door?')
ANSWER2=VQA(image=LEFT,question='Is the door open?')
ANSWER3=VQA(image=RIGHT,question='Is the door open?')
ANSWER4=VQA(image=LEFT,question='Does the image show swivel office chairs around a table on brown carpeting?')
ANSWER5=VQA(image=RIGHT,question='Does the image show swivel office chairs around a table on brown carpeting?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var
```
Answer: True

