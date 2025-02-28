Question: The left and right image contains a total of three elk.

Reference Answer: True

Left image URL: https://i.pinimg.com/originals/8b/c2/ef/8bc2ef0fda1a3dd01fc87d5d25c51435.jpg

Right image URL: https://images.robertharding.com/preview/RF/RH_RF/HORIZONTAL/764-1484.jpg

Original program:

```
The statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left and right image contains a total of three elk.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA8AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0RtbC6tHaMmGaFnVM/ewQM1Neao0NrJKEMZjUvliNvHY+1c/4kMccsJvdNNzYhSRcw58yCT8Ox4H86oWj2VzfwtePLPGV2RW7ZI4G7JUfeGM+tS8ZFaNblxwkpLmT2OztdXjurWGcQyKJEVwCOmRmrS3cTeo+orPs3uLiISyWht1YAqkhG/p3A4H0zU+DxxWn1qBl7CRaaeLB57V5HJbOlw7QZ+YHqeM16g2dp45xXlUM0bSEiUgryQx615mY1VU5bef6Hbg4OF7h9iuSxP2g8g4C0w6dcRgOHwQRk56/54q2JWEvGOmdxPSmtqKqpQLuP3mA6D3rzG0jsdkRRW12kmRKxAPAJ6/WplS5kkLlwHHY9M1AmoRzNmJyW25xjgcZqVrsGAMzgA4JI9+31pOVlcXMraFtGk3YkGPXHpT3VEhLEd6qxXA5jf5znOT6U55kwqtyp5JzxQpXKTTHt5ROTiioGvI0O0qMds+lFO4z09ULHHBJ7etcPrOpWXhfVLLXnt5ZbNleAlBgx+YVwxB9MEYrsC7xl2U5ZRwK8a8cz6pql5PJEJhpwKrKD93eOfwPA/Ku5NOokzCmn7N2PbbO8ttQs0ubSdZoJFDK6HIP+fSpBggZ/OvDPCl48KyRJDI5xuJhmMUg7cfwt9DXa6V4iubae2tYZZ76AIfN89v3iDOPzB9etXJ2dhewbV0d6y7g4zjjj8q8JdiLW4kjOX3fKucAYNe4JJviLrllK5BBrx2LT5WhCMDnc27jrzWdSS0bJpRvcrG9mhiiML5O04J55HarV1DdNPCkVsBBJCj7sj58jOQfTnpSSacYoliRiWRw2SPU/wD166GKd10+0jZUllg3plxgbSOBx2Fc8uW2huo9Gcr82mTQR7WjlcghgM54xkVpXGjXN2sUcYSGFwXRVwy7vX69sHpiptcto7uaCWzztCbCHXBR+/6Dt61NpF9dWkctrvBCbXi3IGIkOMk+oxSa00eoKydmtChFpWpbTGspaWLO7cMb+4AFV2kuYZ3RonGwbTk5O70NdVDfylwbjy0Ow/vUTBDep9a54WE8wkMj7mcksfWs4wW7FKMb3iNM0jHKKoHcdeaKIILkR7QIwATjdwSO1FHKu47M9bdDNDhDtbqGHqK5nxJb2mo6beadpcnm3MzEyQghSrKM859OK6COY7uMge9LJaW4FxdQxolxcW/lu+OrD5QfyP8AKuzlT3Mac3HQ8S0G0eymnmuHCOyZA67een16VNo17crr1y0CySTXCC2iB7OxGCfYda7+bwPpE0C+W91FIw3ZE24Aj69qxfDejxaLrEcV5EDJGzSRSjOCT0OffIq9HqNVnax6FDD5NlHAGJ8qMJk98DrXm0bSrNjcMAZznqc816HJLiNweOoxnPavkaWWTzX+dvvH+I0o0Pb9bWMo1vZ9Nz3qQjKOpXAA3A+lWEKhd5bjbx7n2r5782T++35mjzZP+ejfma0/s/8AvfgP635Hv68biW+UAjFKHjWQtkFjgjHXivn/AM2T/no35mjzZP77fmaX9n/3vwD63/dPoLzA6MD/AL+T39qjM8aBgJFwV/LtXgPmyf8APRv++jSeY/8Afb86f9nv+b8A+t+R7jNMpf78eMcZ9KK8O8x/77fnRR/Z/wDe/AX1vyPrt28vDN3IGPXsacGdwFDZQc7fQ9/xpXUNH5ZztWQAfzqGBiHIz1c59+aw2YR0YSrI0oReNjbh2yKpz2iEJLubIYADsBnqPrxWgx+Yt3Crj88VXUblwST8innselUtBbDZVzCW3cbip56/5zXybJ/rW+pr6tErS2ILYy5OSB7f/Wr5Sk/1jfU11YP7RjU6DaKKK7TIKKKKACiiigAooooA/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left and right image contains a total of three elk.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

