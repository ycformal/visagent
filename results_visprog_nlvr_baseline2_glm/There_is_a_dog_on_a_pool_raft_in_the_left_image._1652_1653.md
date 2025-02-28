Question: There is a dog on a pool raft in the left image.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/c7/8a/45/c78a45884fd9abe39b660cca91b14337.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/1b/30/7a/1b307a86a3a47b2e5559606bbbffb5a6.png

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is a dog on a pool raft in the left image.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a dog on a pool raft in the left image.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

