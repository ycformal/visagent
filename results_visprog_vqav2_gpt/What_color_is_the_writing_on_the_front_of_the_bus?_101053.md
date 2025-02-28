Question: What color is the writing on the front of the bus?

Reference Answer: blue

Image path: ./sampled_GQA/101053.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bus')
IMAGE0=CROP_FRONT(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the writing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_FRONT'

