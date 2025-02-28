Question: Where are the zebras?

Reference Answer: outside

Image path: ./sampled_GQA/42534.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='zebras')
ANSWER0=LOCATION(box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'LOCATION'

