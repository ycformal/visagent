Question: The right image shows at least one 'stand-alone' anemone with tendrils radiating around it but no stalk visible.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/1c/0e/a7/1c0ea7f69701752b1fec382514a3e1d8--sea-anemone-container.jpg

Right image URL: http://www.underseaproductions.com/wp-content/uploads/2015/11/LH25004.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

