Question: Which material is used to make that hat, cloth or leather?

Reference Answer: The hat is made of cloth.

Image path: ./sampled_GQA/n181355.jpg

Program:

```
 Which material is used to make A, B or C?
Program:
ANSWER0=VQA(image=IMAGE,question='Which material is used to make that hat, cloth or leather?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which material is used to make that hat, cloth or leather?')=<b><span style='color: green;'>leather</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>leather</span></b></div><hr>

Answer: leather
