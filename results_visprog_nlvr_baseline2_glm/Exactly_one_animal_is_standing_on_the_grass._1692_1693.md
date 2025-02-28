Question: Exactly one animal is standing on the grass.

Reference Answer: False

Left image URL: https://static9.depositphotos.com/1435513/1151/i/950/depositphotos_11514969-stock-photo-hartebeest-in-etosha-national-park.jpg

Right image URL: https://static8.depositphotos.com/1355265/830/i/950/depositphotos_8302574-stock-photo-a-group-of-red-hartebeest.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Exactly one animal is standing on the grass.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Exactly one animal is standing on the grass.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

