Question: Where are the kites?

Reference Answer: sky

Image path: ./sampled_GQA/245440.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='kites')
ANSWER0=LOCATION(box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'LOCATION'

