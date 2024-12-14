Question: Do both the smiling gentleman in front of the picture and the Caucasian person look young?

Reference Answer: Yes, both the gentleman and the man are young.

Image path: ./sampled_GQA/n281241.jpg

Program:

```
 Do both A and B have <attr>?
Program:
BOX0=LOC(image=IMAGE,object='smiling gentleman')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='picture')
IMAGE1=CROP_BEHIND(image=IMAGE,box=BOX1)
BOX2=LOC(image=IMAGE,object='Caucasian person')
IMAGE2=CROP(image=IMAGE,box=BOX2)
ANSWER0=VQA(image=IMAGE0,question='What is the age of the smiling gentleman?')
ANSWER1=VQA(image=IMAGE2,question='What is the age of the Caucasian person?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == 'young' and {ANSWER1} == 'young' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
```
Answer: No

