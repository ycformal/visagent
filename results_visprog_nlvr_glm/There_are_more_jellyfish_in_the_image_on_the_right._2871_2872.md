Question: There are more jellyfish in the image on the right.

Reference Answer: False

Left image URL: http://www.artofexcellencestudio.com/uploads/1/2/1/0/12107572/789044_orig.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/39/42/3e/39423e8e831004d8b0036d9dab18d730.jpg

Program:

```
Statement: There are more jellyfish in the image on the right.
Program:
ANSWER0=VQA(image=LEFT,question='How many jellyfish are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many jellyfish are in the image?')
ANSWER2=EVAL(expr='{ANSWER1} > {ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: 'There'

