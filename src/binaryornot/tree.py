"""Auto-generated decision tree for binary/text classification.

Do not edit by hand. Regenerate with:
    uv run --with 'scikit-learn,numpy,hypothesis' python scripts/train_detector.py
"""


def is_binary(features):
    """Classify a byte chunk as binary or text.

    Takes the feature list from helpers._compute_features().
    Returns True for binary.
    """
    if features[2] <= 0.253743:  # printable_ascii_ratio
        if features[2] <= 0.027561:  # printable_ascii_ratio
            if features[3] <= 0.089193:  # high_byte_ratio
                if features[5] <= 0.992188:  # even_null_ratio
                    return True
                else:
                    if features[7] <= 0.405639:  # byte_entropy
                        return True
                    else:
                        return False
            else:
                if features[3] <= 0.997696:  # high_byte_ratio
                    if features[0] <= 0.791667:  # null_ratio
                        if features[7] <= 3.150011:  # byte_entropy
                            return False
                        else:
                            if features[1] <= 0.221429:  # control_ratio
                                return False
                            else:
                                return True
                    else:
                        return True
                else:
                    if features[4] <= 0.500000:  # utf8_valid
                        return True
                    else:
                        return False
        else:
            if features[3] <= 0.038690:  # high_byte_ratio
                if features[5] <= 0.630841:  # even_null_ratio
                    return False
                else:
                    if features[6] <= 0.657143:  # odd_null_ratio
                        return False
                    else:
                        return True
            else:
                if features[0] <= 0.172184:  # null_ratio
                    if features[4] <= 0.500000:  # utf8_valid
                        if features[7] <= 2.849632:  # byte_entropy
                            return False
                        else:
                            if features[17] <= 0.042110:  # longest_printable_run
                                if features[5] <= 0.008789:  # even_null_ratio
                                    return False
                                else:
                                    return True
                            else:
                                if features[0] <= 0.077778:  # null_ratio
                                    return True
                                else:
                                    return False
                    else:
                        return False
                else:
                    if features[7] <= 4.071262:  # byte_entropy
                        return False
                    else:
                        if features[7] <= 4.083860:  # byte_entropy
                            return True
                        else:
                            return False
    else:
        if features[1] <= 0.005859:  # control_ratio
            if features[4] <= 0.500000:  # utf8_valid
                if features[13] <= 0.500000:  # try_utf16le
                    if features[7] <= 4.424946:  # byte_entropy
                        if features[7] <= 2.984468:  # byte_entropy
                            return False
                        else:
                            if features[17] <= 0.163880:  # longest_printable_run
                                if features[2] <= 0.376518:  # printable_ascii_ratio
                                    return True
                                else:
                                    return False
                            else:
                                if features[2] <= 0.533937:  # printable_ascii_ratio
                                    return True
                                else:
                                    return True
                    else:
                        return False
                else:
                    if features[17] <= 0.118056:  # longest_printable_run
                        if features[7] <= 4.497743:  # byte_entropy
                            return False
                        else:
                            return True
                    else:
                        if features[17] <= 0.193750:  # longest_printable_run
                            if features[2] <= 0.527778:  # printable_ascii_ratio
                                if features[17] <= 0.177083:  # longest_printable_run
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return True
            else:
                return False
        else:
            if features[7] <= 3.272831:  # byte_entropy
                if features[0] <= 0.521277:  # null_ratio
                    if features[1] <= 0.105556:  # control_ratio
                        if features[17] <= 0.229437:  # longest_printable_run
                            return False
                        else:
                            return True
                    else:
                        if features[2] <= 0.607692:  # printable_ascii_ratio
                            return False
                        else:
                            if features[13] <= 0.500000:  # try_utf16le
                                return False
                            else:
                                return True
                else:
                    if features[17] <= 0.061784:  # longest_printable_run
                        return False
                    else:
                        if features[1] <= 0.652482:  # control_ratio
                            return True
                        else:
                            return False
            else:
                if features[2] <= 0.468736:  # printable_ascii_ratio
                    if features[7] <= 4.433619:  # byte_entropy
                        if features[17] <= 0.063636:  # longest_printable_run
                            if features[17] <= 0.051316:  # longest_printable_run
                                return False
                            else:
                                if features[7] <= 4.049795:  # byte_entropy
                                    return False
                                else:
                                    return True
                        else:
                            if features[4] <= 0.500000:  # utf8_valid
                                if features[1] <= 0.044466:  # control_ratio
                                    return False
                                else:
                                    return True
                            else:
                                return False
                    else:
                        if features[4] <= 0.500000:  # utf8_valid
                            return True
                        else:
                            return False
                else:
                    if features[17] <= 0.077381:  # longest_printable_run
                        if features[17] <= 0.056763:  # longest_printable_run
                            return False
                        else:
                            if features[17] <= 0.058397:  # longest_printable_run
                                return True
                            else:
                                return False
                    else:
                        if features[7] <= 3.987709:  # byte_entropy
                            if features[17] <= 0.193750:  # longest_printable_run
                                if features[13] <= 0.500000:  # try_utf16le
                                    return False
                                else:
                                    return True
                            else:
                                if features[3] <= 0.433036:  # high_byte_ratio
                                    return True
                                else:
                                    return False
                        else:
                            if features[1] <= 0.022002:  # control_ratio
                                return False
                            else:
                                if features[1] <= 0.040833:  # control_ratio
                                    return True
                                else:
                                    return True
