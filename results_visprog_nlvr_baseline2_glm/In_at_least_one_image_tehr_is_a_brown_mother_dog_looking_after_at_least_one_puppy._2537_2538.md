Question: In at least one image tehr is a brown mother dog looking after at least one puppy.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/736x/29/54/c7/2954c7cdb24de5a67c0c6c68d27ce565.jpg

Right image URL: https://i.pinimg.com/736x/99/59/04/99590493b2477691a3c54b1084b90352---month-olds--months.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image tehr is a brown mother dog looking after at least one puppy.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image tehr is a brown mother dog looking after at least one puppy.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

