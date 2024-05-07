from dice_roll import unbiased_dice, biased_dice_on_left, biased_dice_on_right, dice_faces
import pytest

@pytest.mark.parametrize("input_value", ['i', '%', 'r', '.'])
def test_unbiased_dice_with_invalid_input(input_value):
    with pytest.raises(ValueError):
        unbiased_dice(input_value)
    print(f"Test passed: {input_value} raised ValueError as expected")

@pytest.mark.parametrize("input_value", ['i', '%', 'r', '.'])
def test_biased_dice_on_left_with_invalid_input(input_value):
    with pytest.raises(ValueError):
        biased_dice_on_left(input_value)
    print(f"Test passed: {input_value} raised ValueError as expected")

@pytest.mark.parametrize("input_value", ['i', '%', 'r', '.'])
def test_biased_dice_on_right_with_invalid_input(input_value):
    with pytest.raises(ValueError):
        biased_dice_on_right(input_value)
    print(f"Test passed: {input_value} raised ValueError as expected")

@pytest.mark.parametrize("input_value", ['i', '%', 'r', '.'])
def test_dice_faces_with_invalid_input(input_value):
    with pytest.raises(ValueError):
        dice_faces(input_value)
    print(f"Test passed: {input_value} raised ValueError as expected")