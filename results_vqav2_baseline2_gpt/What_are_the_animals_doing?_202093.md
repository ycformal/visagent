Question: What are the animals doing?

Reference Answer: standing

Image path: ./sampled_GQA/202093.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='What are the animals doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='What are the animals doing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What are the animals doing?')=<b><span style='color: green;'>standing</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>standing</span></b></div><hr>

Answer: standing

