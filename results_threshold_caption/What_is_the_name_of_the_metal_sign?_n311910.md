Question: What is the name of the metal sign?

Reference Answer: The sign is a street sign.

Image path: ./sampled_GQA/n311910.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the name of the metal sign?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the name of the metal sign?')=<b><span style='color: green;'>street sign</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>street sign</span></b></div><hr>

Answer: street sign
