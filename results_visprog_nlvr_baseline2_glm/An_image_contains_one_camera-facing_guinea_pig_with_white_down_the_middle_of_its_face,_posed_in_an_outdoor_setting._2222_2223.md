Question: An image contains one camera-facing guinea pig with white down the middle of its face, posed in an outdoor setting.

Reference Answer: True

Left image URL: http://www.cavyspirit.com/images/Pigs/BuddyTina1.jpg

Right image URL: https://i.pinimg.com/736x/aa/06/61/aa06615b56269d462979fba39e93cd14--cute-guinea-pigs-funny-guinea-pig.jpg

Original program:

```
Statement: An image contains one camera-facing guinea pig with white down the middle of its face, posed in an outdoor setting.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image contains one camera-facing guinea pig with white down the middle of its face, posed in an outdoor setting.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image contains one camera-facing guinea pig with white down the middle of its face, posed in an outdoor setting.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

