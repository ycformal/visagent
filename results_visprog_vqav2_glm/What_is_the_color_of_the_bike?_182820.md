Question: What is the color of the bike?

Reference Answer: black

Image path: ./sampled_GQA/182820.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the color of the bike?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the color of the bike?')=<b><span style='color: green;'>silver</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>silver</span></b></div><hr>

Answer: silver

