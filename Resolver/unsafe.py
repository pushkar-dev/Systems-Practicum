import dns.resolver

answers = dns.resolver.resolve('iitmandi.co.in')
for rdata in answers:
    print(rdata)