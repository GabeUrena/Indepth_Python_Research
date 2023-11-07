import ecommerce.shipping #importing packages you start with the name of the package followed by a period, and then the name of the file
ecommerce.shipping.calc_shipping() # how you call the function


from ecommerce import shipping # import the entire module
shipping.calc_shipping()


from ecommerce.shipping import calc_shipping # make your calls shorter
calc_shipping()


