Question: What animals are it?

Reference Answer: The animals are goats.

Image path: ./sampled_GQA/n86120.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What animals are it?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What animals are it?')=<b><span style='color: green;'>cows</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>cows</span></b></div><hr>

Answer: cows
