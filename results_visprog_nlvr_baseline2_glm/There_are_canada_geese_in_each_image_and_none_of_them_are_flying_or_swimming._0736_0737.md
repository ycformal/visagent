Question: There are canada geese in each image and none of them are flying or swimming.

Reference Answer: True

Left image URL: http://media.al.com/sports_impact/photo/canada-geese-wiki-commonsjpg-36caedd9205871e0.jpg

Right image URL: http://dcforest.weebly.com/uploads/2/6/6/2/26628144/6735776.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are canada geese in each image and none of them are flying or swimming.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are canada geese in each image and none of them are flying or swimming.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

