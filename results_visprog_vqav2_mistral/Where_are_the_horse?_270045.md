Question: Where are the horse?

Reference Answer: beach

Image path: ./sampled_GQA/270045.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='horse')
ANSWER0=LOCATION(box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'LOCATION'

