Question: In at least one of the photos, there is a heart.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/0b/c6/db/0bc6dbfeda7a5298179e09d88ae1f958--love-lock-padlocks.jpg

Right image URL: https://i.pinimg.com/736x/7a/bd/f0/7abdf0db55caf2f3e3d884ab8dbc3f22--padlocks-spinning.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one of the photos, there is a heart.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one of the photos, there is a heart.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

