Question: What color are the flowers?

Reference Answer: green

Image path: ./sampled_GQA/474170.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What color are the flowers?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What color are the flowers?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What color are the flowers?')=<b><span style='color: green;'>white</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>white</span></b></div><hr>

Answer: white

