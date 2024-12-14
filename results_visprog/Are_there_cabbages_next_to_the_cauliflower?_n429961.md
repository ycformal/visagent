Question: Are there cabbages next to the cauliflower?

Reference Answer: Yes, there is a cabbage next to the cauliflower.

Image path: ./sampled_GQA/n429961.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cauliflower')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cabbages')
IMAGE1=CROP_NEXTTO(image=IMAGE0,box=BOX1)
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_NEXTTO'

