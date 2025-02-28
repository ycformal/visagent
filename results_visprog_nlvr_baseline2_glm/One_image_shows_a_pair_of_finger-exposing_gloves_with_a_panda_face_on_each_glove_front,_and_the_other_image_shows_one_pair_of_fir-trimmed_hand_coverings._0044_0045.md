Question: One image shows a pair of finger-exposing gloves with a panda face on each glove front, and the other image shows one pair of fir-trimmed hand coverings.

Reference Answer: False

Left image URL: https://s3-eu-west-1.amazonaws.com/images.linnlive.com/86159574884c75271b8a5a8544bc49e5/1ec72ad8-5aca-4b87-ada6-7cc8f1ac1109.jpg

Right image URL: https://d3d71ba2asa5oz.cloudfront.net/43000380/images/b437q1boysblack__1.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a pair of finger-exposing gloves with a panda face on each glove front, and the other image shows one pair of fir-trimmed hand coverings.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a pair of finger-exposing gloves with a panda face on each glove front, and the other image shows one pair of fir-trimmed hand coverings.' true or false?')=<b><span style='color: green;'>fake</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>fake</span></b></div><hr>

Answer: fake

