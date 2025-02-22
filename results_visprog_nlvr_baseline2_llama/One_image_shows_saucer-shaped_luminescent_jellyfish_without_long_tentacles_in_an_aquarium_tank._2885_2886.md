Question: One image shows saucer-shaped luminescent jellyfish without long tentacles in an aquarium tank.

Reference Answer: True

Left image URL: https://i.ytimg.com/vi/2KTJ8GAWlEs/hqdefault.jpg

Right image URL: http://reefkeeping.com/issues/2003-01/gt/images/rroverflow3.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Are the jellyfish saucer-shaped?')
ANSWER1=VQA(image=RIGHT,question='Are the jellyfish saucer-shaped?')
ANSWER2=VQA(image=LEFT,question='Are the jellyfish luminescent?')
ANSWER3=VQA(image=RIGHT,question='Are the jellyfish luminescent?')
ANSWER4=VQA(image=LEFT,question='Are the jellyfish without long tentacles?')
ANSWER5=VQA(image=RIGHT,question='Are the jellyfish without long tentacles?')
ANSWER6=VQA(image=LEFT,question='Are the jellyfish in an aquarium tank?')
ANSWER7=VQA(image=RIGHT,question='Are the jellyfish in an aquarium tank?')
ANSWER8=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4} and {ANSWER6}')
ANSWER9=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5} and {ANSWER7}')
ANSWER10=EVAL(expr='{ANSWER8} xor {ANSWER9}')
FINAL_ANSWER=RESULT(var=ANS
```
Answer: false

