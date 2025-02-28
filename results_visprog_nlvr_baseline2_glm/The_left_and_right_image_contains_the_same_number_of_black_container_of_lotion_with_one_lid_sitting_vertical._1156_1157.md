Question: The left and right image contains the same number of black container of lotion with one lid sitting vertical.

Reference Answer: True

Left image URL: https://i.ebayimg.com/images/g/DLoAAOSw0yxZt0QW/s-l300.jpg

Right image URL: https://2.bp.blogspot.com/-dMZD4fpTFVk/WcaEA9AKDtI/AAAAAAAAGoE/RiQV7AfBk3QXSa6RK2dHaBSacEjEJT2jQCLcBGAs/s1600/lush-sleepy-lotion.jpg

Original program:

```
The program is checking if the left and right image contains the same number of black container of lotion with one lid sitting vertical. If the answer is true, then the final answer will be true, otherwise false.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains the same number of black container of lotion with one lid sitting vertical.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains the same number of black container of lotion with one lid sitting vertical.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

