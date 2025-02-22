Question: One dog in the image on the left is standing on the grass.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/236x/54/9e/46/549e4677e41a5d6af86f27f1ee0e18a6--beagle-puppies-beagles.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/97/01/06/97010688ed803b4868c804d486967240.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is there a dog standing on the grass?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is there a dog standing on the grass?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a dog standing on the grass?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

