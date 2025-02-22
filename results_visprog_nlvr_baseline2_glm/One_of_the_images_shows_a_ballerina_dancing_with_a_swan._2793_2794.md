Question: One of the images shows a ballerina dancing with a swan.

Reference Answer: True

Left image URL: http://www.lovevalencia.com/wp-content/uploads/2012/01/lago_de_los_cisnes_240504_t0.jpg

Right image URL: http://ilarge.lisimg.com/image/2454555/800full-maya-plisetskaya.jpg

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

