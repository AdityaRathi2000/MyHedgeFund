def start_html():
  return '<html>\n <body>'

def style():
  return '<head>\n <style>\n table, th, td {\n border: 1px solid black;\n}\n ' \
         'body {background: url(double-bubble-outline.png) repeat 0 0;} \n ' \
         'h1 {Nobile, Helvetica, Arial, sans-serif; font-size: 200%} \n ' \
         'h2 {font-family: Helvetica; font-size: 180%} \n ' \
         'h3 {font-family: Helvetica; color: blue; font-size: 180%} \n ' \
         'p {font-family: Helvetica; font-size: 100%}\n ' \
         '#graph {float: left; width:500px; height:500px; border: 1px solid grey;}\n ' \
         'g {font-family: Helvetica; color: green; font-size: 100%}\n ' \
         'r {font-family: Helvetica; color: red; font-size: 100%}\n </style>\n</head>'

def end_html():
  return '</body> \n </html>'

def new_table(df_1):
  table = "<table style='width:100%'>\n"
  counter = 0

  table = table + "\n<tr>\n"
  for i in df_1.columns:
    table = table + "<th>{}</th>".format(i)
  table = table + "\n</tr>\n"

  for numbers in range(len(df_1.index)):
    table = table + "\n<tr>\n"
    for col_name in df_1.columns:
      table = table + "<th style='font-weight:normal'>{}</th>".format(df_1.loc[numbers, col_name])
    table = table + "\n</tr>\n"

  table = table + "\n</table>"
  return table

def print_html(text):
  text = str(text)
  text = text.replace('\n', '<br>')
  return '<p>' + str(text) + '</p>'

def print_html_bold(text):
  text = str(text)
  return '<strong>' + str(text) + '</strong>'

def graph_imgs(g_name, company, width, height, filePath_no_idx):
  return '<Center><img src="{}/{}.png"  width="{}" height="{}"></Center>'.format(filePath_no_idx, g_name, width, height)
