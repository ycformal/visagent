Question: the left image is not in glassware

Reference Answer: True

Left image URL: http://cdn.wonderfuldiy.com/wp-content/uploads/2016/04/Strawberry-tiramisu-angel-food-cake.jpg

Right image URL: http://cdn.sheknows.com/articles/2014/06/Carlos_k/dinner/texas/Food/Trifle.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is the image in glassware?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is the image in glassware?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD//gAMQXBwbGVNYXJrCv/bAEMACAYGBwYFCAcHBwkJCAoMFA0MCwsMGRITDxQdGh8eHRocHCAkLicgIiwjHBwoNyksMDE0NDQfJzk9ODI8LjM0Mv/bAEMBCQkJDAsMGA0NGDIhHCEyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMv/AABEIAGQARgMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/AMMfLzTwD9aWEBwKsCPBxiuGO53T2RlXseCHpsTgp0q3qEZMdVLZMxHjpVvYzW5I6/L0rJukYN7VvlQYxxWfcQ7h0rJPU26FWLgLUc2QzCrmzaq8VUvOHz2NC3FLYzp2KviinTopIbOc0VoiTp4JSjA+tbKxvKu5Y2PrhTxXcWmg6ZpCMmlaadRuYWKtdTkABu+0e3+TWc3iqwtZZbaSSWC+3EJEV2oT7EdfxpS5E9WaRpVZxbUdP66HN3Oh6i9hJciymEKcFyuMUy48OT6XojXV1cwRzsu5ISecep/wr0PWLu5u/B9z5zwC4mi/dqFwN3BHUjmvI/EOvXZs4be4itBcwjDnySWUccbs5GaKqtomThrzs1C7v8repsaboWrX9ojiyZNwzliAD7iqMmm3bXEkItpTJG21lC5waXwz4y1LS9GuY7hcrKwe0ZpM+WO4weq+nPFaWl6xo+r67GJRdRSXZUB2uVA3dDgAdM9O9ChqhTxEFzJ6PoZEukahH96xuAOmfLNZOrwSWyATQvG5GQHXHFe7yaVYNC3nqZolh2FHO7GOc/WvNdS0iG50wXmmXNzFbTOYZILg8bgewYHrx0pzhyO5dGPto6M81aUFQDRXd23hnRAVt9TExmC799t8pHPRhjk0Vokmr3MJtwlytHphurXRruDRXume6KFnaOPaoBPfrzWTdapoWjeK7O1k0y3uRPFvluCu51JPGM/Q5HvVTx08ui6xBqNvbPO0kHlYAPBBJzx9a46e+vbu/sr2/wBMaxIyibkKh1AyDzznk1hUk4XSW1vuPWw2FjWSqSlfmi+vXXoux2XxA1rS4LvS4IJBtlifPljOF4G72xXk2vRwwafHm9S5upd0hkhbcMdAh9PXNdRPqkVw8NutqL268wFBtyI2+vb3p+peC4NTuIMymzm8jMkaRhlznqDwfz5qnaT5jkp89D3JztHy+ZgnUYrnSbC4tH8u6ihERUjcCAMd+lZFjaagdVgjs4mnmZ1ZYwu85Bz09PUmvQfAPw+0qfVL2TUNQM1jFK8MdupKNuUgEs3pnPAr2nT/AA3pGmQFdLsreBCOfLXlvq3U1cKUr3voTisVhpwXLD3u5zej2esTosl2iIMZKryeatyy6SZIZ7yaCY2xJjLOPlbpn610sBaOYAoBERkHua5nXPB/hye7S4uNMjVlbOQ5VWHuq4zW01K2hw0JU1K9Rten/DnkHj7X7WbWN2mzJIvRiFyPzor0a48EeG/Naa10qzKOejIWA+mTxRXL9Ve7PY/tmnFKME7I7razxk52e4Fcrra6eb7dcIlxIpOF2KxU9M5Pf3rstSbyNOlf+PbgMOoryCXUrltUmSGzbywR8+evvXVVmktTw6cZX900HtrVblZ4YPKZckljn8cDgVSkmeSZpwpVFQgAjrUGpaktlatLcscnIjiUcuQOnvVaDUI72z85QU9RnODXNJ3N1FpXZRHiezi1O4trVZRdwvmXEeFY45JPr2969S8NeI0uLGMD953POCPwrxMxGHU7+52hftEgY4HpUuneM30i4ZIUQMWyrSZ28fT1pwqKLH7GVTSK1PpD7ZbyoSdpZegqpNFBrVuYypjlT7p7f/qrm/DniRdTjtTcWkls9wMhJHBIHY8etdUkaxyB0HzA/TcO9dPN2OZxadmcXrF1NpN2IXJVtozjv70VpeNIV862lABZ1OTj0opNyvuCSNzxLOsOjygnDPwteYRyuIWCJ5j8ngV6d4ljR9LYkZcH5a8tNzFH5yRFmVZCvCnGfSoq7mkFozkvGCSXJaSabyjbKTGIyT6dR0rl0juDIjWk10YQvzLu4Dn26YrpNWIuZ7ktKYiw8snjKAHr9Tml022WOyCQx8E8BvT1Nc17vQ7lNRp8rMe7uri3sI4Sd9wV5ODz6/hVeGHyjCdu63I5VuRnvXUppaZJI3MepNKuiSuSIlQLnOCP61fI7HOqlma3h2aS6nkuzLulZE8vb/CU449sYr1yxvJr3Q2k/wBTchScHnDCvN9C0VYpIWyY2ByyA8fUV6TbRI9vskGQRg49KqEZJu5FWpGTRi+LZJJIbIiJiNuQVHqKK2dW+xDS7Y3AbaCFQBvaitncxNW6gaaxlRPvumBmvHtTYW80ymHYFYjJ6H3r07SfFNhqluWWVY5F6xvwfrg1yepeFrPUdWml/tPzC+XS3xgLjr+NKceZLlLs4NqSseZCxjlupJthbe2ee/vWxa2ErAAIQK7keG9PsIjJLLGoUZ+ZhzVi2sbOSASxujIRkHOKqFCxEq1zlrbSuhYZrXg04AD5av3d7pWmpuuLmJB9c0HW9LigExnGwjggVryxRF5S2RNa2OCMLzWl50lrE0Y+8RyDwRnvXBX3xPtLW9SGytXuEz88mM4H5/1rJ1j4gapfySNp8AiZowhkdduB+ZrKpOG1zppYTES1UTtvHWsQrLaWsDGQopJRD09zRXhM9xNa3DmbVZJZWOWMbYGTRWLqq52xy2pbWSO7t9QluC0cyRuAeCV5FU7i4ktr3dCSjqfldSQR+OaKKw6Hs2Sm0gu9U1C4jKy3s7Arzl/aqNlq+oW0ZjgvJo0yeA5xRRTcnfcqNKny25V9xRvp5bxt1zI8pB43nNQAAJ90HHaiis222bxjGKskVZruSP7iouO4FZd3fXMpw8rEemaKKI7mdbREUU2wf6uNie7DJooorsjseRL4mf/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the image in glassware?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="False")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

