Question: Is he near a shark?

Reference Answer: no

Image path: ./sampled_GQA/330186.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='shark')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='person')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is he near a shark?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABDAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDCSxiH/LRP++s08WUY5Eyn6P0H50LbOHIbI5546VJ5DJnI5PXAr1+Y+Y5PIQW8GceYGPf5jTTbQL1mXn1WpFgYsWcfTIpwtXKliB9O596XMHs79CuY4Sdu4YA7rUkNtFLMqRncTwAI+ak+y/Lyo55yBWto9oDKSQWCYIBHU9ue1JzaQ6dHmlZlK/0tbS1hdywZif3YXkfWqIji/uueO1ehW+jQ3kSh4x5ZwuwDPFVp/CGya4Yxt5Q5UA9fb6CslWtudc8C27xPP/3IJyje3zc00Mg4MS/8CPNaepWZFyQkPlbQFOepI7/WqRsiMZGa2Um0efOlKMrFfcBwI4xn0GaY0nzYCoP+A1bFk3dTmkFi+3uB6U7sn2cii0rFjwv/AHyKKu/2ee4FFGoezkdAlkAPur04y1T/AGJAwIAHHI3ciqceoRsHbZ0PC5xkVKupwhCFhbcccbs59ax50emuQtR2KdAinPNSrbRfKRtwRjGP0qkmqIjki3PXpv6/pTxq5PCWqj2LE1LmilKBcNpGG/gz24rS0ywR5WRCG3Kc7ex6j+VZMGpI+RINpAyG7A/nXQafqekWarO105dgAy+XwrfXvUSqKxtS5G7nR6LYrFbCQodzA7S3p9KuXKxW0Ek1wVSCOMl3Y4CqOuT2FZ8Gtf2hF5lgROqkbkA2MPQZPFcp8VPENzF4RfSLa2nNxfDbMBGxCxg8gkdCxx+Ga57tvQ7042OUh8TWWv8Ai250uztWCqrPFKD/AKwA+h9uRjPHatq60mS0RWlQqp/SvHNIstSbxjpcd3LLZlL5B++JjeMj5u/PQYya+hdaWK4sXv5nuCki4iKElXPUBj/Dz/KtYVmlqc9bDwd2jkTAnYZPfI4prIiLkoOPesqUTROVkMgkxkgtn9ahdmyQxOfc1t7U8tyS6GsFjcbhtP8AwIUVjkZ64op+18ieddiXAJG08eh4qUD5TjAx1OaVY+4BJqQRYB4xmsbMvlIhxj+dPBPGQcDvUgj470oTnvSsHKMJY5JOfenryQQTkc8iniPI6D8RUiQtjjI+lKxSidJ4c8QvpUQhIWWEuSfm5GfStPVPF9hehoZ7NvKC8NkbgemRXJQ2xZcMqkdB2IpJ7SdYdqsgjPQbTk/nWbXU7YVJqNjD1JbWac7082MNhA5Dj8N2cV1F14oWHwvbWNrYeVGIhE4dhIrYHUY6HPOTXLNZH7UqvjG7nvWtcaZ5sI228CAHO9Mgn/GqV3ZMhTnqYckxmlMhyM9s9KUZIBHTp9Ksf2fImRswCeakS0kQFcfL7Vtyo5HF3KmyirItnXg0UrE8hpC3Xb1yKlSBMcChTtGSN2TxgVLuzn5AB25qzqSQ0Qp2BHuKXyV9PzpwDZyyLt7cYNSdQegH1zSHZDBEvGQBnpT1RByF5HfHSm8YBGB6HHSlCjjKnnvtpNDSLibVAJ788DNOknQqSzDnsy9T+VVQ6YIZlGDwShpDvQbQM8ddv8s0uVF8xSktVLHeuDnkHirXzGLauwL22jH65puOf646U07c/MefyNNRRFwZCvA28enNRMDjsD71MSSMDkeuahO49GxjjnmqJZGUYn7yUUrB88YYetFBNhY2Jxk1Yydjc/lRRTRaAkqBhm/Op2RdgOO3rRRQAJGpcHH606QY4HTBoooGMk+RRt45pLmRljQjaDtzwoooqWD2IQxBIHQgE8UjOxiJOM59KKKOhIjcooIGKikJUnBIxRRQJjSobBIycUUUVViT/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is he near a shark?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: no

