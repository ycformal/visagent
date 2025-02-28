Question: The rght image contains exactly one jellyfish, which is upside-down on its mushroom-like cap.

Reference Answer: True

Left image URL: https://cdn-attachments.timesofmalta.com/69601a67d538189955dc6384cd1c9988491a52ad-1506059655-59c4a587-620x348.jpg

Right image URL: http://cdn.newsapi.com.au/image/v1/cbfea4019b5cd2ddcf2e53b5f296ebf5

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The rght image contains exactly one jellyfish, which is upside-down on its mushroom-like cap.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The rght image contains exactly one jellyfish, which is upside-down on its mushroom-like cap.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

