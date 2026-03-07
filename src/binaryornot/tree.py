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
                        if features[6] <= 0.031250:  # odd_null_ratio
                            if features[1] <= 0.625000:  # control_ratio
                                return False  # text (100.0%, n=1)
                            else:
                                return True  # binary (100.0%, n=1)
                        else:
                            if features[6] <= 0.562500:  # odd_null_ratio
                                return True  # binary (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                    else:
                        if features[17] <= 0.154762:  # longest_printable_run
                            if features[17] <= 0.003906:  # longest_printable_run
                                if features[1] <= 0.286364:  # control_ratio
                                    return False  # text (100.0%, n=1)
                                else:
                                    if features[3] <= 0.683333:  # high_byte_ratio
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                            else:
                                if features[17] <= 0.080128:  # longest_printable_run
                                    return False  # text (100.0%, n=1)
                                else:
                                    if features[4] <= 0.500000:  # utf8_valid
                                        if features[2] <= 0.375000:  # printable_ascii_ratio
                                            if features[6] <= 0.093750:  # odd_null_ratio
                                                return True  # binary (83.3%, n=1)
                                            else:
                                                return False  # text (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
                        else:
                            if features[4] <= 0.500000:  # utf8_valid
                                if features[7] <= 3.264621:  # byte_entropy
                                    if features[17] <= 0.292929:  # longest_printable_run
                                        if features[1] <= 0.041667:  # control_ratio
                                            if features[2] <= 0.541667:  # printable_ascii_ratio
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                return False  # text (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                                else:
                                    if features[1] <= 0.041667:  # control_ratio
                                        if features[3] <= 0.414286:  # high_byte_ratio
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            if features[3] <= 0.583333:  # high_byte_ratio
                                                return False  # text (75.0%, n=1)
                                            else:
                                                return True  # binary (100.0%, n=1)
                                    else:
                                        if features[3] <= 0.591667:  # high_byte_ratio
                                            return True  # binary (100.0%, n=1)
                                        else:
                                            return False  # text (100.0%, n=1)
                            else:
                                if features[0] <= 0.192308:  # null_ratio
                                    return False  # text (100.0%, n=1)
                                else:
                                    return True  # binary (100.0%, n=1)
            else:
                if features[7] <= 1.753445:  # byte_entropy
                    if features[4] <= 0.500000:  # utf8_valid
                        return True  # binary (100.0%, n=1)
                    else:
                        return False  # text (100.0%, n=1)
                else:
                    if features[7] <= 3.090379:  # byte_entropy
                        if features[20] <= 0.500000:  # try_shift_jis
                            return False  # text (100.0%, n=1)
                        else:
                            return True  # binary (100.0%, n=1)
                    else:
                        if features[7] <= 3.279126:  # byte_entropy
                            return True  # binary (100.0%, n=1)
                        else:
                            return False  # text (100.0%, n=1)
        else:
            if features[3] <= 0.048438:  # high_byte_ratio
                if features[16] <= 0.500000:  # try_utf32be
                    return True  # binary (100.0%, n=1)
                else:
                    if features[1] <= 0.975000:  # control_ratio
                        return False  # text (100.0%, n=1)
                    else:
                        return True  # binary (100.0%, n=1)
            else:
                if features[7] <= 1.187558:  # byte_entropy
                    return True  # binary (100.0%, n=1)
                else:
                    return False  # text (100.0%, n=1)
    else:
        if features[4] <= 0.500000:  # utf8_valid
            if features[17] <= 0.045663:  # longest_printable_run
                if features[7] <= 5.183908:  # byte_entropy
                    if features[3] <= 0.992188:  # high_byte_ratio
                        if features[7] <= 3.469369:  # byte_entropy
                            return True  # binary (100.0%, n=1)
                        else:
                            if features[17] <= 0.041452:  # longest_printable_run
                                return False  # text (100.0%, n=1)
                            else:
                                if features[7] <= 4.450505:  # byte_entropy
                                    return False  # text (100.0%, n=1)
                                else:
                                    if features[2] <= 0.426660:  # printable_ascii_ratio
                                        return True  # binary (100.0%, n=1)
                                    else:
                                        return False  # text (100.0%, n=1)
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
                        if features[2] <= 0.571498:  # printable_ascii_ratio
                            if features[19] <= 0.500000:  # try_big5
                                if features[17] <= 0.082207:  # longest_printable_run
                                    if features[3] <= 0.651282:  # high_byte_ratio
                                        return False  # text (100.0%, n=1)
                                    else:
                                        return True  # binary (100.0%, n=1)
                                else:
                                    if features[3] <= 0.490000:  # high_byte_ratio
                                        if features[17] <= 0.166957:  # longest_printable_run
                                            if features[3] <= 0.416118:  # high_byte_ratio
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                return False  # text (100.0%, n=1)
                                        else:
                                            return True  # binary (100.0%, n=1)
                                    else:
                                        if features[17] <= 0.261364:  # longest_printable_run
                                            if features[2] <= 0.464103:  # printable_ascii_ratio
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                return True  # binary (80.0%, n=1)
                                        else:
                                            if features[3] <= 0.590909:  # high_byte_ratio
                                                return True  # binary (100.0%, n=1)
                                            else:
                                                return False  # text (100.0%, n=1)
                            else:
                                return False  # text (100.0%, n=1)
                        else:
                            if features[7] <= 3.921242:  # byte_entropy
                                if features[17] <= 0.199074:  # longest_printable_run
                                    return False  # text (100.0%, n=1)
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
                                        if features[2] <= 0.459416:  # printable_ascii_ratio
                                            if features[0] <= 0.116667:  # null_ratio
                                                return True  # binary (88.5%, n=1)
                                            else:
                                                return False  # text (100.0%, n=1)
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
