Question: How wide is the bucket?

Reference Answer: wide

Image path: ./sampled_GQA/n309148.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='bucket')
ANSWER0=WIDTH(box=BOX0)
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'WIDTH'

