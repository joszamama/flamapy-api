import sys
import warnings
import pytest

sys.path.append("..")
warnings.filterwarnings("ignore", category=DeprecationWarning)

from app import app
from operations.validate import model_validator, product_validator
from operations.count import count_valid_products, count_leafs
from operations.find import find_valid_products, find_core_features
from operations.info import get_plugins, get_operations



def test_get_plugins():
    # Arrange

    # Act
    result = get_plugins()

    # Assert
    assert len(result) > 0


def test_get_operations():
    # Arrange
    plugin = "pysat_metamodel"

    # Act
    result = get_operations(plugin)

    # Assert
    assert len(result) > 0


def test_model_validator_valid_model():
    # Arrange
    valid_model = "../operations/models/valid_model.uvl"

    # Act
    result = model_validator(valid_model)

    # Assert
    assert result == True


def test_model_validator_invalid_model():
    # Arrange
    invalid_model = "../operations/products/valid_product.csv"

    # Act
    result = model_validator(invalid_model)

    # Assert
    assert result == False

# def test_product_validator_valid_product():
#     # Arrange
#     valid_model = "../operations/products/valid_model.uvl"
#     valid_product = "../operations/products/valid_product.csv"

#     # Act
#     result = product_validator(valid_model, valid_product)

#     # Assert
#     assert result == True

# def test_product_validator_invalid_product():
#     # Arrange
#     valid_model = "../operations/products/valid_model.uvl"
#     invalid_product = "../operations/products/invalid_product.csv"

#     # Act
#     result = product_validator(valid_model, invalid_product)

#     # Assert
#     assert result == False


def test_count_valid_products():
    # Arrange
    valid_model = "../operations/models/valid_model.uvl"

    # Act
    result = count_valid_products(valid_model)

    # Assert
    assert result == 816


def test_count_leafs():
    # Arrange
    valid_model = "../operations/models/valid_model.uvl"

    # Act
    result = count_leafs(valid_model)

    # Assert
    assert result == 17


def test_find_valid_products():
    # Arrange
    valid_model = "../operations/models/valid_model.uvl"

    # Act
    result = find_valid_products(valid_model)

    # Assert
    assert len(result) > 0


def test_find_core_features():
    # Arrange
    valid_model = "../operations/models/valid_model.uvl"
    core_features = ["eCommerce", "Server", "Web", "Catalog", "Search",
                     "Shopping", "Security",  "Cart", "Payment", "PHP", "Storage", "v74"]
    # Act
    result = find_core_features(valid_model)

    # Assert
    assert result == core_features
