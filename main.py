import datetime as dt
from selenium import webdriver
import MHF_fundamentals as mhf_f
import MHF_html as mhf_html

if __name__ == '__main__':
  filePath = "file:///Users/adityarathi/Downloads/MyHedgeFund-main/index.html"

  start = dt.datetime(2020, 9, 1)
  end = dt.datetime.now().date()
  end_diff_format = end.strftime('%m/%d/%Y')
  year = 2020

  var = input("Please enter ticker symbol of company you are interested in: ")
  watchList = [var]
  watching = 0

  ttm_ROE = 0;
  sector_var = ""
  industry_var = ""

  # 0 - unclear, 1 - buy, 2 - sell
  tracking_fundamentals = ["Total Revenue", "Gross Profit", "Operating Expense", "Operating Income", \
                           "Basic EPS", "Normalized Income", "EBIT"]
  globalResultsDict = {}
  for i in tracking_fundamentals:
      globalResultsDict[i] = 0

  req_headers = {
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'en-US,en;q=0.8',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
  }

  df_financials = mhf_f.financial_table(watchList[watching], end_diff_format, req_headers)
  sector_industry_list = mhf_f.sector_industry(watchList[watching], req_headers)

  mhf_f.four_year_increasing(df_financials, "Total Revenue", globalResultsDict)
  mhf_f.four_year_increasing(df_financials, "Gross Profit", globalResultsDict)
  mhf_f.four_year_decreasing(df_financials, "Operating Expense", globalResultsDict)
  mhf_f.four_year_increasing(df_financials, "Operating Income", globalResultsDict)
  mhf_f.four_year_increasing_noTTM(df_financials, "Basic EPS", globalResultsDict)
  mhf_f.four_year_increasing(df_financials, "Normalized Income", globalResultsDict)
  mhf_f.four_year_increasing(df_financials, "EBIT", globalResultsDict)

  competitor_df = mhf_f.competitor_func(watchList[watching], req_headers)
  news_df = mhf_f.news_df_create(watchList[watching], req_headers)
  insider_df = mhf_f.insider_df_creation(watchList[watching], req_headers)
  etf_df = mhf_f.etf_exposure_create(watchList[watching], req_headers)
  analysis_list = mhf_f.competitor_analysis(competitor_df, watchList[watching])

  webpage_data = mhf_html.start_html()
  webpage_data += mhf_html.style()

  webpage_data += mhf_html.print_html("<Center><h1> Welcome to My Hedge Fund. You are now looking at ticker symbol <r>{}</r>\n </h1></Center> ".format(mhf_html.print_html_bold(watchList[watching])))
  webpage_data += mhf_html.print_html("<Center><p> {} is part of <r>{}</r> sector and <r>{}</r> industry\n </p></Center>".format(watchList[watching], mhf_html.print_html_bold(sector_industry_list[0]), mhf_html.print_html_bold(sector_industry_list[1])))

  webpage_data += mhf_html.print_html_bold("<h3>Financials: </h3>")

  webpage_data += mhf_html.new_table(df_financials)
  webpage_data += mhf_html.print_html(" ")

  webpage_data += mhf_html.print_html_bold("<h3>Peer Comparison: </h3>")
  webpage_data += mhf_html.new_table(competitor_df)
  for i in analysis_list:
    webpage_data += mhf_html.print_html(i)

  webpage_data += mhf_html.print_html_bold("<h3>Current Affairs: </h3>")
  webpage_data += mhf_html.new_table(news_df)
  webpage_data += mhf_html.print_html(" ")

  webpage_data += mhf_html.print_html_bold("<h3>Insider Trading: </h3>")
  webpage_data += mhf_html.new_table(insider_df)
  webpage_data += mhf_html.print_html(" ")

  webpage_data += mhf_html.print_html_bold("<h3>ETF Involvement: </h3>")
  webpage_data += mhf_html.new_table(etf_df)
  webpage_data += mhf_html.print_html(" ")

  webpage_data += mhf_html.print_html(" ")
  webpage_data += mhf_html.print_html_bold("<h3>Fundamentals: </h3>")

  for i in tracking_fundamentals:
    webpage_data += mhf_html.print_html("<div id='graph'>")
    webpage_data += mhf_html.print_html("<Center>{}</Center>".format(mhf_html.print_html_bold(i)))
    if (globalResultsDict[i] == 'Buy'):
        webpage_data += mhf_html.print_html("<Center>Recommendation based on trend: <g>{}</g></Center>".format(mhf_html.print_html_bold(globalResultsDict[i])))
    else:
        webpage_data += mhf_html.print_html("<Center>Recommendation based on trend: <r>{}</r></Center>".format(mhf_html.print_html_bold(globalResultsDict[i])))
    webpage_data += mhf_html.graph_imgs(i, watchList[watching], 460, 345)
    webpage_data += mhf_html.print_html("</div>")

  webpage_data += mhf_html.end_html()
  with open('index.html', 'w') as fd:
      fd.write(webpage_data)

  driver = webdriver.Chrome(executable_path="/Users/adityarathi/Documents/chromedriver")
  driver.get(filePath)

########################################################################################################
########################################################################################################
########################################################################################################
