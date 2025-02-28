Question: Every single dog is standing; none are sitting.

Reference Answer: False

Left image URL: http://2.bp.blogspot.com/_Kf5oZYrnlw8/SmPEVaerLwI/AAAAAAAABFA/vdJAyrppiDc/s320/chow5

Right image URL: https://i.ytimg.com/vi/L3u1Up3sGM0/hqdefault.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Every single dog is standing; none are sitting.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAyAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDkrCxlTBML4/3a6K1lW3ADLz6VuPYL9kzwCCPx9qoS6a0eoRebKscAjLSgj7uBk5xz06V8tUo8798+l+uO1omhqXie6l8Pw6dDDCkcTHzZJMndzlR04x9a4jUEvpMhjBg91U13Vxosr6JOysfKkQFCwIz3HBwfzrHttL/tNPMkYpmNWIUdaFTas1rbT7hUq1NaNWv2KtmJLywtbIbS/lqsZPGGA/rUd5Ibe/2RBgZY0DfNkO/TIx2zxV6K2jjaLY+WgYpIDxkDofrjP5Vg3upfY4yyLH52DtlI+ZB7V9BD4UeNUd5ux0TmKeULPHI8Y/dSgnJfH+Oa64+H9Mv9H8tbYW84GY3UcqfQ+1cHo+ot/ZwuEQyTHkY5JPrW1pWr6qk7m+aJYSvyqHyQah1OVkcrkiCTRbzTkb7VCdrkBWU5FLCG2ruIyM811tvey6gBbPb77V1AMgIOD9O1cbqEVxFfz2rFoo4nK46M/vnsKqMubUiV1oyGa782MRw4LpwzEcIf61Xt7RYUABZmPUt1qdIwuERQAPSrCJk5zx61oRcjWEY4Aoq4sWV7fjRTFcSS/edgsRG2Jgx5+8R6VHqOuSS6jYu0AMRk23PPzKoHb171SgASRlzxjpUcs4cpDtPmE/KeuRXjRledpK56rjaN4s6OXWpNRsLe0hSSNp28sCUYYp/ePp3/AAqUz21jJLEqlmwFUL0GPesnTZHs0uZNmZhthjPUqzZJP5D9a7Xw/wCGVkiWa55J557VTi5fCZqSj8R5jdzuIbuNhhkmL7h1zkcfqa5LWZAYDtO0qMFfX3Feg+LLdYtb1G0tl/drK7uf9rAI/LpXnGrDCl+gA5zXp09kmckmm20bXhrUjBp0Sjk7QMetbYnttn2qe7mhgyA3yAgEkDtXCaDcOPkHODla7K28u5IMsip/eDHaGx61lOHvajUtND0PSMafqIRLgvG6BgGTGAaz/FLhtcYrgfu1OaXSLwTrGse1sYyc5/WqGolp9UuXc9JCOvYcCrpKxnN3ZWQbjnPHtVhFGc4+WmxpuHHK4qzGjM6jBVc/exWxBNFD5kYPls3uAKK3IvD0TRhl1ONMjJUggg+9FXYRyQ0aCJfM8+RnPX5ev61TmtjJdQzLBLGYmO0sB0Prz1yARWZH8X/DAXD+GLjPqsqD+lPHxi8ND/mXb7/wIT/CvM+rVL3sd3t4WaNu1juUv4bmZY5QjchV2kj8+favWtI1TTp7VPLuowwXmN/lYfUGvC/+FyeGh08OXwP/AF8p/hS/8Ls0hZAU0O8AxjBnQ/0q40qsOhnOcJ9S74znjj8SatK8gWP7S/Oeorg7uCfUyCiNHAfUcn/CuhlZfENydZcFI7gmWOE4+QHt6Z96nMCjCqorrV7GFzjE026tplltyS445710N3JNeaYsUUDrNkZLLjOK1VtYy3QZq3BaqrZx34pNXdxp2VifQLmWHTPLZJEm2AAsBgHvV1F5GRkdyTnNQxoCrKM45U4qyGIUnHQcU1FITdyRdobaB1GcDoKljXcdowPqcVCD0JA/AVcgWO5Aj+YEMTlEySPzqyBxOT95s9+R/jRWrHp+yNf30PIz88QBoqrMD5OoooqgCjvRRQB63oH/ACL+n/8AXBa0xRRWTKLCAb+n8I/rVpAMUUUgGWzHa3J71YiYlyMnHpRRTEyy3Rvoau6eqmCUkAkRE8iiiqQiHzZP+ej/AJ0UUUwP/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Every single dog is standing; none are sitting.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

