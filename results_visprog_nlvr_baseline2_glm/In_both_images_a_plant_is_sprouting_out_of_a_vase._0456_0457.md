Question: In both images a plant is sprouting out of a vase.

Reference Answer: True

Left image URL: https://i.pinimg.com/236x/8d/29/90/8d2990ee45b7c2915ce14263d0ece0e8--plastic-spoon-crafts-plastic-spoons.jpg

Right image URL: http://www.craftberrybush.com/wp-content/uploads/2012/09/IMG_9170.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In both images a plant is sprouting out of a vase.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAxAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0XW9KlnguYLTY0rLiMMcgH3rHn0aW01CNZL6UAoFKIzLhsAkg56E5/Krep6gNIuX8642EtgLnmtQzQeTCU2um0OT13Me+fxrL2UW7vdA7ljwtBLZ6U9pcXs95KJWk82VcHacYXj0xVPUdUS11jUbc7xiyicsR8uCz9/UBTV+C8S1LBULM4GcdqxdYmj1HUTC8R8sQBpwRgFckBc+/P4ZqqlSNODk+gatmE9jNq2m6c5lCMqgsGHQHmmahqn9mJHBANiDK/l3p134neK4KRIu2PqmOMUl3BZ6oiTb/ACvMXJ718vWmq03Onp1NOho6NetqVmpkf5FbLD+96VqXD72THas7Rk061tPJWUuy8bVGPxrZjgRmLLBLtxkHcD+navocI3KhHW5DauVtvAoYZqw8eFVlVsHseoqEjtW47ldlKmkblasFeKjcDFAFMrzRUhxmigCzNpMepX7XV/PPtiyRGz/IRzwBjiomls47YRW8HlohChI2xhenHt3rE1/7Xd3st/8A2pcQWSKyhY4BxnHHLc89/Y1p6dZRLFFL58sodM8qB2HPWs414ym4rdA42W5rakLexUtBJJKp27Tv65BrIur8x38SFD5EkJDnOSOTUk1pK9zuNy/k7AojEY4985p0vkWdn9omDNHECSSOepp1FGUJKewbM5fWNGkmkaSOaNYSBk5xnn+dXrjR3g0+Fo512lPlO/OKs6X4h0/WhL9nglUxttIZeD7iusSzs7mJVmgiO6IquVHJ4NefHLqcqbUHuJvQ4PRdSj0id/m3nG1pAAdnPbPGa6nT5bSWZpQk4MmGWZ1KkGn6x4c06extwLZYPnV3EY4f1VvUGroEUbqMgFD0HQV3YTDyoQ5GyG+xIFJiyTuVixxjG1qpzkLID6jrViSYLcKc/u2Gce/Sqk2Nwwc8kD6A4FdEthoY0mDUTsDRLUAPymoKA9etFQGQg0UDIE0577Up/IvUE0UZjkiVshW4xnNbenRXcEJivwoaMbMh927Hf9f0rmm+KnggO7pq6AknOLeQbgf+A9aqzfFDwlJI7DXky3U/Z5f/AIms6WGp0pOUd2Q22ddO4QnA4zUsdtDfaYYpkDxuzIwNcM3xK8IlNp1xG5znyJf/AImus8N69put6E91plz9phWdo2cIy4bAOOQOxFaqN9GNlmLSLPS7dDaRBIo8Aj2HvWi6K9soXkfeBBwQexBpFlG0Aq2D7dah81bPKkE2x4PHMef6fyq7JEk2oXYazQp0bs/VT6Gs+KQv8xwzscbSegp7xMEkwzMrHIPIx/jVdhIyqhJKJ905xmqBIke4jedVGRsbcc8YA7e1QLceZgDsc0z7I+TzndyfelFs8ZyBxUSuUh8pyKr5+U1M6kjFReXgYNRYZVY80VKY1zRTsO58oUUUVRIV9C/BL/kn15/2EX/9FpRRTQmenj/VR0xv9XJ/umiimySC3/5BkP8AuVW/hFFFJbIpEvf8Kd/yzoopjKb/AHqY3U0UVIFZutFFFAH/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In both images a plant is sprouting out of a vase.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

