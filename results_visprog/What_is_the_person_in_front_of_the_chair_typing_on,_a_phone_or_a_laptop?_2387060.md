Question: What is the person in front of the chair typing on, a phone or a laptop?

Reference Answer: The person is typing on a phone.

Image path: ./sampled_GQA/2387060.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='chair')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
IMAGE1=CROP(image=IMAGE0,box=BOX1)
ANSWER0=VQA(image=IMAGE1,question='What is the person typing on?')
ANSWER1=EVAL(expr="'phone' if {ANSWER0} == 'phone' else 'laptop'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'CROP_FRONT'

