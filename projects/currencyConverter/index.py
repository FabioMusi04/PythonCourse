import streamlit as st
import requests
import json 
import pandas as pd


exchange_rates = {
    'USD': {'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0, 'AUD': 1.35, 'CAD': 1.25},
    'EUR': {'USD': 1.18, 'GBP': 0.88, 'JPY': 129.53, 'AUD': 1.59, 'CAD': 1.47},
    'GBP': {'USD': 1.33, 'EUR': 1.14, 'JPY': 147.0, 'AUD': 1.80, 'CAD': 1.67},
    'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0068, 'AUD': 0.012, 'CAD': 0.011},
    'AUD': {'USD': 0.74, 'EUR': 0.63, 'GBP': 0.56, 'JPY': 82.0, 'CAD': 0.93},
    'CAD': {'USD': 0.80, 'EUR': 0.68, 'GBP': 0.60, 'JPY': 88.0, 'AUD': 1.07}
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency == to_currency:
        return amount
    return amount * exchange_rates[from_currency][to_currency]

def fetch_data(cur, cur2, amount):
    res = requests.get(f"https://economia.awesomeapi.com.br/json/last/{cur}-{cur2}")
    response = json.loads(res.text)
    st.write(response)

    if "status" not in response:
        exchange_rate = response[f'{cur}{cur2}']['high']
        converted_amount = float(amount) * float(exchange_rate)
        st.success(f'{float(amount)} {cur} is equal to {converted_amount:.2f} {cur2}')
    elif response['status'] == 404:
        st.error('An error occurred while fetching data from the API.')
        return

st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Esercizio 1', 'Esercizio 2', 'Esercizio 3', 'Esercizio 4'])

if page == 'Esercizio 1':
    st.title('Currency Converter')

    from_currency = st.selectbox('From Currency', options=list(exchange_rates.keys()))
    to_currency = st.selectbox('To Currency', options=list(exchange_rates.keys()))

    amount = st.number_input('Amount', min_value=0.0, format="%.2f")

    if st.button('Convert'):
        if from_currency == to_currency:
            st.warning('The two currencies must be different for conversion.')
        else:
            converted_amount = convert_currency(amount, from_currency, to_currency)
            st.success(f'{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}')

elif page == 'Esercizio 2':
    st.title('Currency Converter')

    from_currency = st.selectbox('From Currency', options=list(exchange_rates.keys()))
    to_currency = st.selectbox('To Currency', options=list(exchange_rates.keys()))

    amount = st.number_input('Amount', min_value=0.0, format="%.2f", key='amount_input')

    if st.session_state.amount_input:
            fetch_data(from_currency, to_currency, st.session_state.amount_input)

elif page == 'Esercizio 3':
    class CurrencyModel:
        def __init__(self):
            self.exchange_rates = {
                'USD': {'EUR': 0.85, 'GBP': 0.75, 'JPY': 110.0, 'AUD': 1.35, 'CAD': 1.25},
                'EUR': {'USD': 1.18, 'GBP': 0.88, 'JPY': 129.53, 'AUD': 1.59, 'CAD': 1.47},
                'GBP': {'USD': 1.33, 'EUR': 1.14, 'JPY': 147.0, 'AUD': 1.80, 'CAD': 1.67},
                'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0068, 'AUD': 0.012, 'CAD': 0.011},
                'AUD': {'USD': 0.74, 'EUR': 0.63, 'GBP': 0.56, 'JPY': 82.0, 'CAD': 0.93},
                'CAD': {'USD': 0.80, 'EUR': 0.68, 'GBP': 0.60, 'JPY': 88.0, 'AUD': 1.07}
            }

        def fetch_data(self, cur, cur2, amount):
            res = requests.get(f"https://economia.awesomeapi.com.br/json/last/{cur}-{cur2}")
            response = json.loads(res.text)
            if "status" not in response:
                exchange_rate = response[f'{cur}{cur2}']['high']
                converted_amount = float(amount) * float(exchange_rate)
                return converted_amount
            elif response['status'] == 404:
                return None


    class CurrencyView:
        def display_result(self, amount, from_currency, to_currency, converted_amount):
            st.success(f'{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}')

        def display_error(self, message):
            st.error(message)


    class CurrencyController:
        def __init__(self, model, view):
            self.model = model
            self.view = view

        def handle_fetch_data(self, from_currency, to_currency, amount):
            converted_amount = self.model.fetch_data(from_currency, to_currency, amount)
            if converted_amount is not None:
                self.view.display_result(amount, from_currency, to_currency, converted_amount)
            else:
                self.view.display_error('An error occurred while fetching data from the API.')


    model = CurrencyModel()
    view = CurrencyView()
    controller = CurrencyController(model, view)

    st.title('Currency Converter')

    from_currency = st.selectbox('From Currency', options=list(model.exchange_rates.keys()))
    to_currency = st.selectbox('To Currency', options=list(model.exchange_rates.keys()))

    amount = st.number_input('Amount', min_value=0.0, format="%.2f", key='amount_input')

    if st.session_state.amount_input:
        controller.handle_fetch_data(from_currency, to_currency, st.session_state.amount_input)

elif page == 'Esercizio 4':
    import matplotlib.pyplot as plt

    class CryptoModel:
        def fetch_crypto_data(self, crypto, currency, days):
            url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency={currency}&days={days}"
            res = requests.get(url)
            data = res.json()
            prices = data['prices']
            return prices

    class CryptoView:
        def display_chart(self, prices, crypto, currency):
            df = pd.DataFrame(prices, columns=['Timestamp', 'Price'])
            df['Date'] = pd.to_datetime(df['Timestamp'], unit='ms')
            plt.figure(figsize=(10, 5))
            plt.plot(df['Date'], df['Price'], label=f'{crypto} Price')
            plt.xlabel('Date')
            plt.ylabel(f'Price in {currency}')
            plt.title(f'{crypto} Price Over Time')
            plt.legend()
            st.pyplot(plt)

        def display_error(self, message):
            st.error(message)

    class CryptoController:
        def __init__(self, model, view):
            self.model = model
            self.view = view

        def handle_fetch_data(self, crypto, currency, days):
            prices = self.model.fetch_crypto_data(crypto, currency, days)
            if prices:
                self.view.display_chart(prices, crypto, currency)
            else:
                self.view.display_error('An error occurred while fetching data from the API.')

    model = CryptoModel()
    view = CryptoView()
    controller = CryptoController(model, view)

    st.title('Cryptocurrency Price Tracker')

    crypto = st.selectbox('Cryptocurrency', options=['bitcoin', 'ethereum', 'ripple', 'litecoin'])
    currency = st.selectbox('Currency', options=['usd', 'eur', 'gbp'])
    days = st.number_input('Days', min_value=1, max_value=365, value=30)

    if st.button('Show Chart'):
        controller.handle_fetch_data(crypto, currency, days)