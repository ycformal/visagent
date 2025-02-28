Question: One image shows balloons on strings that gather to a point against a blue sky, but no one holding the balloons.

Reference Answer: True

Left image URL: https://st.depositphotos.com/1063346/1362/i/950/depositphotos_13625661-stock-photo-group-of-various-colored-balloons.jpg

Right image URL: https://images.freeimages.com/images/premium/large-thumbs/1203/12038329-happy-young-girl-holding-a-bunch-of-balloons-outside.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows balloons on strings that gather to a point against a blue sky, but no one holding the balloons.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows balloons on strings that gather to a point against a blue sky, but no one holding the balloons.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

