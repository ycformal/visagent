Question: An image features a light blue cabinet with an arched top, feet, and a non-distressed finish.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/3d/ff/ae/3dffaeddcb71325e3cf7b7980e6cb103--painted-hutch-painted-furniture.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/474x/97/3b/45/973b455aae89fc4970bc10c7abfee104.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image features a light blue cabinet with an arched top, feet, and a non-distressed finish.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABYAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDOisg11Acdj/SvRNEtQqKMdq422cR6hACATgH5uQcgV6NaW8gjAyE/3ExTgroU5WNGMQwrmR1Wnf2nZKcBmb6Cqj2sKOA8c0rkZ5Ut/LikJRRgQSj/ALZEVfKRzs047+yk/jK/7wqfETrlWVh6g5rnJZY1yTHIMd9hqnJcMvzRtIp9dpo5Q5+517Rp5LAd68S8d+Vb/Euaact9ni0hJJAuc4DH/Gu+sdXuFvPLmmeTcp2oePxrz7x3Is3ju9EnAbQ+/b5qznpoaLWLZS0TVdN1m8kgsraUGIK7SSjqCwHHJ9a7FPDsssG+NZHcgHC4wK5TwbbaPCZFsbyC4u3jQyiNSNgDjueozivV9P8AF/hi0tVR9YtlcKFZTuyDjGOnrQloZW1OHu/D91bWsssw2gA4BH9a4vU9asdO1KeyubKZjE2PNTBzwD7HvXrmoeJ9J1rT7q1tbqGSRCSoB+ZgD6fnXluvRaQdVvBPeQJcCQgq+c5446dKTQJa6nGeIoPL125QDCgjAz0GBRXSa5Daf25eb49zeZyfwFFYvc6o/CjYuZjDe2jDjKr0+n/1q3/GOgXN3eXV5byTqysvCk7WG3Jxjv3x3Fc3q42R2kgGCET+Zr13Tde0lri7sZ7iJbiYIwhk43jZ2J4P0rpp7GM9ypq9sLbw6LWJWVYoUUBScgBq49dMa9iDQ3yc9RvOQfTrXe+I9RhsoLi5dJCiooKp975jt/rXK2Wo29sreX+6BcMFEBHHfPuap8zehCSKehWaxamxW5M6+RICwY4zwO/1qprmiXlxfXF4kUxgyMuCdo4FdLb3ekz3jpYwyxSCJ8LswpGASfrxWbr3iaxg0u+0R/OS5dv9ZtJXnB7e1NXS1E0r6EelI0Gtafb5O1bIt191rl/GpJ+Jk6c4fQXA9zhq62wKy+J7dlB2/wBngjIx1YVzvji2jTxzFctKC0umSRbNv3QEc5z7/wBKzl8RaXuGZ4GsZ7XUZmltpot8agNJGVB+de5rprLSI5ZZsxM2WLZVC2efaub8G200VyJmaYqUXG8kj7y+tXV0oXF7N5d3Io81t+J2VUyT15wKfQSV5WRvwWsPmsRbNG8asu4xkDOPXFUNb0u0mh+2LC8ly9yQVC5AHr0pul2iQ6gWW7llxG4AaV2U9ASM9axvE2lXlhq4uvt12UuZ1k8tHIjQM+Ap568H8KUtg5WpNMytbjL65fEHGJiDRS6vKp1q+JHWd/5mismjaOxe11sWFu/Iwg/RjXR21pb6p4gtIpiMPCCeeuAvv/SuY8QOf7Hjxnow+mCKuQa1PpuoW1xDHvZ7VUB3kYBUZ4x+taUnoRUWp6BqAVmfTwCE2hQQfu45H4ZFb1jb2ItERoFL4G/zRnP4155c61dXFg1+kKy3DJxHgsGwQPx4p0Go61qNs5cm2FwmCqlsryTkZH3ue9XOXKRFXO2m02PT4dQnZF8zzCsJ/uxkDH58/lXPa/ptq9/aSAZkuIWkcZ6ENtB/H+lOOoaibCO2uXjNvBEEBw298AAFiTyf8a5q58YXdlqt/pohDQPKvziQhsAdPTHJrSEk1ciS1sdPaRhfFYUfw6fGPzc/4Vz3iyGGT4lQxS5dv7PBEY7g7gc/UGt7SJTN4ld24P2SAEfUsa57xqwT4t25HA/s1R+rVlJe8zT7Bft4I7OFTFbRxquFGx845HH5gVK+h2shlc2IzJy4EpAbnPI3Y61B5zCGIFg2cY46Dj9a0hNMEPzRk8dQRVpGKlJO6ZTt9LgsF86K2kUIjKMyZ2gnnAJpt7pttdPJPdRXLnzElYGY4BU5XAzwB6VcklmNuQ/lbTj7ufUVHJK32ZsMA+Tgj3zQ0HNJu7Z5F4j1ZrTxDexRIkw8wsWIKkE84/Wis/xJAbjxJqEiNj98Qee4wKKyaOlPQ7PXSDpJ9mcAf5+lTaRp8WsTWIuLh4IPsseWVM7j6E1m63Ox0yUYyBJkrn2NaFjfsLaNI7eBUCgKuDgDApUdhVXY6Z5bXT7wJBI8lvDxuKYJ6Z4HvWlHqkEVrDeltxRmAjOehwMkYz+Fcm1+8al/IhJA7MRn8af9vkwT9jjI9fNPP6VpKHMZqTRvz6nJc6bcCadHZmVo1WMqVHOR0HtXJ6lZNJctexrKTks4fGDj+7jkk1b+2uXC/ZolBBJy7H0+nrUjXco6xQj8/wDGmlbRCcru7NbS9UW21C9uypIihh+XOM4UnH61i634g02/19tRu2t7W7ECRR75jkAE9vQ5rL1bUnjtbkIiRs2FYoCNwzjnmuD8Wur6rCVQL/o6AgdOpqHL3jVL3D1iHXtIIy+p6bxyP9MI5+hFD+KNODY+32Y+XBaO8VgfwbFeEUU+ZkciPcX8W2jtsFxamLuzXkYY9+B0pJvFtivCz2zDqT9qj4/CvD6KOZhyI9Fv49GuNQuJhfwESSFgftA7mivOqKVyrHo2pux0yXcrAnB5BH+etLp91m1iGf4B/IV0vxT8TvrN+1pE3+hW8eYh/fY9WP5ce1ecx6tb2rLHkhdo525HSphpcc9Trll22+3ez4U/Mx5NWt5dVxIy7Wz8vfnofauSTxBZkbGlIB4yIjxV+HX7GRSRcxrj++pWtLozszoPO/egfX+YpHkKmRvMZt2PlJ4H0rnm8R2G7cJmJHHER/Oo5fEtmFyruxz0EXP60XQcrLmrF2gkkxlPMUZrkfEj79SQ/wDTFR/OtnUdZthZNCokLnZIBgY9eeetc9rMqzXaSKcqYlwfzrN7mq+Ez6KKKYgooooAKKKKAOx8T3jy6iI1OFaIbj+J4rFS3jbGeeMCiisJtmsEiZLOAnJBqwtlb7fumiiueUpdzdRQfZIB0SoZLOIZIFFFCk+4OKK10pdixGTwOPYVmS/fx2HSiiuum2znmrDKKKK0MwooooAKKKKAP//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image features a light blue cabinet with an arched top, feet, and a non-distressed finish.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

