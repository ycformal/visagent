Question: A smiley face is in the milk foam of a latte.

Reference Answer: False

Left image URL: http://4.bp.blogspot.com/-SkIX7G1rvVQ/UWKoU8HeyWI/AAAAAAAAA7Q/Fj_ONDSFTes/s640/207556_15734885_lz.jpg

Right image URL: https://i.pinimg.com/originals/10/80/f6/1080f6b6e91f0c1df6a1162a78ceb576.jpg

Original program:

```
Statement: A smiley face is in the milk foam of a latte.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A smiley face is in the milk foam of a latte.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A smiley face is in the milk foam of a latte.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

