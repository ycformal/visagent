Question: The sink in the image on the right is not mounted onto a counter.

Reference Answer: False

Left image URL: https://media-cdn.tripadvisor.com/media/photo-s/0b/f1/49/08/wash-basin-is-outside.jpg

Right image URL: https://media-cdn.tripadvisor.com/media/photo-s/07/e0/54/1f/the-grand-jbr-hotel.jpg

Program:

```
ANSWER0=VQA(image=RIGHT,question='Is the sink mounted onto a counter?')
ANSWER1=EVAL(expr='not {ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkADgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwC0g6VMBxioQ2Oe1SxSButTYgbcZFtJ9KxJu9dFPCskJQOgZuBk9a527UxSMjcEHBFSBLYjmVsf3RU54qS2EUiM9vGyIx4Rm3HjjrSSo0YBZSAe9DWpNylOaKSc8Gilyhc0/wCE59PWo5ZTHbOw69KsRmEtKrqxwccN2xVa9eEQSIsZXacZ3ZzkVtyiuVYxK0jM8hAQZBz1qpcytLLuZiWJ5NOBzCu85ZW4Ofaqzt+8H1olqEdhPtdwpWGFyAD0B9c1etZZfs3lySBirEYz6cVkIStyrDJ4Bz25rWgltkjdvk3O5YnHPfFSkhNjJn4oqC7mHzsPu4zxRRYRpknJbzXBI5IPWqhyyD53ck/xHNPMgA+tM3rEDIeh64rQY2cFVVv4WOPqRmqbE7ifQGlnuN7KR90HNLYKLq8WM8560ktQ6EcKYGSdp/OrHmAIAOBTb6IW926Qn5CNwQjG3Pas651CG1CiYsmemVJH51NrBZj7+bEDc8niis+8n82ESRfOgySV5FFMaRo3WuWEAINyhI/und/KsybxPAUxFFJIfU/KK5Xfk5447U5cn6UnJmigkdnaR6xfx8WJhVhlGdgBjseea3tJ0S+gvIp7mWP5QcohJHI75rn/AAl4lFnIlhqJ/wBHJAimY/6s9g3qv8vpXpUOw/IoJJPKheKE9QcUZ0+mwXDBZcCWRjsZRzgDv61zUsEEm+NgskZJHI4Nd1JYvLGyqwVtpVWPJXPWuL1nSrnQ4lJJlgzgSgcD2PpVya3M0mc5Poc9rMZtJnaJz1hY5Vv8+9Fa1j9o1AlbeF2dRkleg/GiouikpHBbV3YVTk9vStfSNIS/1C3tmlWLzDgyv8wX8Ko3V9bPeFrcYU8/KuMmrOl3hTUrfcdiFsYPvS5fesVf3bnqVh4C0az5mikvJO5mOF/75H9a6aO32RrFEgRFACqgwAKzPC+rpeQm1uDmaIcE/wAS+v4V0THDEAYrZpR0M0+bUz54Xt9rA0kssMlpL5yK6BCXQjIYd6vOBKu01nSxNC2ecUaS3D4djnNP8TLa+Fb/AEzR9ID3AZgrMNgDn+Ik9cdlzRVvUoLh5IXsliUr8rRYwr57+xopclh+0PG7PT7eW0WUbjJkqxJ+63Xj8KruqH5gDjuegB9qs6FJvMtnxulw0ef747fiM1Q83bI6MTtYkEe9RLZNFRvzNM7Pw3rkn7uVHxcwEZ9x/wDXr1/Tr+LU7GO4i6EYI7qe4r5zsrp7ScTRgkIcNgdVPavR/C/iIafdI5ctazYEgHb0Ye4rVPnWu5m1yS02PR7u7gsIGuLmQRxL1Y1A+rWVxbM8MiT4wCEOcZ6ZpdW0621zSpLWViYpQCHQ9O4YVheHvCY0GScC4MqycY24GKnVMp6otK/mH/PFFbCW0McZVEAPr60VfOiFBnzKjskgZSQw5BHagksSSck8k0UVgdBcinZwM4w5wQOB1rQ0qRkklhBOxW4HpRRThuRPY9e8EXs9xpksMrblhYBM9QD2+ldM3BoorWe5lHYjJ5oooqDQ/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the sink mounted onto a counter?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="not ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="not True")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

