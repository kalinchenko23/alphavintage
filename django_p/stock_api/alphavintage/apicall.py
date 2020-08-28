import requests
import json
import os
with open("/etc/config.json") as config_file:
    config=json.load(config_file)


api_key=config.get["API_KEY"]

class InfoGatheringCompany():




    def company_overview(self,company_name):
        url=f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={company_name}&apikey={api_key}"
        r=requests.get(url)
        result=r.json()
        result_modified=json.dumps(result,indent=2)
        return result

    def income_statement(self,company_name):
        url=f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={company_name}&apikey={api_key}"
        r=requests.get(url)
        result=r.json()
        result_modified=json.dumps(result,indent=2)
        return result

    def balanse_sheet(self,company_name):
        url=f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={company_name}&apikey={api_key}"
        r=requests.get(url)
        result=r.json()
        result_modified=json.dumps(result,indent=2)
        return result

    def cash_flow(self,company_name):
        url=f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={company_name}&apikey={api_key}"
        try:
            r=requests.get(url)
            result=r.json()
            result_modified=json.dumps(result,indent=2)
        except KeyError:
                pass
        return result

    def get_currency_exchange_rate(self,from_currency,to_currency):
        url=f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}"
        r=requests.get(url)
        result=r.json()
        result_modified=json.dumps(result,indent=2)
        d={}
        if from_currency==None and to_currency==None:
            pass
        else:
            try:
                d["currancy_name"]=result["Realtime Currency Exchange Rate"]["2. From_Currency Name"]
                d["to_currency"]=result["Realtime Currency Exchange Rate"]["4. To_Currency Name"]
                d["exchange_rate"]=result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
                d["last_refreashed"]=result["Realtime Currency Exchange Rate"]["6. Last Refreshed"]
                d["bid_price"]=result["Realtime Currency Exchange Rate"]["8. Bid Price"]
                d["ask_price"]=result["Realtime Currency Exchange Rate"]["9. Ask Price"]
            except KeyError:
                pass

        return d


    def get_cryptocurrency_rate(self,currency):
        url=f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={currency}&to_currency=USD&apikey={api_key}"
        r=requests.get(url)
        result=r.json()
        result_modified=json.dumps(result,indent=2)
        d={}
        if currency==None:
            pass
        else:
            try:
                d["crypto_name"]=result["Realtime Currency Exchange Rate"]["2. From_Currency Name"]
                d["to_currency"]=result["Realtime Currency Exchange Rate"]["4. To_Currency Name"]
                d["exchange_rate"]=result["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
                d["last_refreashed"]=result["Realtime Currency Exchange Rate"]["6. Last Refreshed"]
                d["bid_price"]=result["Realtime Currency Exchange Rate"]["8. Bid Price"]
                d["ask_price"]=result["Realtime Currency Exchange Rate"]["9. Ask Price"]
            except KeyError:
                pass
        return d

    def get_daily_adjusted_stock(self,stock):
        url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock}&apikey={api_key}"
        r=requests.get(url)
        result=r.json()
        result_modified=json.dumps(result,indent=2)
        daily_adjused={}
        if stock==None:
            pass
        else:
            try:
                for keys,values in result["Time Series (Daily)"].items():
                    daily_adjused[keys]={
                    "open":values["1. open"],
                    "high":values["2. high"],
                    "low":values["3. low"],
                    "adjusted_close":values["5. adjusted close"],
                    "dividend_amount":values["7. dividend amount"],
                    "split_coefficient":values["8. split coefficient"]}
            except KeyError:
                pass

        return daily_adjused


    def get_daily_adjusted_stock_history(self,stock,date):
        url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock}&outputsize=full&apikey={api_key}"
        r=requests.get(url)
        result=r.json()
        result_modified=json.dumps(result,indent=2)
        daily_adjused={}
        if stock==None and date==None:
            pass
        else:
            try:
                for keys,values in result["Time Series (Daily)"].items():
                    if keys==date:
                        daily_adjused[keys]={
                        "open":values["1. open"],
                        "high":values["2. high"],
                        "low":values["3. low"],
                        "adjusted_close":values["5. adjusted close"],
                        "dividend_amount":values["7. dividend amount"],
                        "split_coefficient":values["8. split coefficient"]}
            except KeyError:
                pass

        return daily_adjused

    def us_sector_performance(self):
        url=f"https://www.alphavantage.co/query?function=SECTOR&apikey={api_key}"
        r=requests.get(url)
        result=r.json()
        d={}
        for keys,values in result.items():
            if keys=="Meta Data":
                continue
            else:
                try:
                    d[keys]={
                    "information_tech":values["Information Technology"],
                    "consumer":values["Consumer Discretionary"],
                    "comm_serv":values["Communication Services"],
                    "Utilities":values["Utilities"],
                    "Materials": values["Materials"],
                    "Financials": values["Financials"],
                    "Consumer_Staples": values["Consumer Staples"],
                    "Real_Estate": values["Real Estate"],
                    "Industrials": values["Industrials"],
                    "Health_Care": values["Health Care"],
                    "Energy": values["Energy"]
                    }
                except KeyError:
                    continue
                except TypeError:
                    continue
        return d
