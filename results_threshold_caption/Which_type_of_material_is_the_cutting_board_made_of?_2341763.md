Question: Which type of material is the cutting board made of?

Reference Answer: The cutting board is made of wood.

Image path: ./sampled_GQA/2341763.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Which type of material is the cutting board made of?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Which type of material is the cutting board made of?')=<b><span style='color: green;'>wood</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>wood</span></b></div><hr>

Answer: wood
