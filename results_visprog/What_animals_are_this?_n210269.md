Question: What animals are this?

Reference Answer: These are horses.

Image path: ./sampled_GQA/n210269.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What animals are this?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What animals are this?')=<b><span style='color: green;'>horses</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>horses</span></b></div><hr>

Answer: horses
