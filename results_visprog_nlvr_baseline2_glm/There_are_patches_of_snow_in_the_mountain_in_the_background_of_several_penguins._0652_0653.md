Question: There are patches of snow in the mountain in the background of several penguins.

Reference Answer: True

Left image URL: http://www.photosension.com/foto-galleri-billede/public/20080108-4849-king-penguin-colony.jpg

Right image URL: http://2.bp.blogspot.com/-9h4LZYTD94E/Ux6iPe8SZvI/AAAAAAAADDU/qMKvOY41cUA/s1600/DSC_3434.jpg

Original program:

```
The program provided is a series of questions that are asked to determine if certain statements are true or false based on the images provided. Each statement is evaluated step by step to determine if it is true or false. The final answer is then returned as a result of the evaluation.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are patches of snow in the mountain in the background of several penguins.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are patches of snow in the mountain in the background of several penguins.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

