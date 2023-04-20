from requests import get, Response
class DoH:
    def __init__(self,dns_server='https://1.1.1.1/dns-query'):
        self.dns_server=dns_server
    
    def resolve(self,name, typ)->Response:
        headers = {'accept': 'application/dns-json'}

        params = {'name': name, 'type':typ}
        response = get('https://1.1.1.1/dns-query', params=params, headers=headers)
        return response

if __name__=='__main__':
    myDoH=DoH()
    ans=myDoH.resolve('iitmandi.co.in')
    print(ans)


