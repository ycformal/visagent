Question: An image contains a single elephant, and that elephant has its trunk raised and curled back toward its forehead.

Reference Answer: True

Left image URL: http://999thepoint.com/files/2016/09/image4.jpeg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/0d/01/83/a7/one-of-their-two-asian.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

