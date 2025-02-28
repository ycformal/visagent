Question: An image contains a single chimp, which is eating something nut-like and holding more food in its hand.

Reference Answer: True

Left image URL: http://www.chinadaily.com.cn/world/2006-05/19/xin_110503191100177163659.jpg

Right image URL: https://i.ytimg.com/vi/cy9xc2hz_y4/maxresdefault.jpg

Original program:

```
The program is designed to analyze an image and determine if it contains a single chimp that is eating something nut-like and holding more food in its hand. The program uses a series of questions to gather information about the image and then evaluates the answers to determine if the statement is true or false.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image contains a single chimp, which is eating something nut-like and holding more food in its hand.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image contains a single chimp, which is eating something nut-like and holding more food in its hand.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

