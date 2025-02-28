Question: The right image contains two hooved animals - at least one without horns, and the left image contains one hooved animal with curving horns.

Reference Answer: False

Left image URL: https://www.peterflack.co.za/wp-content/uploads/2016/07/articleFiveHuntableHartebeest11-1.jpg

Right image URL: https://i.ytimg.com/vi/8TQVFT6nYik/maxresdefault.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image contains two hooved animals - at least one without horns, and the left image contains one hooved animal with curving horns.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image contains two hooved animals - at least one without horns, and the left image contains one hooved animal with curving horns.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

