Question: Are there airplanes in this scene that are huge?

Reference Answer: yes

Image path: ./sampled_GQA/n497658.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='Are there airplanes in this scene that are huge?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Are there airplanes in this scene that are huge?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: yes

