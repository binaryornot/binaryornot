"""Auto-generated decision tree for binary/text classification.

Do not edit by hand. Regenerate with:
    uv run --with 'scikit-learn,numpy,hypothesis' python scripts/train_detector.py
"""


def is_binary(features):
    """Classify a byte chunk as binary or text.

    Takes the feature list from helpers._compute_features().
    Returns True for binary.
    """
    if features[7] <= 3.457998:  # byte_entropy
        if features[1] <= 0.796165:  # control_ratio
            if features[3] <= 0.972656:  # high_byte_ratio
                if features[7] <= 3.041395:  # byte_entropy
                    if features[1] <= 0.753906:  # control_ratio
                        if features[20] <= 0.500000:  # try_shift_jis
                            return False  # text (100.0%, n=1)
                        else:
                            if features[6] <= 0.596875:  # odd_null_ratio
                                return False  # text (100.0%, n=1)
                            else:
                                if features[5] <= 0.550000:  # even_null_ratio
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                    else:
                        if features[2] <= 0.180990:  # printable_ascii_ratio
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                else:
                    if features[7] <= 3.092967:  # byte_entropy
                        if features[1] <= 0.610705:  # control_ratio
                            if features[3] <= 0.613281:  # high_byte_ratio
                                return False  # text (100.0%, n=1)
                            else:
                                if features[6] <= 0.031250:  # odd_null_ratio
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                    else:
                        if features[17] <= 0.154762:  # longest_printable_run
                            if features[17] <= 0.003906:  # longest_printable_run
                                if features[3] <= 0.713636:  # high_byte_ratio
                                    if features[10] <= 0.500000:  # bom_utf16le
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                            else:
                                if features[17] <= 0.080128:  # longest_printable_run
                                    return False  # text (100.0%, n=1)
                                else:
                                    if features[4] <= 0.500000:  # utf8_valid
                                        if features[2] <= 0.375000:  # printable_ascii_ratio
                                            if features[1] <= 0.202020:  # control_ratio
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                return False  # text (75.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                        else:
                            if features[4] <= 0.500000:  # utf8_valid
                                if features[17] <= 0.174242:  # longest_printable_run
                                    if features[7] <= 3.349666:  # byte_entropy
                                        return False  # text (100.0%, n=1)
                                    else:
                                        if features[2] <= 0.458333:  # printable_ascii_ratio
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            return False  # text (50.0%, n=1)
                                else:
                                    if features[13] <= 0.500000:  # try_utf16le
                                        if features[3] <= 0.572727:  # high_byte_ratio
                                            if features[7] <= 3.186779:  # byte_entropy
                                                return False  # text (50.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        if features[7] <= 3.350356:  # byte_entropy
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            if features[17] <= 0.315476:  # longest_printable_run
                                                return False  # text (100.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                            else:
                                if features[5] <= 0.192308:  # even_null_ratio
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
            else:
                if features[4] <= 0.500000:  # utf8_valid
                    if features[7] <= 1.953445:  # byte_entropy
                        return True  # binary (100.0%, n=1)
                    else:
                        if features[7] <= 2.860666:  # byte_entropy
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                else:
                    return False  # text (100.0%, n=1)
        else:
            if features[3] <= 0.048438:  # high_byte_ratio
                if features[5] <= 0.962963:  # even_null_ratio
                    return True  # binary (100.0%, n=1)
                else:
                    if features[6] <= 0.800000:  # odd_null_ratio
                        return False  # text (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
            else:
                if features[0] <= 0.791667:  # null_ratio
                    return False  # text (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
    else:
        if features[4] <= 0.500000:  # utf8_valid
            if features[17] <= 0.045663:  # longest_printable_run
                if features[7] <= 5.183908:  # byte_entropy
                    if features[2] <= 0.011719:  # printable_ascii_ratio
                        return True  # binary (100.0%, n=1)
                    else:
                        if features[1] <= 0.575621:  # control_ratio
                            if features[17] <= 0.041452:  # longest_printable_run
                                return False  # text (100.0%, n=1)
                            else:
                                if features[7] <= 4.450505:  # byte_entropy
                                    return False  # text (100.0%, n=1)
                                else:
                                    if features[3] <= 0.502389:  # high_byte_ratio
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                else:
                    if features[2] <= 0.476415:  # printable_ascii_ratio
                        return True  # binary (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
            else:
                if features[1] <= 0.028595:  # control_ratio
                    if features[17] <= 0.354353:  # longest_printable_run
                        if features[3] <= 0.456439:  # high_byte_ratio
                            if features[2] <= 0.601190:  # printable_ascii_ratio
                                if features[17] <= 0.128289:  # longest_printable_run
                                    if features[3] <= 0.394444:  # high_byte_ratio
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
                            else:
                                if features[13] <= 0.500000:  # try_utf16le
                                    if features[17] <= 0.252381:  # longest_printable_run
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                                else:
                                    return False  # text (100.0%, n=1)
                        else:
                            if features[19] <= 0.500000:  # try_big5
                                if features[17] <= 0.074176:  # longest_printable_run
                                    if features[2] <= 0.333333:  # printable_ascii_ratio
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                                else:
                                    if features[2] <= 0.458042:  # printable_ascii_ratio
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        if features[17] <= 0.163333:  # longest_printable_run
                                            if features[3] <= 0.490000:  # high_byte_ratio
                                                return False  # text (100.0%, n=1)
                                            else:
                                                return True  # binary (66.7%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
                else:
                    if features[10] <= 0.500000:  # bom_utf16le
                        if features[11] <= 0.500000:  # bom_utf16be
                            if features[6] <= 0.499089:  # odd_null_ratio
                                if features[7] <= 4.385591:  # byte_entropy
                                    if features[17] <= 0.094494:  # longest_printable_run
                                        if features[0] <= 0.116667:  # null_ratio
                                            if features[2] <= 0.404211:  # printable_ascii_ratio
                                                return True  # binary (95.5%, n=1)
                                            else:
                                                return False  # text (84.6%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        if features[2] <= 0.651515:  # printable_ascii_ratio
                                            if features[2] <= 0.456439:  # printable_ascii_ratio
                                                return True  # binary (99.0%, n=1)
                                            else:
                                                return True  # binary (87.9%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                else:
                                    if features[2] <= 0.471743:  # printable_ascii_ratio
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        if features[17] <= 0.071429:  # longest_printable_run
                                            return False  # text (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
        else:
            if features[1] <= 0.207945:  # control_ratio
                if features[6] <= 0.076786:  # odd_null_ratio
                    return False  # text (100.0%, n=1)
                else:
                    return True  # binary (100.0%, n=1)
            else:
                if features[0] <= 0.356383:  # null_ratio
                    return True  # binary (100.0%, n=1)
                else:
                    return False  # text (100.0%, n=1)
