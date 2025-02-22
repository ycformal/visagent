Question: there is an ox pulling a wooden cart down a road with two people in the cart

Reference Answer: False

Left image URL: http://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Child_and_ox_ploughing%2C_Laos_%281%29.jpg/440px-Child_and_ox_ploughing%2C_Laos_%281%29.jpg

Right image URL: http://i.dailymail.co.uk/i/pix/2015/05/02/08/2837993F00000578-0-image-a-3_1430551679098.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

