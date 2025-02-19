Question: Is the small calf in the bottom part of the image?

Reference Answer: yes

Image path: ./sampled_GQA/n331357.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='calf')
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
ANSWER0=COUNT(box=IMAGE0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: yes

