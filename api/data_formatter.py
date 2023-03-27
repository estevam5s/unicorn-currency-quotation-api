class DataFormatter:

    @staticmethod
    def format_currency_quotation(cotacao):
        formatted_output = []
        formatted_output.append('Cotação do Dólar: R$ {}'.format(cotacao['USDBRL']['bid']))
        formatted_output.append('Cotação do Euro: R$ {}'.format(cotacao['EURBRL']['bid']))
        formatted_output.append('Cotação do Bitcoin: R$ {}'.format(cotacao['BTCBRL']['bid']))

        return formatted_output

    @staticmethod
    def print_formatted_output(formatted_output):
        for line in formatted_output:
            print(line)
