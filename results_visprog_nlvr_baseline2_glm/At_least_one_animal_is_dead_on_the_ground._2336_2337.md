Question: At least one animal is dead on the ground.

Reference Answer: True

Left image URL: http://www.africahunting.com/hunting-pictures-videos/watermark.php?file=6182&size=1

Right image URL: http://www.africahunting.com/hunting-pictures-videos/data/501/medium/P1040014.JPG

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'At least one animal is dead on the ground.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one animal is dead on the ground.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

