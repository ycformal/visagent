Question: Where are the engines?

Reference Answer: back

Image path: ./sampled_GQA/466005.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='engines')
ANSWER0=LOCATION(box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'LOCATION'

