Question: Who is standing?

Reference Answer: The boy is standing.

Image path: ./sampled_GQA/2358945.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Who is standing?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Who is standing?')=<b><span style='color: green;'>boy</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>boy</span></b></div><hr>

Answer: boy
