Question: Where is the cat?

Reference Answer: chair

Image path: ./sampled_GQA/142484.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='cat')
ANSWER0=LOCATION(box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'LOCATION'

