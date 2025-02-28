Question: Where are the signs in the photograph?

Reference Answer: center

Image path: ./sampled_GQA/123239.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='signs')
ANSWER0=LOCATION(box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'LOCATION'

