from flamapy.core.discover import DiscoverMetamodels


def model_validator(model):
    """ 
    This operation is used to validate a model:
    It returns True if the model is valid, False otherwise. 
    If the model does not follow the UVL specification, an 
    exception is raised and the operation returns False.
    """

    # Use the operation from the DiscoverMetamodels class
    dm = DiscoverMetamodels()

    # Try to use the Valid operation, which returns True if the model is valid
    try:
        return dm.use_operation_from_file('Valid', model)
    # If the model does not follow the UVL specification, an exception is raised
    except:
        return False

def product_validator(model, product):
    return 'API operation for checking product'