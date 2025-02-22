Question: There are a total of 1 pelican that has black markings.

Reference Answer: False

Left image URL: https://c1.staticflickr.com/4/3323/3411279617_3d722de017_b.jpg

Right image URL: https://maltpadaderson.files.wordpress.com/2015/11/pelican-hasting-harbour-15-nov-2015.jpg

Original program:

```
The statement is False.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA8AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDVj+0ws8clsLcoxUJkPx2OapX9k92p2gBj1IGK2FtlHTP508W49TW1znaOHm8PXmcxMM9iTTYvD9yoJnUu3YK2Bmu6+zrTGgWgLs4GXR9TLHCqE/3qhVDiu+eJQD9K4FblM1zYjodFB7imNjTRAT2qYXCVPbsLieOGPG92Cj6muY6LorLAaVocDpXqlj4L0uK0X7SrTykZL7iB+AFcX4o0200yV2tJwyKwVoyclcjIq3SklclTTdjnNlHlg9qga6GaT7UM9aixV0T+SPSimC6XHWinYND1n7MB3NVpxJGpKKCR0zWjmmMqsrFmVVHUk123scdr7HPNfXpJCWobHHGTWZea5qFtkPaKh9GBFXJtXmGoGGCVlijkyGQZyvuO1WPENs14qvKpGE+UnuKiNXmdkaSpcsbnNT+Ir5kGI0Td04rjy7DnJroJrZFYj5hjtWACCKzrvYVNAsznua3PDMMF7rUUF45EDK+7kj+E+nNYaqM1qaUWh1G2lQ8rKv8AOsYtXRpY9bs766t/DgZZGxBHsUSjLNtGBuPXNebyJbrZapdMj+Zet5pZyTlwcZBPUfSvStSx/ZNxyctnnNea+KboG4S3TASNQigdgAK7JNKLE4qxzb5B61EXNSMcmmsBiuOwxnmkd6KYVGaKeoHuM10FhLRMrsemDmud1PWJmh8pfldiTkngD/Cuv1i3Emmv5AWKTIy6KAQM81ytzocUisVzuZtzZOc//W9q0rqXQqjKK3E8PtbpEqsQd3zE98+p9a3ruRLtvsrDjZuVge9YllpfkyBs9K2EtpEeJozyGAYEZyueazpKSNJuLVmcpdaefNJLHoeK4Erg19DPb2/lNH5UW3B4wOteCmynJ4ibqegrTE9DmplRRzWnpTB9StI/WZB+oqoLK4PIicg+grU0O1ddfsEZCG89OMe9c0b3Rep6lqWP7LPvk/zryfW2MlwJv7zN/OvUNfkaDRJXw3yQM3T3A/rXlWplhDDuBzluo+ld1bSDYm9kZMkhBqJpmNThN/UUGEDtXHzhcrecaKc0Yz0oo5wufRzJG0bRuc7gRzXJ3l99gvvskykuw3JtGdy+oFadwzlsmRsjgHNc7e6XHLr0Vy805khiYp8/AzgHtXZU1FT3NOO+iyS25QOSWQjH51tWQMoSVVyh5BPQ1kpbLe27W9w8jxyoUcFzyD1rYiP2eC3gj4SNNij2HAqYR1HN6FzYmx9yfwnkE46V8ePLJvb526+pr67DshkQE7cMMfhXyE/32+tayM0L5sn99vzpRPKpBEjgjphjUdFSUTG7uGGDPKR6FzTDNIesjn/gRplFADvMf++350eY/wDfb86bRRYB3mP/AH2/Oim0UWA//9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

