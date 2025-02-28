Question: Each image shows a corgi dog in a sitting pose, and the dog on the right has an open mouth while the dog on the left does not.

Reference Answer: False

Left image URL: https://cdn.wallpapersafari.com/11/38/GvKLPC.jpg

Right image URL: https://i.pinimg.com/736x/4d/eb/c7/4debc7a8ac1bf7f27b324511127bd318--pembroke-welsh-corgi-dog-training.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image shows a corgi dog in a sitting pose, and the dog on the right has an open mouth while the dog on the left does not.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA3AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+sXxVqFxpnh25uLRgtxlUjYjOCzAZ/WtqsnxNZm+8PXkKjLBN6/VTu/pUyvyuxULcyuchoPi2+sZ/s+qzNcwn+Mj509+PvD9a9CiljniSWJw8bgMrKcgivD/ABHPJpy213byF2LKHjA6j+8PStfwr4vv4Q9vAUmUnd5cvCoT/dx0rBVeRqLOqVDnXMj1yiuc/wCEpMUdt59m2+VSWEbfdwcdxUV744srV0iS1uJZXHyDhQfxzWrqwW7MFRm9kdRRXBXHifV7sYieG0U/8813t+bcfpXReFbu9vdH829k8xxKyq5ABZR34980Kom7BKk4xuzbooqC+ne2sLieNA8kcTOqn+IgEgVo3YyWpPRXFaV8Qra58Ivqt1Cy3cSkNbop/eMOmz2P6c1teEdYuNe8MWepXUcccs4YkR524DEDGfpWcKsJu0Wazozgm5LyNuiiitDIKRlDKVPQjBpaCcAn0oA8M8a2dzZ6y2jQR5jCb1lxj5Dzg1ytlaa2/iO1Wzu41tVkUSwNkDAPJIxz9c12mvar/aHiO6eTIw+1foO1YU2rM1hqNxpylL21LRbSR8p6hvx/pXHCCcnJHfKT5VFno3iiS8h8OPd6dbme5hj2BM43Z78VytqLzVPDsUuq24gusFiVUqFIPB9sjqKy/hPrfiLVby9g1maSWwFuQxnbOHzxj04zntXpAWy1XRzFbNi3dTtZRg/UVdeHNsTRny7mXoukC+RYbdfLLAFmznYvrn+VeiWttFZ2sdvCu2ONdqiq2j29tb6dElsiqNoDY6k471frWnGyu9znqz5nboFI2Np3YxjnNLVPVryLT9JurqcExRRMzAd+OlXJ2TbM0rux4be6JfeU8FvZXLrezNKjQzjZGqn5VUejZP0217B4MkVvCWnxgIHhj8l1U/dZTg59+M/jXN6NNYLo0LW9yrQxA5LYBQnkg/StX4fyQS6RfNatvt/t0nlvnO8YXn881x0IKMotdUdlebnFp9GdbRRRXacQVHO2y3kbBOFJwPpUlVdRm8jTLqX+5Ex/ShjW541qsEc3mXVt8wZiT7GuO1PTor4yXSRXBmZfLuEt2Id19QO5Bx9a7e2hZLz1hnHzr2z61JbaOsV8ZDHuQHNccG9zulZMxfA3hDFozrLqdtZSN+8ScmNph6YPIX1xjOa9PjtlFt5URCqOFAHAqskjSxgIo2rx1rStIiBljzWr97QyctblvTme31PyNxMUsQKj0K1uVz9j+914c4EUZx7np/WugrSnsY1N0Z2sa9pXh+2S41fULeyhkfy1ed9oLYJwPfANctrPjfwPrWk3GnyeL7GBJ02M8U67gPxBrk/2kP8AkStL/wCwiP8A0W9fM2T61TSasyE2ndH0rJqPh2JEgs/GXh5IFG1y0hBlHbOOhxxnJrqvD/jbwfo+mi1k8V6MRuLLHDIqpGD2Hc89zXyBk+tGT61MYRi7oqVSUlZn2p/wsvwV/wBDPpf/AIECivivJ9aKsg+/6r30IuLCeFujxkfpRRQNbnk01rJbSMiHKhvlyfumtqKFT8x3cj1oorBJJux0t33NK1swTlZZVH1q5axGEtI8kjAc/M2f0ooprchlrQR5txLcH+Ikit+iirp/CiKvxHjP7SH/ACJWl/8AYRH/AKLevmaiirMwooooAKKKKAP/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image shows a corgi dog in a sitting pose, and the dog on the right has an open mouth while the dog on the left does not.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

