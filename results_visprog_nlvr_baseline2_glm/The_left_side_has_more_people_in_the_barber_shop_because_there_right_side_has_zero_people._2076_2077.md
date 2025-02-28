Question: The left side has more people in the barber shop because there right side has zero people.

Reference Answer: False

Left image URL: https://s3-media4.fl.yelpcdn.com/bphoto/gEu2KtaHm6rqXTK8JnbpmQ/o.jpg

Right image URL: https://i.pinimg.com/736x/aa/84/9b/aa849bbee61b30ab0ee118361e1e7e4b--vintage-barber-hair-salons.jpg

Original program:

```
The given statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left side has more people in the barber shop because there right side has zero people.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA+AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDwWzQS3sEZGQ0igj8a7y38O27MP9GiP1QVw2nsV1K1ZV3ESqQvrzXqMHiLTrHUXstShns5EI5kTcMHoeOR+VJlJCQ+ErNxk2UP4oKbN4Rtoz8tjCykdNgyK9B0iTTtRhDWV3b3A/6ZuCfy61Y1WGGwsmnaNn+YKqLjLMeg5IA+pNK40jxa/wDDogJWC1jznOGXJrBuLDy2bciKR6gDNe0tp8d5bfamtCpeN02SYOw9M5BwSOx6VxOraFtYjygzHgNzn9KEwaPPJIlUE8fgKv8Ah5nWe78t2RzbEAoSDyyjtVzUdKlgR9yhQoOflxjFVPDjmO7uHHVYdwyM9HQ1SJZ6TouhXC28n22Z3DhTGRK2e/r07VPLYyW17b20aNJDIMvIzHcp56HNZ0GpXkV8usXEhkju5SGVlPK/xPtHCgYxuxito6vFBGVlQqZZGCyPkmIgZ2L2Pb86BDGtSGYSyEp3YcMPxyAaaNNjeWMJPMhdgoYysE59flPH41uLYWUGl3Nwlx+/MvEf3t3QHPf1xUGoyxxXRt0R5EVtvmbOM+vXpzwfrQBQtNOm0e5vrF70zNHOCzW9y0iAmNDgHPvRUejrH5M5j4Uy+mP4FooA8h8P/wDIx6Z/19Rf+hCu28U+Hrm/8S30tqEJVwpjAbcflByMAj9a4rw//wAjHpn/AF9Rf+hCvZ4720s/Fty9xfJbhbtWdWl2hlMKjkd+fX8KmRcXocNpnhi+h8Q6OmoWdzbW9xdxxbyR83OSM9ema9g1rwbr1wzpZ6yp06KDcsE8Ykd3XOMcZXjvk57Yri7nxhp1/eaLNdzqzWWpNLMII2AMYBCEE+vFeraT4rsrtr65MuyK32mRMcxjA6+uc5zU6bMpX3RkXGj6jovhg3MsC3ZhtxIyw4Vyx6jb0HUcjt1rlblWurFJ5LbyJiCSgO8KRzjcOO4r0tvE+kancSadDcea7xPlVjYg8dAcdawLmwe18KaittOYknhy5lG7YTgbvbHXp2FHoN/3tzwLVL7Vbixe5lEKQsWQkBQT1HHOayPDjBbydjjAiHXp/rErt/FOnweG9mnSXVrd25tZRHdRnlmbnlOx6DP4+1cHob7Li4wU3GE7QzhdxDKcZJHpWmhgr9T2bRfEel6fqDaXexWL6VcWTSXFygZljcHhCegGOfxFULgeG7Rkm0rUjqWZJRJDIwbyvlJUgHA/HPNcpo2qywa+kt0bNbORlWfzEimCqOrKpb71Ok1IzTPaTXEH9nI7+XHGkKBl3EgkA9f5UDNHXdXvDptm+nySWwmi8+fY2DnJUZPf7pwO2avjxddX8sY1OKFLYQr9mkCbQcNg5Prx0qta65pkGmy2GYWjkdX3My5XbnAB3cDk/nTG1LR2VVd1dFztVnUhc9cDdxQA7wGS2kXjet45/wDHUoq3o+paVFDcBLm1tlM2Qkk8ak/KoyBu6cfpRQB5JYKzahbqrMrGVcMoyRz1AroLu5K63LPd3sxuoiCryw/MxAGMjJArm4JnguI5o/vowZeM8ir73huro3NxhpmOS2cc/hSGjWsWSaFUWSIME5DOAT9PU9a9W8A+M9Bto5V1a6sbVltY4Hd5N3n7c9R7dPxrh/CWnDxBI/mzyrudS20I3AIAzkcE9sehrR+LOnW+j+J9Pv7W2hSCSIbo40CqXifByB3I25pWuyk2lY9J8T/EbQ9O0q2n0Ge11CTzwrW9s3OwqecAdjitPWtRi1DwleATWsS3FruE1yxWLaQCGYjkV85aRqlxbXxltdiSzFlwwyBk5wMfSrt74j1TWdCgsHlRLCzGPKLAOzEk8jOWAyQPSmIsePdL1C3vY55bi3vbZbdCJ7cFUweg5JOTXB1u6tLJcjzri4WWURImc+gwBjHYAVhUxMKKKKBBRRRQAUUUUAOjcxyK6nBUgirMc91IxCl35ycDNVVOGB9DVlLryzxn6DigaOy8NXVxb+I9FtIrmRbdpoZbmJMKpbOcHgc8Diuw+LzQXNjZP5qJKtwzBScM6svOB3wVH5ivLbTVYImE0nnC8Rg8UqKCFI6ZBPNO1vxLeeILyK4v3yYkCIEUKAO/60h3H6ZiK7Dnb3CMT91sfewOc1UWMRuoSVD0yM9feqoulViVDDNMaYEdDQBauZVdeucLjgVnU8uOnNMpksKKKKACiiigAooooA//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left side has more people in the barber shop because there right side has zero people.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

