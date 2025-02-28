Question: The right image shows a top view of just one forward-facing purplish crab, and the left image shows the underside of a forward-facing crab that is raising its 'head'.

Reference Answer: False

Left image URL: https://sc01.alicdn.com/kf/UTB8rIWtXhHEXKJk43Jeq6yeeXXan/LIVE-MUD-CRAB-LIve-King-Crab-LIve.jpg

Right image URL: https://i.ytimg.com/vi/z9zWeZwgHNQ/maxresdefault.jpg

Original program:

```
The statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image shows a top view of just one forward-facing purplish crab, and the left image shows the underside of a forward-facing crab that is raising its 'head'.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image shows a top view of just one forward-facing purplish crab, and the left image shows the underside of a forward-facing crab that is raising its 'head'.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

