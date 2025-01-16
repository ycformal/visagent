Question: How is the water?

Reference Answer: The water is choppy.

Image path: ./sampled_GQA/2366091.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='How is the water?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How is the water?')=<b><span style='color: green;'>calm</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>calm</span></b></div><hr>

Answer: calm

