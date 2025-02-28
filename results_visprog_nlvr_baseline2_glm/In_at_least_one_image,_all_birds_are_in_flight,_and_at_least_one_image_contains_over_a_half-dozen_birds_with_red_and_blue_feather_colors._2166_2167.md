Question: In at least one image, all birds are in flight, and at least one image contains over a half-dozen birds with red and blue feather colors.

Reference Answer: False

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/04/71/93/61/botanical-garden-of-guayaquil.jpg

Right image URL: http://2.bp.blogspot.com/-ayRg9ccozAA/UGLg2je8r_I/AAAAAAAAEUA/fQ94G_ii258/s1600/0248+-+Scarlet+Macaws+3+sig.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image, all birds are in flight, and at least one image contains over a half-dozen birds with red and blue feather colors.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image, all birds are in flight, and at least one image contains over a half-dozen birds with red and blue feather colors.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

