from urllib.request import urlopen
from urllib.error import URLError, HTTPError

def testar_site():

    url = 'https://www.iefp.pt'

    try:
        resposta = urlopen(url, timeout=5)

        print('\nO site do IEFP está acessível.')

        resposta.close()

    except HTTPError as e:

        print(f'\nO site respondeu com erro HTTP: {e.code}')

    except URLError:

        print('\nNão foi possível ligar ao site do IEFP.')

    except Exception:

        print('\nOcorreu um erro inesperado.')


testar_site()