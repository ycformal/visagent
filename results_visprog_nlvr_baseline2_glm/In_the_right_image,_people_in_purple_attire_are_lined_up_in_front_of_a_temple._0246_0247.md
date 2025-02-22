Question: In the right image, people in purple attire are lined up in front of a temple.

Reference Answer: False

Left image URL: http://d27k8xmh3cuzik.cloudfront.net/wp-content/uploads/2017/11/Distant-view-of-Lingdum-Monastery-in-Sikkim-ss28112016.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/01/67/8d/3d/rumtek-monastery.jpg

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

