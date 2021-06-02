"""Because No one likes taxes They get their own script so that they can be as far away from all the honest folk as
possible"""
import configReader
rules = configReader.rulesFileReader()


def taxes(company):
    # 50 means 50%, 10 000 000 means company value who could get 50% tax rate
    if company.profits <= 0:
        return
    tax, richCompany = rules['rules']['taxes']['tax'], rules['rules']['taxes']['richCompany']
    if company.profits < richCompany:
        tax = tax * (company.profits / richCompany)
    if company.isClean:
        tax -= 5
    if company.isEqual:
        tax -= 5
    taxesOwed = company.profits * (tax / 100)
    company.cash -= taxesOwed


# Because corruption is basically the same as taxes is it not.
def Corruption():
    pass
