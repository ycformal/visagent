Question: Is there lots of dry grass surrounding the zebra?

Reference Answer: yes

Image path: ./sampled_GQA/425573.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='zebra')
IMAGE0=CROP_AROUND(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is there lots of dry grass surrounding the zebra?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Answer: Runtime error: 'CROP_AROUND'

