Question: Where is the paper cup lid?

Reference Answer: on glass

Image path: ./sampled_GQA/371864.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='paper cup lid')
ANSWER0=LOCATION(box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'LOCATION'

