Question: Where are the people in the picture?

Reference Answer: mountain

Image path: ./sampled_GQA/390130.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='people')
ANSWER0=LOCATION(box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'LOCATION'

