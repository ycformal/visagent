Question: A hand is in the image of the dog on the left, and the right image shows a chihuahua chewing something stick-like.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/67/67/3d/67673d545827f9acd87f506b5ac03558.jpg

Right image URL: http://www.famouschihuahua.com/wp-content/uploads/2011/08/jemma-chihuahua.jpg

Original program:

```
Statement: A hand is in the image of the dog on the left, and the right image shows a chihuahua chewing something stick-like.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A hand is in the image of the dog on the left, and the right image shows a chihuahua chewing something stick-like.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A hand is in the image of the dog on the left, and the right image shows a chihuahua chewing something stick-like.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

